Summary:	POSIX functions for Lua
Summary(pl):	Funkcje POSIX dla Lua
Name:		lua-poslib
Version:	1.4
Release:	2
License:	BSD-like
Group:		Development/Languages
Source0:	ftp://ftp.lua.org/poslib.tar.gz
URL:		http://www.soho-one.com/software/poslib/
BuildRequires:	lua40-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POSIX bindings for Lua language implemented as dynamic library in C.

%description -l pl
Funkcje ze standardu POSIX dla jêzyka Lua zaimplementowane jako
dynamiczna biblioteka w C.

%prep
%setup  -q -n poslib

%build

%{__cc} -o poslib.so $RPM_OPT_FLAGS -shared -fPIC -DPIC lposlib.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_libdir}/lua
install poslib.so $RPM_BUILD_ROOT/%{_libdir}/lua

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt *.lua
%attr(755,root,root)		%{_libdir}/lua/*.so
