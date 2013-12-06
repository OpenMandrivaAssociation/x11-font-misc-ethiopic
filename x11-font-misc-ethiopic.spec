Name: x11-font-misc-ethiopic
Version: 1.0.3
Release: 9
Summary: Xorg X11 font misc-ethiopic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2
BuildRequires: fontconfig
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font misc-ethiopic

%prep
%setup -q -n font-misc-ethiopic-%{version}

%build
./configure --prefix=/usr \
            --x-includes=%{_includedir}\
            --x-libraries=%{_libdir} \
            --with-otf-fontdir=%_datadir/fonts/OTF \
	    --with-ttf-fontdir=%_datadir/fonts/TTF

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/OTF/fonts.dir
rm -f %{buildroot}%_datadir/fonts/OTF/fonts.scale
rm -f %{buildroot}%_datadir/fonts/TTF/fonts.dir
rm -f %{buildroot}%_datadir/fonts/TTF/fonts.scale

%post
mkfontscale %_datadir/fonts/OTF
mkfontdir %_datadir/fonts/OTF
mkfontscale %_datadir/fonts/TTF
mkfontdir %_datadir/fonts/TTF

%postun
mkfontscale %_datadir/fonts/OTF
mkfontdir %_datadir/fonts/OTF
mkfontscale %_datadir/fonts/TTF
mkfontdir %_datadir/fonts/TTF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/OTF/GohaTibebZemen.otf
%_datadir/fonts/TTF/GohaTibebZemen.ttf


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-4mdv2011.0
+ Revision: 675489
+ rebuild (emptylog)

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-3
+ Revision: 675254
- rebuild for new rpm-setup

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671212
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 618741
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 583210
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 490607
- New version: 1.0.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-8mdv2009.1
+ Revision: 351285
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2009.0
+ Revision: 225997
- rebuild
- fix no-buildroot-tag

* Thu Dec 20 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-6mdv2008.1
+ Revision: 136047
- correct license

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2008.1
+ Revision: 129746
- kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild prep


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:54:51 (51489)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

