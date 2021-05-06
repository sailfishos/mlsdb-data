Name: mlsdb-data
Version: 0.1
Release: 1
Summary: Geoinformation data from Mozilla Location Services Geoclue provider
URL: https://github.com/sailfishos/mlsdb-data/
License: Public Domain
Source0: %{name}-%{version}.tar.gz
BuildRequires:  qt5-qttools-linguist
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
mkdir -p %{buildroot}%{_datadir}/geoclue-provider-mlsdb/
cp -r  Australia %{buildroot}%{_datadir}/geoclue-provider-mlsdb/
cp -r India %{buildroot}%{_datadir}/geoclue-provider-mlsdb
cp -r Northern_Europe %{buildroot}%{_datadir}/geoclue-provider-mlsdb
cp -r Western_Europe %{buildroot}%{_datadir}/geoclue-provider-mlsdb
cp -r Southern_Europe %{buildroot}%{_datadir}/geoclue-provider-mlsdb
cp -r Eastern_Europe %{buildroot}%{_datadir}/geoclue-provider-mlsdb
mkdir -p %{buildroot}%{_datadir}/translations/source
cp mlsdb-data.ts %{buildroot}%{_datadir}/translations/source

%files australia
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/Australia

%files india
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/India

%files northern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/Northern_Europe

%files western-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/Western_Europe

%files southern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/Southern_Europe

%files eastern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/Eastern_Europe

%package ts-devel
Summary: Translations for MLS location data package descriptions in Store.

%description ts-devel
Translations for MLS location data package descriptions in Store.

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/mlsdb-data.ts
