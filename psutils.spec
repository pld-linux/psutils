Summary:	PostScript Utilities
Summary(pl):	Narzêdzia do PostScriptu 
Name:		psutils
Version:	1.17
Release:	6
Copyright:	non-free
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
Source0:	ftp://ftp.dcs.ed.ac.uk/pub/ajcd/%{name}-p17.tar.gz
Patch0:		psutils-Makefile.patch
# Patch1 bases on:	
# ftp:		//jurix.jura.uni-sb.de/pub/linux/source/networking/printing/psutils.dif
Patch1:		psutils-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This archive contains some utilities for manipulating PostScript
documents. Page selection and rearrangement are supported, including
arrangement into signatures for booklet printing, and page merging for
n-up printing.

%description -l pl 
PSutils zawiera programy pomagaj±ce manipulowaæ plikami PostScript,
wybieraæ strony przeznacznone do wydruku, ich kolejno¶æ, uk³ad.
Pozwala tak¿e na ³±czenie ró¿nych plików PostScript w ca³o¶æ.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
make -f Makefile.unix
 
%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile.unix \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,LICENSE}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
