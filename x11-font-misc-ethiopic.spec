Name: x11-font-misc-ethiopic
Version: 1.0.0
Release: %mkrel 7
Summary: Xorg X11 font misc-ethiopic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} \
      --with-otf-fontdir=%_datadir/fonts/OTF --with-ttf-fontdir=%_datadir/fonts/TTF

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
