
%define		_theme		revolution

Summary:	The Revolution KDM theme
Summary(pl):	Motyw KDM Revolution
Name:		kdm-theme-%{_theme}
Version:	01
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/23531-%{_theme}_kdm_theme.tar.bz2
# Source0-md5:	00ec01fc0e4ec5b4b44793b2a03ffa7b
URL:		http://www.kde-look.org/content/show.php?content=23531
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Revolution of KDM Theme.

%description -l pl
Motyw KDM Revolution.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}_kdm_theme/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
