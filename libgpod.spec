Summary:	Shared library to access the contents of an iPod
Summary(pl):	Biblioteka wsp�dzielona do dost�pu do zawarto�ci iPod�w
Name:		libgpod
Version:	0.2.0
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	9ea91a96805d7e5803397bdd18aa6a80
Patch0:		%{name}-align.patch
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	hal-devel >= 0.5.2
BuildRequires:	intltool >= 0.33
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%description -l pl
libgpod to biblioteka maj�ca na celu wyabstrahowanie dost�pu do
zawarto�ci iPod�w. Udost�pnia �atwe w u�yciu API do pobierania listy
plik�w i playlist zapisanych na iPodzie, modyfikowania ich i
zapisywania z powrotem na iPoda.

%package devel
Summary:	Header files for libgpod library
Summary(pl):	Pliki nag��wkowe biblioteki libgpod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	hal-devel >= 0.5.2

%description devel
This is the package containing the header files for libgpod library.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki libgpod.

%package static
Summary:	Static libgpod library
Summary(pl):	Statyczna biblioteka libgpod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpod library.

%description static -l pl
Statyczna biblioteka libgpod.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-eject-command="/usr/bin/eject" \
	--with-unmount-command="/bin/umount"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgpod.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgpod.la
%attr(755,root,root) %{_libdir}/libgpod.so
%{_pkgconfigdir}/libgpod-1.0.pc
%{_includedir}/gpod-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpod.a
