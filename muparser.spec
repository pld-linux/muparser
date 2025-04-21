#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	openmp	# OpenMP support
#
Summary:	A fast math parser library
Summary(pl.UTF-8):	Biblioteka szybkiego analizatora matematycznego
Name:		muparser
Version:	2.3.5
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/beltoforion/muparser/releases
Source0:	https://github.com/beltoforion/muparser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	04d4224cb01712207b85af05a255b6fc
URL:		https://github.com/beltoforion/muparser
BuildRequires:	cmake >= 3.15.0
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Many applications require the parsing of mathematical expressions. The
main objective of this project is to provide a fast and easy way of
doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode and
precalculating constant parts of it.

%description -l pl.UTF-8
Wiele aplikacji wymaga analizowania wyrażeń matematycznych. Głównym
celem tego projektu jest zapewnienie szybkiego i wygodnego sposobu
wykonywania tego zadania. muParser to bardzo wydajna, rozszerzalna
biblioteka analizatora matematycznego. Opiera się na przekształcaniu
wyrażenia na bajtkod oraz wstępnym obliczaniu jego stałych części.

%package devel
Summary:	Development and doc files for muParser library
Summary(pl.UTF-8):	Pliki programistyczne i dokumentacja do biblioteki muParser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Development and doc files for muParser library.

%description devel -l pl.UTF-8
Pliki programistyczne i dokumentacja do biblioteki muParser.

%package apidocs
Summary:	API documentation for muParser library
Summary(pl.UTF-8):	Dokumentacja API biblioteki muParser
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for muParser library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki muParser.

%prep
%setup -q

# html/misc/footer.html not present (even in git)
%{__sed} -i -e '/^HTML_FOOTER .*/s/.*/HTML_FOOTER = /' docs/Doxyfile

%build
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	%{!?with_openmp:-DENABLE_OPENMP=OFF} \
	-DENABLE_SAMPLES=OFF

%{__make} -C build

%if %{with apidocs}
cd docs
doxygen
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md docs/muparser_doc.html
%attr(755,root,root) %{_libdir}/libmuparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmuparser.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmuparser.so
%{_includedir}/muParser*.h
%{_pkgconfigdir}/muparser.pc
%{_libdir}/cmake/muparser

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/classdocu/{d?,search,*.css,*.html,*.jpg,*.js,*.png}
%endif
