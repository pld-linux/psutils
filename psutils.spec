Summary:	PostScript Utilities
Summary(pl):	Narz�dzia do PostScriptu 
Name:		psutils
Version:	1.17
Release:	16
License:	distributable
Group:		Applications/Printing
Group(cs):	Aplikace/Tisk
Group(da):	Programmer/Udskrift
Group(de):	Applikationen/Drucken
Group(es):	Aplicaciones/Impresi�n
Group(fr):	Applications/Impression
Group(is):	Forrit/�r�a�
Group(it):	Applicazioni/Stampa
Group(no):	Applikasjoner/Utskrift
Group(pl):	Aplikacje/Drukowanie
Group(pt):	Aplica��es/Impress�o
Group(ru):	����������/������
Group(sl):	Programi/Tiskanje
Group(sv):	Till�mpningar/Utskrift
Source0:	ftp://ftp.dcs.ed.ac.uk/pub/ajcd/%{name}-p17.tar.gz
# Source0-md5:	b161522f3bd1507655326afa7db4a0ad
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	1e7a4663e9b535e102e6242ec1d5c875
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
PSutils zawiera programy pomagaj�ce manipulowa� plikami PostScript,
wybiera� strony przeznacznone do wydruku, ich kolejno��, uk�ad.
Pozwala tak�e na ��czenie r�nych plik�w PostScript w ca�o��.

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

gzip -9nf README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_datadir}/%{name}
