Summary:     PostScript Utilities
Summary(pl): Narzêdzia do PostScriptu 
Name:        psutils
Version:     1.17
Release:     4
Copyright:   non-free
Group:       Utilities/Printing
Source:      ftp://ftp.dcs.ed.ac.uk/pub/ajcd/%{name}-p17.tar.gz
Patch0:      psutils-Makefile.patch
# Patch1 bases on:
# ftp://jurix.jura.uni-sb.de/pub/linux/source/networking/printing/psutils.dif
Patch1:      psutils-misc.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This archive contains some utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%description -l pl 
PSutils zawiera programy pomagaj±ce manipulowaæ plikami PostScript, wybieraæ
strony przeznacznone do wydruku, ich kolejno¶æ, uk³ad. Pozwala tak¿e na
³±czenie ró¿nych plików PostScript w ca³o¶æ.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
make -f Makefile.unix
 
%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile.unix DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README LICENSE
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/share/psutils

%changelog
* Mon Sep 07 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>  
  [1.17-4]
- added pl translation,
- more detailed %attr for binaries,
- moved some files from /usr/lib/psutils to /usr/share/psutils.

* Tue Jun 23 1998 Peter Soos <sp@osb.hu>
  [1.17-3]
- Using %attr for ability to rebuild the package as an ordinary user.

* Wed Jun 04 1997 Timo Karjalainen <timok@iki.fi>
  [1.17-2]
- Reverted back to un-gzipped man-pages (Redhat style)
- Added patch to compile everything cleanly
- Some minor changes to specfile

* Thu Mar 27 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17-1]
- new version:
  Patchlevel 17 had some minor bugfixes and improvements
  - Trailer information now put before %%EOF comments if no %%Trailer
  - psselect can now add blank pages.
  - Piped input works in Linux
  - spec file rewrited for using Buildroot,
  - man pages gziped.
