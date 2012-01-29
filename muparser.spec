Summary:	A fast math parser library
Summary(pl.UTF-8):	Biblioteka szybkiego analizatora matematycznego
Name:		muparser
Version:	1.30
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/muparser/%{name}_v130.tar.gz
# Source0-md5:	f6b4d79aa0f762fd4bfeb38f47cf1d15
URL:		http://muparser.sourceforge.net/
BuildRequires:	dos2unix
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

%description devel
Development and doc files for muParser library.

%description devel -l pl.UTF-8
Pliki programistyczne i dokumentacja do biblioteki muParser.

%prep
%setup -q -n muparser

%build
%configure \
	--enable-shared=yes \
	--enable-debug=no \
	--enable-samples=no \

%{__make} \
	CXXFLAGS="%{rpmcflags}"
mv docs/html .
dos2unix *.txt
dos2unix html/sources/*
dos2unix html/script/*

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes.txt Credits.txt License.txt
%attr(755,root,root) %{_libdir}/libmuparser.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libmuparser.so.0

%files devel
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_libdir}/libmuparser.so
%{_includedir}/*
%{_pkgconfigdir}/muparser.pc
