Summary:	POSIX functions for Lua
Summary(pl):	Funkcje POSIX dla Lua
Name:		lua-poslib
Version:	1.4
Release:	1
License:	BSD-like
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source:		ftp://ftp.lua.org/poslib.tar.gz
URL:		http://www.soho-one.com/software/poslib/
BuildRequires:	lua-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup  -q -n poslib

%build

%{__cc} -o poslib.so $RPM_OPT_FLAGS -shared -fPIC -DPIC lposlib.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_libdir}/lua
install poslib.so $RPM_BUILD_ROOT/%{_libdir}/lua

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt.gz *.lua
%attr(755,root,root)		%{_libdir}/lua/*.so
