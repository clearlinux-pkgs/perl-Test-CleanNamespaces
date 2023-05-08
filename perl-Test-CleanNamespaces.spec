#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-CleanNamespaces
Version  : 0.24
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-CleanNamespaces-0.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-CleanNamespaces-0.24.tar.gz
Summary  : 'Check for uncleaned imports'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-CleanNamespaces-license = %{version}-%{release}
Requires: perl-Test-CleanNamespaces-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::pushd)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Builder)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::More)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::Tester)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(namespace::clean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Test-CleanNamespaces,
version 0.24:
Check for uncleaned imports

%package dev
Summary: dev components for the perl-Test-CleanNamespaces package.
Group: Development
Provides: perl-Test-CleanNamespaces-devel = %{version}-%{release}
Requires: perl-Test-CleanNamespaces = %{version}-%{release}

%description dev
dev components for the perl-Test-CleanNamespaces package.


%package license
Summary: license components for the perl-Test-CleanNamespaces package.
Group: Default

%description license
license components for the perl-Test-CleanNamespaces package.


%package perl
Summary: perl components for the perl-Test-CleanNamespaces package.
Group: Default
Requires: perl-Test-CleanNamespaces = %{version}-%{release}

%description perl
perl components for the perl-Test-CleanNamespaces package.


%prep
%setup -q -n Test-CleanNamespaces-0.24
cd %{_builddir}/Test-CleanNamespaces-0.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-CleanNamespaces
cp %{_builddir}/Test-CleanNamespaces-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-Test-CleanNamespaces/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::CleanNamespaces.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-CleanNamespaces/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
