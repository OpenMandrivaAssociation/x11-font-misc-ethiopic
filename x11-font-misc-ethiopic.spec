Name: x11-font-misc-ethiopic
Version: 1.0.3
Release: 12
Summary: Xorg X11 font misc-ethiopic
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.bz2
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
%configure \
	--with-ttf-fontdir=%_datadir/fonts/TTF \
	--with-otf-fontdir=%_datadir/fonts/OTF   

%make

%install
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

%files
%doc COPYING
%_datadir/fonts/OTF/GohaTibebZemen.otf
%_datadir/fonts/TTF/GohaTibebZemen.ttf
