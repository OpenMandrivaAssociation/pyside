%define qtver 4.8
%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py2verflags -python2.7

Summary:	The PySide project provides LGPL-licensed Python bindings for the Qt
Name:		pyside
Version:	1.2.2
Release:	8
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		http://www.pyside.org
Source0:	http://ftp.fau.de/qtproject/official_releases/pyside/pyside-qt4.8+%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(shiboken)
BuildRequires:  python-setuptools 
BuildRequires:  python2-setuptools
BuildRequires:	python-sphinx
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
%{py_platsitedir}/PySide/_utils.py
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

%define api 1.2
%define libname %mklibname pyside.%{py3verflags} %{api}

%package -n %{libname}
Summary:	PySide core library
Group:		Development/KDE and Qt
Obsoletes:	%{_lib}pyside1 < 1.1.2-2

%description -n %{libname}
PySide core library.

%files -n %{libname}
%{_libdir}/libpyside.%{py3verflags}.so.%{api}*

#------------------------------------------------------------------------------

%define api 1.2
%define libname_py2 %mklibname pyside%{py2verflags} %{api}

%package -n %{libname_py2}
Summary:        PySide core library
Group:          Development/KDE and Qt

%description -n %{libname_py2}
PySide core library.

%files -n %{libname_py2}
%{_libdir}/libpyside%{py2verflags}.so.%{api}*

#------------------------------------------------------------------------------

%package -n python2-pyside
Requires:       python2-pyside-phonon
Requires:       python2-pyside-core
Requires:       python2-pyside-declarative
Requires:       python2-pyside-gui
Requires:       python2-pyside-help
Requires:       python2-pyside-multimedia
Requires:       python2-pyside-network
Requires:       python2-pyside-opengl
Requires:       python2-pyside-script
Requires:       python2-pyside-scripttools
Requires:       python2-pyside-sql
Requires:       python2-pyside-test
Requires:       python2-pyside-xmlpatterns
Requires:       python2-pyside-xml
Requires:       python2-pyside-uitools
Requires:       python2-pyside-svg
Requires:       python2-pyside-webkit

%description -n python2-pyside
Pyside for python2.

%files -n python2-pyside

#------------------------------------------------------------------------------

%package -n python2-pyside-phonon
Summary:	PySide phonon module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-phonon
PySide phonon module.

%files -n python2-pyside-phonon
%{py2_platsitedir}/PySide/phonon.so

#------------------------------------------------------------------------------

%package -n python2-pyside-core
Summary:	PySide core module
Group:		Development/KDE and Qt

%description -n python2-pyside-core
PySide core module.

%files -n python2-pyside-core
%{py2_platsitedir}/PySide/QtCore.so
%{py2_platsitedir}/PySide/__init__.py
%{py2_platsitedir}/PySide/_utils.py

#------------------------------------------------------------------------------

%package -n python2-pyside-declarative
Summary:	PySide declarative module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-declarative
PySide declarative module.

%files -n python2-pyside-declarative
%{py2_platsitedir}/PySide/QtDeclarative.so

#------------------------------------------------------------------------------

%package -n python2-pyside-gui
Summary:	PySide gui module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-gui
PySide gui module.

%files -n python2-pyside-gui
%{py2_platsitedir}/PySide/QtGui.so
#------------------------------------------------------------------------------

%package -n python2-pyside-help
Summary:	PySide help module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-help
PySide help module.

%files -n python2-pyside-help
%{py2_platsitedir}/PySide/QtHelp.so

#------------------------------------------------------------------------------

%package -n python2-pyside-multimedia
Summary:	PySide multimedia module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-multimedia
PySide multimedia module.

%files -n python2-pyside-multimedia
%{py2_platsitedir}/PySide/QtMultimedia.so

#------------------------------------------------------------------------------

%package -n python2-pyside-network
Summary:	PySide network module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-network
PySide network module.

%files -n python2-pyside-network
%{py2_platsitedir}/PySide/QtNetwork.so

#------------------------------------------------------------------------------

%package -n python2-pyside-opengl
Summary:	PySide opengl module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-opengl
PySide opengl module.

%files -n python2-pyside-opengl
%{py2_platsitedir}/PySide/QtOpenGL.so

#------------------------------------------------------------------------------

%package -n python2-pyside-script
Summary:	PySide script module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-script
PySide script module.

%files -n python2-pyside-script
%{py2_platsitedir}/PySide/QtScript.so

#------------------------------------------------------------------------------

%package -n python2-pyside-scripttools
Summary:	PySide scripttool module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-scripttools
PySide scripttool module.

%files -n python2-pyside-scripttools
%{py2_platsitedir}/PySide/QtScriptTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside-sql
Summary:	PySide sql module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-sql
PySide sql module.

%files -n python2-pyside-sql
%{py2_platsitedir}/PySide/QtSql.so

#------------------------------------------------------------------------------

%package -n python2-pyside-svg
Summary:	PySide svg module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-svg
PySide svg module.

%files -n python2-pyside-svg
%{py2_platsitedir}/PySide/QtSvg.so

#------------------------------------------------------------------------------

%package -n python2-pyside-test
Summary:	PySide test module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-test
PySide test module.

%files -n python2-pyside-test
%{py2_platsitedir}/PySide/QtTest.so

#------------------------------------------------------------------------------

%package -n python2-pyside-uitools
Summary:	PySide uitools module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-uitools
PySide uitools module.

%files -n python2-pyside-uitools
%{py2_platsitedir}/PySide/QtUiTools.so

#------------------------------------------------------------------------------

%package -n python2-pyside-webkit
Summary:	PySide webkit module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-webkit
PySide webkit module.

%files -n python2-pyside-webkit
%{py2_platsitedir}/PySide/QtWebKit.so

#------------------------------------------------------------------------------

%package -n python2-pyside-xmlpatterns
Summary:	PySide xmlpatterns module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-xmlpatterns
PySide xmlpatterns module.

%files -n python2-pyside-xmlpatterns
%{py2_platsitedir}/PySide/QtXmlPatterns.so

#------------------------------------------------------------------------------

%package -n python2-pyside-xml
Summary:	PySide xml module
Group:		Development/KDE and Qt
Requires:	pyside-core = %{version}

%description -n python2-pyside-xml
PySide xml module.

#------------------------------------------------------------------------------

%package devel
Summary:        PySide devel files
Group:          Development/KDE and Qt
Requires:       %{name} = %{version}-%{release}
Requires:       python2-%{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libname_py2} = %{version}-%{release}

%description devel
PySide devel files.

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

#------------------------------------------------------------------------------


%files -n python2-pyside-xml
%{py2_platsitedir}/PySide/QtXml.so

#------------------------------------------------------------------------------


%prep
%setup -qn %{name}-qt%{qtver}+%{version}

%__sed 's/-Wno-strict-aliasing/-fno-strict-aliasing/' -i CMakeLists.txt

cp -a . %py2dir

%build

%define Werror_cflags %nil
pushd %{py2dir}
%cmake \
	-DQT_QMAKE_EXECUTABLE=/usr/lib/qt4/bin/qmake \
        -DQT_SRC_DIR=%{buildroot}%{qt4dir} \
        -DQT_PHONON_INCLUDE_DIR=%{_includedir}/phonon \
        -DPYTHON_EXECUTABLE=%{__python2} \
	-DPYTHON_SUFFIX="-python2.7"
%make
popd
%cmake \
	-DQT_QMAKE_EXECUTABLE=/usr/lib/qt4/bin/qmake \
	-DQT_SRC_DIR=%{buildroot}%{qt4dir} \
	-DQT_PHONON_INCLUDE_DIR=%{_includedir}/phonon \
	-DPYTHON_SUFFIX=.%{py3verflags} \
	-DSHIBOKEN_PYTHON_INTERPRETER=%{__python3}
%make

%install
pushd %{py2dir}
%makeinstall_std -C build
popd

%makeinstall_std -C build

