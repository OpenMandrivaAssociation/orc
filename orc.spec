# orc is used by pulseaudio, pulseaudio is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define api 0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libtest %mklibname %{name}-test %{api} %{major}
%define devname %mklibname -d %{name}
%define devstatic %mklibname -d -s %{name}
%define lib32name %mklib32name %{name} %{api} %{major}
%define lib32test %mklib32name %{name}-test %{api} %{major}
%define dev32name %mklib32name -d %{name}
%define dev32static %mklib32name -d -s %{name}

Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.31
Release:	2
License:	BSD
Group:		Development/Other
Url:		http://code.entropywave.com/projects/orc/
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
BuildRequires:	meson

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

%package -n %{devstatic}
Summary:	The Oil Runtime Compiler
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{devstatic}
This package includes the development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	The Oil Runtime Compiler (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains a shared library for %{name}.

%package -n %{lib32test}
Summary:	The Oil Runtime Compiler (32-bit)
Group:		System/Libraries

%description -n %{lib32test}
This package contains a shared library for %{name}.

%package -n %{dev32name}
Summary:	The Oil Runtime Compiler
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{lib32test} = %{version}-%{release}

%description -n %{dev32name}
This package includes the development files for %{name}.

%package -n %{dev32static}
Summary:	The Oil Runtime Compiler
Group:		Development/C
Requires:	%{dev32name} = %{version}-%{release}

%description -n %{dev32static}
This package includes the development files for %{name}.
%endif

%prep
%autosetup -p1

%if %{with compat32}
export LDFLAGS="%(echo %{ldflags} |sed -e 's,-m64,,g;s,-mx32,,g') -m32"
%meson32 -Dgtk_doc=disabled
%endif

export LDFLAGS="%{ldflags}"
%meson -Dgtk_doc=disabled

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install

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
%{_libdir}/pkgconfig/orc-test-%{api}.pc
%{_datadir}/aclocal/orc.m4

%files -n %{devstatic}
%{_libdir}/liborc*-%{api}.a

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/liborc-%{api}.so.%{major}*

%files -n %{lib32test}
%{_prefix}/lib/liborc-test-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/liborc*-%{api}.so
%{_prefix}/lib/pkgconfig/orc-%{api}.pc
%{_prefix}/lib/pkgconfig/orc-test-%{api}.pc

%files -n %{dev32static}
%{_prefix}/lib/liborc*-%{api}.a
%endif
