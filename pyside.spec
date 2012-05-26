%define qtver 4.8
%define pyver python2.7

Name:		pyside
Version:	1.1.1
Release:	1
License:	LGPLv2+
Summary:	The PySide project provides LGPL-licensed Python bindings for the Qt
Group:		Development/KDE and Qt
URL:		http://www.pyside.org
Source0:	http://www.pyside.org/files/%{name}-qt%{qtver}+%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	phonon-devel
BuildRequires:	shiboken-devel >= 1.1.1
Buildrequires:	python-devel
Requires:	pyside-phonon
Requires:	pyside-core
Requires:	pyside-declarative
Requires:	pyside-gui
Requires:	pyside-help
Requires:	pyside-multimedia
Requires:	pyside-network
Requires:	pyside-opengl
Requires:	pyside-script
Requires:	pyside-scripttools
Requires:	pyside-sql
Requires:	pyside-test
Requires:	pyside-xmlpatterns
Requires:	pyside-xml
Requires:	pyside-uitools
Requires:	pyside-svg
Requires:	pyside-webkit

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files

#------------------------------------------------------------------------------

%package phonon
Summary:	PySide phonon module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description phonon
PySide phonon module.

%files phonon
%{py_platsitedir}/PySide/phonon.so
%{_datadir}/PySide/typesystems/typesystem_phonon.*

#------------------------------------------------------------------------------

%package core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description core
PySide core module.

%files core
%{py_platsitedir}/PySide/QtCore.so
%{py_platsitedir}/PySide/__init__.py
%{_datadir}/PySide/typesystems/typesystem_core*
%{_datadir}/PySide/typesystems/typesystem_templates.*

#------------------------------------------------------------------------------

%package declarative
Summary:	PySide declarative module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description declarative
PySide declarative module.

%files declarative
%{py_platsitedir}/PySide/QtDeclarative.so
%{_datadir}/PySide/typesystems/typesystem_declarative.*

#------------------------------------------------------------------------------

%package gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description gui
PySide gui module.

%files gui
%{py_platsitedir}/PySide/QtGui.so
%{_datadir}/PySide/typesystems/typesystem_gui*

#------------------------------------------------------------------------------

%package help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description help
PySide help module.

%files help
%{py_platsitedir}/PySide/QtHelp.so
%{_datadir}/PySide/typesystems/typesystem_help.*

#------------------------------------------------------------------------------

%package multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description multimedia
PySide multimedia module.

%files multimedia
%{py_platsitedir}/PySide/QtMultimedia.so
%{_datadir}/PySide/typesystems/typesystem_multimedia*

#------------------------------------------------------------------------------

%package network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description network
PySide network module.

%files network
%{py_platsitedir}/PySide/QtNetwork.so
%{_datadir}/PySide/typesystems/typesystem_network.*

#------------------------------------------------------------------------------

%package opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description opengl
PySide opengl module.

%files opengl
%{py_platsitedir}/PySide/QtOpenGL.so
%{_datadir}/PySide/typesystems/typesystem_opengl*

#------------------------------------------------------------------------------

%package script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description script
PySide script module.

%files script
%{py_platsitedir}/PySide/QtScript.so
%{_datadir}/PySide/typesystems/typesystem_script.*

#------------------------------------------------------------------------------

%package scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description scripttools
PySide scripttool module.

%files scripttools
%{py_platsitedir}/PySide/QtScriptTools.so
%{_datadir}/PySide/typesystems/typesystem_scripttools.*

#------------------------------------------------------------------------------

%package sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description sql
PySide sql module.

%files sql
%{py_platsitedir}/PySide/QtSql.so
%{_datadir}/PySide/typesystems/typesystem_sql.*

#------------------------------------------------------------------------------

%package svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description svg
PySide svg module.

%files svg
%{py_platsitedir}/PySide/QtSvg.so
%{_datadir}/PySide/typesystems/typesystem_svg.*

#------------------------------------------------------------------------------

%package test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description test
PySide test module.

%files test
%{py_platsitedir}/PySide/QtTest.so
%{_datadir}/PySide/typesystems/typesystem_test.*

#------------------------------------------------------------------------------

%package uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description uitools
PySide uitools module.

%files uitools
%{py_platsitedir}/PySide/QtUiTools.so
%{_datadir}/PySide/typesystems/typesystem_uitools.*

#------------------------------------------------------------------------------

%package webkit
Summary:	PySide webkit module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description webkit
PySide webkit module.

%files webkit
%{py_platsitedir}/PySide/QtWebKit.so
%{_datadir}/PySide/typesystems/typesystem_webkit*

#------------------------------------------------------------------------------

%package xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description xmlpatterns
PySide xmlpatterns module.

%files xmlpatterns
%{py_platsitedir}/PySide/QtXmlPatterns.so
%{_datadir}/PySide/typesystems/typesystem_xmlpatterns*

#------------------------------------------------------------------------------

%package xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description xml
PySide xml module.

%files xml
%{py_platsitedir}/PySide/QtXml.so
%{_datadir}/PySide/typesystems/typesystem_xml.*

#------------------------------------------------------------------------------

%define major 1
%define libname %mklibname pyside %{major}

%package -n %{libname}
Summary:	PySide core library
Group:		Development/KDE and Qt
Obsoletes:	%{_lib}pysidebase0 < 0.4.0

%description -n %{libname}
PySide core library.

%files -n %{libname}
%{_libdir}/libpyside-python%{py_ver}.so.%{major}*

#------------------------------------------------------------------------------

%package devel
Summary:	PySide devel files
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}

%description devel
PySide devel files.

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

#------------------------------------------------------------------------------

%prep
%setup -qn %{name}-qt%{qtver}+%{version}

%build
%define Werror_cflags %nil
%__sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt
%cmake \
	-DQT_SRC_DIR=%{buildroot}%{qt4dir} \
	-DQT_PHONON_INCLUDE_DIR=%{_includedir}/phonon \
	-DPYTHON_BASENAME=%{pyver}
%make

%install
%makeinstall_std -C build

