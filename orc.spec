%define api 0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %{name}

Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.16
Release:	2
Source0:	http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
License:	BSD
Group:		Development/Other
Url:		http://code.entropywave.com/projects/orc/

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
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package -n %{develname}
Summary:	The Oil Runtime Compiler
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.  The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README TODO
%{_bindir}/orcc
%{_bindir}/orc-bugreport

%files -n %{libname}
%{_libdir}/liborc*-%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}-%{api}/
%{_libdir}/liborc*-%{api}.a
%{_libdir}/liborc*-%{api}.so
%{_libdir}/pkgconfig/orc-%{api}.pc
%{_datadir}/gtk-doc/html/orc
%{_datadir}/aclocal/orc.m4


%changelog
* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 0.4.16-1mdv2012.0
+ Revision: 731113
- new version
- update file list

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.4.14-1
+ Revision: 685502
- update to new version 0.4.14

* Wed Apr 20 2011 Götz Waschk <waschk@mandriva.org> 0.4.13-1
+ Revision: 656111
- update to new version 0.4.13

* Sun Apr 17 2011 Götz Waschk <waschk@mandriva.org> 0.4.12-1
+ Revision: 654289
- update to new version 0.4.12

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 0.4.11-1mdv2011.0
+ Revision: 591448
- update to new version 0.4.11

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 0.4.10-1mdv2011.0
+ Revision: 586586
- new version
- update file list

* Tue Sep 07 2010 Götz Waschk <waschk@mandriva.org> 0.4.9-1mdv2011.0
+ Revision: 576476
- update to new version 0.4.9

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 0.4.8-1mdv2011.0
+ Revision: 575667
- update to new version 0.4.8

* Sat Aug 21 2010 Götz Waschk <waschk@mandriva.org> 0.4.7-1mdv2011.0
+ Revision: 571687
- update to new version 0.4.7

* Wed Jul 14 2010 Götz Waschk <waschk@mandriva.org> 0.4.6-1mdv2011.0
+ Revision: 553395
- new version
- add orc-bugreport tool

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.4.5-1mdv2011.0
+ Revision: 550278
- update to new version 0.4.5

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.4.4-2mdv2010.1
+ Revision: 540039
- rebuild so that shared libraries are properly stripped again

* Fri Apr 23 2010 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 538139
- new version
- drop patch

* Wed Mar 10 2010 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 517309
- import orc


