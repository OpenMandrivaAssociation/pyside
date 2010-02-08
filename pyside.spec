%define qtver 4.6

Name: pyside
Version: 0.2.3
Release: %mkrel 2
License: LGPLv2+
Summary: The PySide project provides LGPL-licensed Python bindings for the Qt
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  http://www.pyside.org/files/%name-qt%{qtver}+%{version}.tar.bz2
Patch0: pyside-qt4.5+0.2-cmake-install-module.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: phonon-devel
BuildRequires: boost-devel
BuildRequires: openssl-devel
BuildRequires: generatorrunner
BuildRequires: boostpythongenerator
BuildRequires: graphviz
%py_requires -d
Requires: pyside-phonon
Requires: pyside-core
Requires: pyside-gui
Requires: pyside-help
Requires: pyside-multimedia
Requires: pyside-network
Requires: pyside-opengl
Requires: pyside-script
Requires: pyside-scripttools
Requires: pyside-sql
Requires: pyside-xmlpatterns
Requires: pyside-xml
Requires: pyside-uitools
Requires: pyside-svg
Requires: pyside-webkit

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files
%doc README

#------------------------------------------------------------------------------

%package phonon
Summary: PySide phonon module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description phonon
PySide phonon module.

%files phonon
%defattr(-,root,root,-)
%py_platsitedir/PySide/phonon.so
%_datadir/PySide/typesystem/typesystem_phonon.*
%_datadir/PySide/typesystem/typesystem_maemo*
#------------------------------------------------------------------------------

%package core
Summary: PySide core module
Group: Development/KDE and Qt

%description core
PySide core module.

%files core
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtCore.so
%py_platsitedir/PySide/__init__.py
%_datadir/PySide/typesystem/typesystem_core*
%_datadir/PySide/typesystem/typesystem_templates.*

#------------------------------------------------------------------------------

%package gui
Summary: PySide gui module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description gui
PySide gui module.

%files gui
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtGui.so
%_datadir/PySide/typesystem/typesystem_gui*

#------------------------------------------------------------------------------

%package help
Summary: PySide help module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description help
PySide help module.

%files help
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtHelp.so
%_datadir/PySide/typesystem/typesystem_help.*

#------------------------------------------------------------------------------

%package multimedia
Summary: PySide multimedia module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtMultimedia.so
%_datadir/PySide/typesystem/typesystem_multimedia*

#------------------------------------------------------------------------------

%package network
Summary: PySide network module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description network
PySide network module.

%files network
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtNetwork.so
%_datadir/PySide/typesystem/typesystem_network.*

#------------------------------------------------------------------------------

%package opengl
Summary: PySide opengl module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtOpenGL.so
%_datadir/PySide/typesystem/typesystem_opengl*

#------------------------------------------------------------------------------

%package script
Summary: PySide script module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description script
PySide script module.

%files script
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtScript.so
%_datadir/PySide/typesystem/typesystem_script.*

#------------------------------------------------------------------------------

%package scripttools
Summary: PySide scripttool module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description scripttools
PySide scripttool module.

%files scripttools
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtScriptTools.so
%_datadir/PySide/typesystem/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package sql
Summary: PySide sql module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description sql
PySide sql module.

%files sql
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtSql.so
%_datadir/PySide/typesystem/typesystem_sql.*

#------------------------------------------------------------------------------

%package svg
Summary: PySide svg module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description svg
PySide svg module.

%files svg
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtSvg.so
%_datadir/PySide/typesystem/typesystem_svg.*

#------------------------------------------------------------------------------

%package uitools
Summary: PySide uitools module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtUiTools.so
%_datadir/PySide/typesystem/typesystem_uitools.*

#------------------------------------------------------------------------------

%package webkit
Summary: PySide webkit module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description webkit
PySide webkit module.

%files webkit
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtWebKit.so
%_datadir/PySide/typesystem/typesystem_webkit*

#------------------------------------------------------------------------------

%package xmlpatterns
Summary: PySide xmlpatterns module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description xmlpatterns
PySide xmlpatterns module.

%files xmlpatterns
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtXmlPatterns.so
%_datadir/PySide/typesystem/typesystem_xmlpatterns*

#------------------------------------------------------------------------------

%package xml
Summary: PySide xml module
Group: Development/KDE and Qt
Requires: pyside-core = %{version}

%description xml
PySide xml module.

%files xml
%defattr(-,root,root,-)
%py_platsitedir/PySide/QtXml.so
%_datadir/PySide/typesystem/typesystem_xml.*

#------------------------------------------------------------------------------

%define major 0
%define libname %mklibname pysidebase %{major}

%package -n %{libname}
Summary: PySide core library
Group: Development/KDE and Qt

%description -n %{libname}
PySide core library.

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libpysidebase.so.*

#------------------------------------------------------------------------------

%package devel
Summary: PySide devel files
Group: Development/KDE and Qt
Requires: %{name} = %{version}
Requires: %{libname} = %{version}

%description devel
PySide devel files.

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/Modules/*

#------------------------------------------------------------------------------


%prep
%setup -q -n %name-qt%{qtver}+%{version}
%patch0 -p0 -b .orig

%build
%cmake \
	-DQT_SRC_DIR=%buildroot/%qt4dir \
	-DQT_PHONON_INCLUDE_DIR=%_includedir/phonon
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

