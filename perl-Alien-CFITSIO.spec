#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	CFITSIO
Summary:	Alien::CFITSIO - Install the CFITSIO library
Summary(pl.UTF-8):	Alien::CFITSIO - instalacja biblioteki CFITSIO
Name:		perl-Alien-CFITSIO
Version:	4.4.0.2
Release:	4
License:	GPL v3
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	bd914ee4cb81359dc93b677e97ac64b7
URL:		https://metacpan.org/dist/Alien-CFITSIO
BuildRequires:	cfitsio-devel >= 4.4.0
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Alien-Build >= 0.32
BuildRequires:	perl-Package-Stash
BuildRequires:	perl-Test-Alien >= 2.39_01
BuildRequires:	perl-Test2-Suite
%endif
%requires_eq	cfitsio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# contains arch-dependent paths, but no binaries
%define		_enable_debug_packages	0

%description
This module finds or builds the CFITSIO library. It supports CFITSIO
version 4.4.0.

%description -l pl.UTF-8
Ten moduł znajduje lub buduje bibliotekę CFITSIO. Obsługuje wersję
4.4.0.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
export ALIEN_CFITSIO_ATLEAST_VERSION=4.4.0
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Alien/CFITSIO
%{perl_vendorarch}/Alien/CFITSIO.pm
%{perl_vendorarch}/auto/Alien/CFITSIO
%{perl_vendorarch}/auto/share/dist/Alien-CFITSIO
%{_mandir}/man3/Alien::CFITSIO.3pm*
