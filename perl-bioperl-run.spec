%define module	bioperl-run
%define name	perl-%{module}
%define version 1.6.1
%define release %mkrel 2

%define _requires_exceptions perl(Bio::Root::AccessorMaker)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	BioPerl wrappers for external programs
Group:		Development/Perl
License:	Artistic
Source:		http://bioperl.org/DIST/%{module}-%{version}.tar.bz2
URL:		http://www.bioperl.org
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildRequires:	perl-bioperl >= 1.6

Obsoletes:	perl-Bioperl-Run
Provides:	perl-Bioperl-Run
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Officially organized in 1995 and existing informally for several years
prior, The Bioperl Project is an international association of developers
of open source Perl tools for bioinformatics, genomics and life science
research.

%prep
%setup -q -n BioPerl-run-1.6.0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOI
n
a
n
EOI
%make

%check
# most of the check useanon-packaged  external tools, so they are useless there

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
#%{__rm} -f %{buildroot}%{perl_vendorlib}/bptutorial.pl
#%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes INSTALL.PROGRAMS LICENSE README
%{perl_vendorlib}/Bio
%{_bindir}/*
%{_mandir}/man?/*
