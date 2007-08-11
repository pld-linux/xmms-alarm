Summary:	An alarm plugin for XMMS
Summary(pl.UTF-8):	Wtyczka budzika do XMMS
Name:		xmms-alarm
Version:	0.3.7
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.snika.uklinux.net/xmms-alarm/%{name}-%{version}.tar.bz2
# Source0-md5:	be1a3b60dbab6b1ab5e3e893c22cbe23
URL:		http://www.snika.uklinux.net/
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms-alarm is an alarm plugin to use with XMMS that fades up the
volume in the morning and wakes you up.

%description -l pl.UTF-8
xmms-alarm to wtyczka budzika do używania z XMMS. Wtyczka ta zwiększa
głośność rano w celu obudzenia.

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
