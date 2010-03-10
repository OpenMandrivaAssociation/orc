%define name orc
%define version 0.4.3
%define release %mkrel 1

%define api 0.4
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Summary: The Oil Runtime Compiler
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
Patch0: orc-0.4.3-fix-linking.patch
License: BSD
Group: Development/Other
Url: http://code.entropywave.com/projects/orc/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package -n %libname
Summary: The Oil Runtime Compiler
Group: System/Libraries

%description -n %libname
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package -n %develname
Summary: The Oil Runtime Compiler
Group: Development/C
Requires: %libname = %version-%release
Requires: %name >= %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%prep
%setup -q
%apply_patches
autoreconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%_bindir/orcc
%_libexecdir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/liborc*-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_includedir/%name-%api/
%_libdir/liborc*-%api.a
%_libdir/liborc*-%api.la
%_libdir/liborc*-%api.so
%_libdir/pkgconfig/orc-%api.pc
%_datadir/gtk-doc/html/orc

