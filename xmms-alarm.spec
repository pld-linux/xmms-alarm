Summary:	An alarm plugin for XMMS
Summary(pl):    Wtyczka budzika do XMMS
Name:		xmms-alarm
Version:	0.3.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.snika.uklinux.net/xmms-alarm/%{name}-%{version}.tar.gz
# Source0-md5:	0474472d68e29daccb8ce9d0700508ed
URL:		http://www.snika.uklinux.net/
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms-alarm is an alarm plugin to use with XMMS that fades up the
volume in the morning and wakes you up.

%description -l pl
xmms-alarm to wtyczka budzika do u¿ywania z XMMS. Wtyczka ta zwiêksza
g³o¶no¶æ rano w celu obudzenia.

%prep
%setup -q 

%build
cp -f %{_datadir}/automake/install-sh .
cp -f %{_datadir}/automake/config.sub .
%configure \
	--libdir=%{xmms_general_plugindir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{xmms_general_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{xmms_general_plugindir}
