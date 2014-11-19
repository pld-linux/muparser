Summary:	A fast math parser library
Summary(pl.UTF-8):	Biblioteka szybkiego analizatora matematycznego
Name:		muparser
Version:	2.2.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/muparser/%{name}_v2_2_3.zip
# Source0-md5:	9de40ec1dab5bd2787ee344fce5846ad
URL:		http://muparser.sourceforge.net/
BuildRequires:	dos2unix
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
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

%prep
%setup -q -n muparser_v2_2_3

%build
%configure \
	--disable-debug \
	--disable-samples \
	--enable-shared

%{__make} \
	CPPFLAGS="%{rpmcppflags}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes.txt License.txt
%attr(755,root,root) %{_libdir}/libmuparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmuparser.so.2

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%attr(755,root,root) %{_libdir}/libmuparser.so
%{_includedir}/muParser*.h
%{_pkgconfigdir}/muparser.pc
