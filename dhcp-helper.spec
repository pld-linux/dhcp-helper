Summary:	simple, straightforward DHCP relay agent
Summary(pl):	prosty, nieskomplikowany DHCP relay
Name:		dhcp-helper
Version:	0.2
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	-
URL:		http://thekelleys.org.uk/dhcp-helper/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple, straightforward DHCP relay agent, written as
alternative to the ISC relay.

%description -l pl
To jest prosty, nieskomplikowany agent DHCP relay, napisany jako
alternatywa dla relaya autorstwa ISC.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR="%{_sbindir}" \
	MANDIR="%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
