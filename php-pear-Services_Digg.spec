%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_Digg
Summary:	%{_pearname} - PHP interface to Digg's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API Digga
Name:		php-pear-%{_pearname}
Version:	0.4.7
Release:	4
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	11bf3da0e0bf74c01cee9a2dc300cc5c
URL:		http://pear.php.net/package/Services_Digg/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(curl)
Requires:	php-pear
Obsoletes:	php-pear-Services_Digg-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for accessing Digg's web services API at
<http://services.digg.com/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza interfejs umożliwiający dostęp do usług WWW
serwisu Digg znajdujących się pod adresem <http://services.digg.com/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Digg
%{php_pear_dir}/Services/Digg.php
