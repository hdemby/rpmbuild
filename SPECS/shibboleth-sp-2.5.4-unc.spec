# Project    : Shibboleth-2.5.4
# File       : shibboleth-sp-2.5.4-unc.spec
# Copyright  : Shibboleth

Summary: Shibboleth for RHEL6
Name: shibboleth-sp
Version: 2.5.4
Release: unc
Group: Networking-IP Services
URL: http://download.opensuse.org/repositories/security:/shibboleth/RHEL_6/i686/shibboleth-2.5.4-3.3.el6.i686.rpm
License: GNU GPL version 2

Source:%{name}-%{version}-%{release}.tar.gz

%define _topdir /usr/local/rpmbuild
Buildroot: %{_tmppath}/ROOT
AutoProv: no

%description 
Shibboleth-2.5.4 for RHEL6 and CentOS6

%package shibboleth-sp-2.5.4
Summary: SHibboleth
Group: DNS

%description shibboleth-sp-2.5.4

%build

%install
tar xvfz /usr/local/rpmbuild/SOURCES/shibboleth-sp-2.5.4-unc.tar.gz -C /usr/local/rpmbuild/ROOT/

%files
%defattr(-,bin,bin)
/opt/unc/shibboleth-sp/*
