%define libname %mklibname wlembed
%define devname %mklibname -d wlembed
%define girname %mklibname wlembed-gir

%define git_id			4d37dc9da9a1f699b86d4e6b05f4619b8eee4ee8

Name:           libwlembed
Version:        0.0.0
Release:        1
Summary:        Library for Wayland embedded compositor
License:        GPL-3.0-only
URL:            https://gitlab.xfce.org/kelnos/libwlembed
Source0:        https://gitlab.xfce.org/kelnos/libwlembed/-/archive/%{git_id}/libwlembed.tar.gz#/%{name}-%{git_id}.tar.gz
#Source1:        https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/archive/%{wlr_protocols_git_id}/wlr-protocols.tar.gz#/wlr-protocols-%{wlr_protocols_git_id}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xfce4-dev-tools >= 4.19.2
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
libwlembed is a Wayland compositor library that allows you to embed
surfaces from one application into another by way of what's called an
"embedded compositor".

%package -n %{libname}
Summary:        Library for Wayland embedded compositor

%description -n %{libname}
libwlembed is a Wayland compositor library that allows you to embed
surfaces from one application into another by way of what's called an
"embedded compositor".

%package -n %{devname}
Summary:        Development files for libwlembed and libwlembed-gtk3
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
This package contains development files for libwlembed and libwlembed-gtk3.

%package -n %{girname}
Summary:        Introspection bindings for libwlembed
Requires:	%{libname} = %{EVRD}

%description -n %{girname}
This package provides the GObject Introspection bindings for libwlembed.


%prep
%autosetup -p1 -n %{name}-%{git_id}
#tar -C protocol/wlr-protocols --strip-components 1 -xf %{SOURCE1}

%build
%meson
%meson_build

%install
%meson_install

%files -n %{devname}
%doc README.md
%license LICENSE
%{_includedir}/libwlembed-0
%{_libdir}/libwlembed-0.so
%{_libdir}/libwlembed-gtk3-0.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

%files -n %{libname}
%{_libdir}/libwlembed-0.so.*
%{_libdir}/libwlembed-gtk3-0.so.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Libwlembed-0.0.typelib
%{_libdir}/girepository-1.0/Libxfce4libwlembed_gtk3-0.0.typelib
