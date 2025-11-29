%define git_id			4d37dc9da9a1f699b86d4e6b05f4619b8eee4ee8
%define wlr_protocols_git_id	a5028afbe4a1cf0daf020c4104c1565a09d6e58a

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

%package -n %{name}-0-0
Summary:        Library for Wayland embedded compositor

%description -n %{name}-0-0
libwlembed is a Wayland compositor library that allows you to embed
surfaces from one application into another by way of what's called an
"embedded compositor".

%package -n %{name}-gtk3-0-0
Summary:        Library for Wayland embedded compositor

%description -n %{name}-gtk3-0-0
libwlembed is a Wayland compositor library that allows you to embed
surfaces from one application into another by way of what's called an
"embedded compositor".

%package devel
Summary:        Development files for libwlembed and libwlembed-gtk3
Requires:       %{name}-0-0 = %{version}
Requires:       %{name}-gtk3-0-0 = %{version}

%description devel
This package contains development files for libwlembed and libwlembed-gtk3.

%package -n typelib-1_0-Libwlembed-0
Summary:        Introspection bindings for libwlembed

%description -n typelib-1_0-Libwlembed-0
This package provides the GObject Introspection bindings for libwlembed.

%package -n typelib-1_0-Libxfce4libwlembed_gtk3-0
Summary:        Introspection bindings for libwlembed-gtk3

%description -n typelib-1_0-Libxfce4libwlembed_gtk3-0
This package provides the GObject Introspection bindings for libwlembed-gtk3.

%prep
%autosetup -p1 -n %{name}-%{git_id}
#tar -C protocol/wlr-protocols --strip-components 1 -xf %{SOURCE1}

%build
%meson
%meson_build

%install
%meson_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/libwlembed-0
%{_libdir}/libwlembed-0.so
%{_libdir}/libwlembed-gtk3-0.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

%files -n libwlembed-0-0
%{_libdir}/libwlembed-0.so.*

%files -n libwlembed-gtk3-0-0
%{_libdir}/libwlembed-gtk3-0.so.*

%files -n typelib-1_0-Libwlembed-0
%{_libdir}/girepository-1.0/Libwlembed-0.0.typelib

%files -n typelib-1_0-Libxfce4libwlembed_gtk3-0
%{_libdir}/girepository-1.0/Libxfce4libwlembed_gtk3-0.0.typelib
