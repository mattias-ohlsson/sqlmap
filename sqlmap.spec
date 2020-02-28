%global pypi_name sqlmap

Name:           sqlmap
Version:        1.4.2
Release:        1%{?dist}
Summary:        Automatic SQL injection and database takeover tool

License:        GPLv2+ with exceptions
URL:            http://sqlmap.org
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  /usr/bin/pathfix.py

%description
Sqlmap is an open source penetration testing tool that automates the
process of detecting and exploiting SQL injection flaws and taking over
of database servers. It comes with a powerful detection engine, many
niche features for the ultimate penetration tester and a broad range of
switches lasting from database fingerprinting, over data fetching from
the database, to accessing the underlying file system and executing
commands on the operating system via out-of-band connections.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" sqlmap/extra/shutils/duplicates.py

%build
%py3_build

%install
%py3_install

%files
%license sqlmap/LICENSE sqlmap/thirdparty/socks/LICENSE sqlmap/thirdparty/identywaf/LICENSE
%doc README.rst
%{_bindir}/sqlmap
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.4.2-1
- Initial build
