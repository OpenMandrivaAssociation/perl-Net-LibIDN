%define upstream_name	 Net-LibIDN
%define upstream_version 0.12

Summary: 	Perl bindings for GNU LibIDN
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release: 	1
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TH/THOR/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	idn-devel >= 0.4.0
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
Provides perl bindings for GNU Libidn, a C library for handling
Internationalized Domain Names according to IDNA (RFC 3490), in a way very
much inspired by Turbo Fredriksson's PHP-IDN.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor LIBS="-lidn"

make OPTIMIZE="%{optflags}"

# Change man page encoding into UTF-8
iconv -f latin1 -t utf-8 -o "blib/man3/Net::LibIDN.3pm.utf8" "blib/man3/Net::LibIDN.3pm"
mv -f "blib/man3/Net::LibIDN.3pm.utf8" "blib/man3/Net::LibIDN.3pm"

%install

%makeinstall_std

%check
%{__make} test

%files
%doc Artistic Changes README
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/man3/*.3pm*
