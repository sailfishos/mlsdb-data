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

%files australia
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/505.dat

%files india
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/404.dat
%{_datadir}/geoclue-provider-mlsdb/data/405.dat

%files northern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/234.dat
%{_datadir}/geoclue-provider-mlsdb/data/235.dat
%{_datadir}/geoclue-provider-mlsdb/data/238.dat
%{_datadir}/geoclue-provider-mlsdb/data/240.dat
%{_datadir}/geoclue-provider-mlsdb/data/242.dat
%{_datadir}/geoclue-provider-mlsdb/data/244.dat
%{_datadir}/geoclue-provider-mlsdb/data/246.dat
%{_datadir}/geoclue-provider-mlsdb/data/247.dat
%{_datadir}/geoclue-provider-mlsdb/data/248.dat
%{_datadir}/geoclue-provider-mlsdb/data/272.dat
%{_datadir}/geoclue-provider-mlsdb/data/274.dat

%files western-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/204.dat
%{_datadir}/geoclue-provider-mlsdb/data/206.dat
%{_datadir}/geoclue-provider-mlsdb/data/208.dat
%{_datadir}/geoclue-provider-mlsdb/data/212.dat
%{_datadir}/geoclue-provider-mlsdb/data/228.dat
%{_datadir}/geoclue-provider-mlsdb/data/232.dat
%{_datadir}/geoclue-provider-mlsdb/data/262.dat
%{_datadir}/geoclue-provider-mlsdb/data/270.dat
%{_datadir}/geoclue-provider-mlsdb/data/295.dat

%files southern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/202.dat
%{_datadir}/geoclue-provider-mlsdb/data/213.dat
%{_datadir}/geoclue-provider-mlsdb/data/214.dat
%{_datadir}/geoclue-provider-mlsdb/data/218.dat
%{_datadir}/geoclue-provider-mlsdb/data/219.dat
%{_datadir}/geoclue-provider-mlsdb/data/220.dat
%{_datadir}/geoclue-provider-mlsdb/data/222.dat
%{_datadir}/geoclue-provider-mlsdb/data/268.dat
%{_datadir}/geoclue-provider-mlsdb/data/276.dat
%{_datadir}/geoclue-provider-mlsdb/data/278.dat
%{_datadir}/geoclue-provider-mlsdb/data/292.dat
%{_datadir}/geoclue-provider-mlsdb/data/293.dat
%{_datadir}/geoclue-provider-mlsdb/data/294.dat
%{_datadir}/geoclue-provider-mlsdb/data/297.dat

%files eastern-europe
%defattr(-,root,root,-)
%{_datadir}/geoclue-provider-mlsdb/data/216.dat
%{_datadir}/geoclue-provider-mlsdb/data/226.dat
%{_datadir}/geoclue-provider-mlsdb/data/230.dat
%{_datadir}/geoclue-provider-mlsdb/data/231.dat
%{_datadir}/geoclue-provider-mlsdb/data/255.dat
%{_datadir}/geoclue-provider-mlsdb/data/257.dat
%{_datadir}/geoclue-provider-mlsdb/data/259.dat
%{_datadir}/geoclue-provider-mlsdb/data/260.dat
%{_datadir}/geoclue-provider-mlsdb/data/284.dat

%package ts-devel
Summary: Translations for MLS location data package descriptions in Store.

%description ts-devel
Translations for MLS location data package descriptions in Store.

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/mlsdb-data.ts
