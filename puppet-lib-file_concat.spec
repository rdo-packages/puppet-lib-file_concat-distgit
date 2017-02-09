%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-lib-file_concat
%global commit 813132b5d776204e1da169a93e4bc6a1e253f75c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-lib-file_concat
Version:                1.0.1
Release:                1%{?alphatag}%{?dist}
Summary:                Library for concatenating multiple files into 1
License:                ASL 2.0

URL:                    https://github.com/electrical/puppet-lib-file_concat

Source0:                https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch


Requires:               puppet >= 2.7.0

%description
Library for concatenating multiple files into 1

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/file_concat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/file_concat/



%files
%{_datadir}/openstack-puppet/modules/file_concat/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.1-1.813132bgit
- Ocata update 1.0.1 (813132b5d776204e1da169a93e4bc6a1e253f75c)

