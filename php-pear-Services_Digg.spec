%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Digg
%define		_status		alpha
%define		_pearname	Services_Digg
Summary:	%{_pearname} - PHP interface to Digg's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API Digg-a
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	45966f524a5fb60a773fd16438c314fb
URL:		http://pear.php.net/package/Services_Digg/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for accessing Digg's web services API at
http://services.digg.com.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet tne dostarcza interfejs umożliwiający dostęp do web services
Digg-a znajdujących się pod adresem http://services.digg.com

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Digg
