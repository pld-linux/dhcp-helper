Summary:	Simple, straightforward DHCP relay agent
Summary(pl.UTF-8):	Prosty, nieskomplikowany DHCP relay
Name:		dhcp-helper
Version:	0.8
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://thekelleys.org.uk/dhcp-helper/%{name}-%{version}.tar.gz
# Source0-md5:	e7029d720878e335564872ad3551f901
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://thekelleys.org.uk/dhcp-helper/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple, straightforward DHCP relay agent, written as
alternative to the ISC relay.

%description -l pl.UTF-8
To jest prosty, nieskomplikowany agent DHCP relay, napisany jako
alternatywa dla relaya autorstwa ISC.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR="%{_sbindir}" \
	MANDIR="%{_mandir}"

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add dhcp-helper
%service dhcp-helper restart "dhcp-helper daemon"

%preun
if [ "$1" = "0" ];then
	%service dhcp-helper stop
	/sbin/chkconfig --del dhcp-helper
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/dhcp-helper
%attr(754,root,root) /etc/rc.d/init.d/dhcp-helper
%attr(755,root,root) %{_sbindir}/dhcp-helper
%{_mandir}/man8/dhcp-helper.8*
