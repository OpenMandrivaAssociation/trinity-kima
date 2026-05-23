%bcond clang 1
%bcond tdehwlib 1


# TDE variables
%define tde_pkg kima
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		14.1.6
Release:		1
Summary:		Kicker monitoring applet [Trinity]
Group:			Applications/Utilities
URL:			http://www.elliptique.net/~ken/kima/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/settings/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DPLUGIN_INSTALL_DIR=%{tde_prefix}/%{_lib}/trinity
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_NVCONTROL=OFF
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# UDEV support
%{?with_tdehwlib:BuildRequires:  pkgconfig(udev)}

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
This applet monitors various temperature,
frequency and fan sources in your kicker
panel.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_prefix}/%{_lib}/trinity/libkima.la
%{tde_prefix}/%{_lib}/trinity/libkima.so
%{tde_prefix}/share/apps/kicker/applets/kima.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kima/

