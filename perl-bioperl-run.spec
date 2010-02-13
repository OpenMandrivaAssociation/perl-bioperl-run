%define upstream_name	 bioperl-run
%define upstream_version 1.6.1

%define _requires_exceptions perl(Bio::Root::AccessorMaker)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	BioPerl wrappers for external programs
License:	Artistic
Group:		Development/Perl
Url:		http://www.bioperl.org
Source0:	http://bioperl.org/DIST/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildRequires:	perl-bioperl >= 1.6.0

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:	perl-Bioperl-Run
Provides:	perl-Bioperl-Run

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
%{_mandir}/man?/*
