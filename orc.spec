%define api 0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libtest %mklibname %{name}-test %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	The Oil Runtime Compiler

Name:		orc
Version:	0.4.22
Release:	1
License:	BSD
Group:		Development/Other
Url:		http://code.entropywave.com/projects/orc/
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package -n %{libname}
Summary:	The Oil Runtime Compiler

Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{libtest}
Summary:	The Oil Runtime Compiler

Group:		System/Libraries
Conflicts:	%{_lib}orc0.4_0 <= 0.4.17-2

%description -n %{libtest}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	The Oil Runtime Compiler

Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libtest} = %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/orcc
%{_bindir}/orc-bugreport

%files -n %{libname}
%{_libdir}/liborc-%{api}.so.%{major}*

%files -n %{libtest}
%{_libdir}/liborc-test-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}-%{api}/
%{_libdir}/liborc*-%{api}.so
%{_libdir}/pkgconfig/orc-%{api}.pc
%{_datadir}/gtk-doc/html/orc
%{_datadir}/aclocal/orc.m4
