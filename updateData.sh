#!/bin/bash

# The tool in question should be the tool_wrapper script in mlsdbtool, in the
# geoclue-providers-mlsdb repository here:
# https://github.com/mer-hybris/geoclue-providers-mlsdb

# The file is the MLS-full-cell-export csv file found here:
# https://location.services.mozilla.com/downloads

TOOL="$1"
FILE="$2"
SPEC="rpm/mlsdb-data.spec"

if [ -z "$FILE" ] ; then
  echo "Usage: $0 [tool] [mls_data_file]" >&2
  exit 1
fi
if [ ! -x "$TOOL" ] ; then
  echo "ERROR: $TOOL must be an executable" >&2
  exit 1
fi

REGIONS="Eastern_Europe Northern_Europe Western_Europe Southern_Europe Australia India"
Northern_Europe="dk ee fi is ie lv lt no se gb"
Southern_Europe="al ad ba hr gr it mk mt me pt sm rs si es"
Western_Europe="at be fr de li mc nl ch" # Also lu, but mcc 270 is included in be
Eastern_Europe="by bg cz hu md pl ro sk ua"
Australia="au"
India="in"

cat <<EOF > $SPEC
Name: mlsdb-data
Version: 0.2
Release: 1
Summary: Geoinformation data from Mozilla Location Services Geoclue provider
URL: https://github.com/sailfishos/mlsdb-data/
License: Public Domain
Source0: %{name}-%{version}.tar.gz
BuildRequires: qt5-tools
BuildRequires: qt5-qttools-linguist

%description
%{summary}.

%package australia
Summary: Mozilla Location Services data for Australia
%description australia
%{summary}.

%package india
Summary: Mozilla Location Services data for India
%description india
%{summary}.

%package northern-europe
Summary: Mozilla Location Services data for Northern Europe
%description northern-europe
Includes data for Denmark, Estonia, Finland, Iceland, Ireland,
Latvia, Lithuania, Norway, Sweden and United Kingdom.

%package western-europe
Summary: Mozilla Location Services data for Western Europe
%description western-europe
Includes data for Austria, Belgium, France, Germany, Liechtenstein,
Luxembourg, Monaco, Netherlands and Switzerland.

%package southern-europe
Summary: Mozilla Location Services data for Southern Europe
%description southern-europe
Includes data for Albania, Andorra, Bosnia and Herzegovina, Croatia,
Greece, Italy, Macedonia, Malta, Montenegro, Portugal, San Marino,
Serbia, Slovenia and Spain, but not including Holy See (Vatican).

%package eastern-europe
Summary: Mozilla Location Services data for Eastern
%description eastern-europe
Includes data for Belarus, Bulgaria, Czech Republic, Hungary,
Moldova, Poland, Romania, Slovakia and Ukraine.

%prep
%setup -q -n %{name}-%{version}

%build
lupdate . -ts mlsdb-data.ts

%install
mkdir -p %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp Australia/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp India/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp Northern_Europe/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp Western_Europe/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp Southern_Europe/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
cp Eastern_Europe/* %{buildroot}%{_datadir}/geoclue-provider-mlsdb/data
mkdir -p %{buildroot}%{_datadir}/translations/source
cp mlsdb-data.ts %{buildroot}%{_datadir}/translations/source

EOF

for region in $REGIONS; do
  mkdir -p "$region"
  echo "%files $region" | tr [:upper:] [:lower:] | tr '_' '-' >> $SPEC
  echo "%defattr(-,root,root,-)" >> $SPEC
  pushd "$region"
  # ${!var} is bash indirect referencing, i.e. accessing whatever is in the
  # variable with the name that is stored in $var.
  for country in ${!region} ; do
    mccs=`../"$TOOL" ../"$FILE" "$country" | sed 's/.*://'`
    for mcc in $mccs ; do
      echo "%{_datadir}/geoclue-provider-mlsdb/data/${mcc}.dat" >> ../$SPEC
    done
  done
  popd
  echo >> $SPEC
done

cat <<EOF >> $SPEC
%package ts-devel
Summary: Translations for MLS location data package descriptions in Store.

%description ts-devel
Translations for MLS location data package descriptions in Store.

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/mlsdb-data.ts
EOF
