Summary:	An alarm plugin for XMMS
Summary(pl):    Plugin alarm do XMMS
Name:		xmms-alarm
Version:	0.3.1
Release:	1
License:        GPL
Group:          X11/Applications/Multimedia
Source0:	http://www.snika.uklinux.net/xmms-alarm/%{name}-%{version}.tar.gz
URL: 		http://www.snika.uklinux.net/
Requires:	xmms >= 1.2.0
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
xmms-alarm is an alarm plugin to use with XMMS that fades up the
volume in the morning and wakes you up.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%build

%configure --libdir=/%{_libdir}/xmms/General

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} libdir=$RPM_BUILD_ROOT%{_libdir}/xmms/General install

gzip -9nf  README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/xmms/General/*
%doc *.gz 
