Summary:	PostScript Utilities
Summary(pl):	Narzêdzia do PostScriptu
Name:		psutils
Version:	1.17
Release:	15
License:	distributable
Group:		Applications/Printing
Source0:	ftp://ftp.dcs.ed.ac.uk/pub/ajcd/%{name}-p17.tar.gz
# Source0-md5: b161522f3bd1507655326afa7db4a0ad
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5: 1e7a4663e9b535e102e6242ec1d5c875
Patch0:		%{name}-Makefile.patch
# Patch1 derived from ftp://jurix.jura.uni-sb.de/pub/linux/source/networking/printing/psutils.dif
Patch1:		%{name}-misc.patch
Patch2:		%{name}-paper.patch
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
%patch2 -p1

%build
%{__make} -f Makefile.unix OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -f Makefile.unix install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_datadir}/%{name}
