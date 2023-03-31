Name: x11-font-misc-ethiopic
Version: 1.0.5
Release: 2
Summary: Xorg X11 font misc-ethiopic
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.xz
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font misc-ethiopic.

%prep
%autosetup -n font-misc-ethiopic-%{version} -p1

%build
%configure \
	--with-ttf-fontdir=%{_datadir}/fonts/TTF \
	--with-otf-fontdir=%{_datadir}/fonts/OTF   

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/OTF/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/OTF/fonts.scale
rm -f %{buildroot}%{_datadir}/fonts/TTF/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/TTF/fonts.scale

%post
mkfontscale %{_datadir}/fonts/OTF
mkfontdir %{_datadir}/fonts/OTF
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%postun
mkfontscale %{_datadir}/fonts/OTF
mkfontdir %{_datadir}/fonts/OTF
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%files
%doc COPYING
%{_datadir}/fonts/OTF/GohaTibebZemen.otf
%{_datadir}/fonts/TTF/GohaTibebZemen.ttf
