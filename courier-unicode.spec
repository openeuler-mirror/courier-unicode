Summary:             A library implementing algorithms related to the Unicode Standard
Name:                courier-unicode
Version:             2.0
Release:             1
License:             GPLv3
URL:                 https://sourceforge.net/projects/courier/files/courier-unicode
Source0:             https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:             https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:             pubkey.maildrop
BuildRequires:       gcc-c++ gcc gnupg perl-interpreter
%description
This library implements several algorithms related to the Unicode Standard:
* Look up uppercase, lowercase, and titlecase equivalents of a unicode character.
* Implementation of grapheme and work breaking rules.
* Implementation of line breaking rules.
Several ancillary functions, like looking up the unicode character that
corresponds to some HTML 4.0 entity (such as “&amp;”, for example), and
determining the normal width or a double-width status of a unicode character.
Also, an adaptation of the iconv(3) API for this unicode library.
This library also implements C++ bindings for these algorithms.
The current release of the Courier Unicode library is based on the Unicode 8.0.0 standard.

%package devel
Summary:             Development tools for programs which will use the libcourier-unicode library
Requires:            %{name}%{?_isa} = %{version}-%{release}
%description devel
The courier-unicode-devel package includes the header files and documentation
necessary for developing programs which will use the libcourier-unicode library.

%prep
%setup -q
gpg --import %{SOURCE2}
gpg --verify %{SOURCE1} %{SOURCE0}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%makeinstall
rm %{buildroot}%{_libdir}/*.la

%check
%{__make} check

%files
%license COPYING
%doc README ChangeLog AUTHORS
%{_libdir}/libcourier-unicode.so.4
%{_libdir}/libcourier-unicode.so.4.0.0

%files devel
%{_includedir}/courier-unicode.h
%{_includedir}/courier-unicode-categories-tab.h
%{_includedir}/courier-unicode-script-tab.h
%{_libdir}/libcourier-unicode.so
%{_datadir}/aclocal/courier-unicode.m4
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
* Wed Oct 14 2020 chengzihan <chengzihan2@huawei.com> - 2.0-1
- Package init
