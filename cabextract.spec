Summary: A program to extract Microsoft Cabinet files
Name: cabextract
Version: 1.11
Release: 1
License: GPL
Group: Applications/Archiving
Source: https://www.cabextract.org.uk/%{name}-%{version}.tar.gz
URL: https://www.cabextract.org.uk/
Vendor: Stuart Caie
Packager: Stuart Caie <kyzer@cabextract.org.uk>
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: /usr

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program unpacks these files.

%prep
%setup

%build
CFLAGS=${RPM_OPT_FLAGS} ./configure --prefix=%{prefix}
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%attr(0755, root, root) %{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*
