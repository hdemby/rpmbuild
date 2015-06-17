Summary: grepcidr IP address search engine
Name: grepcidr
Version:2
Release:99
License: GPL
Group:UNC-ITS - Networking
%define _topdir /home/hdemby/rpmbuild
URL: http://www.taugh.com/grepcidr-2/grepcidr-2.99.tjz
Buildroot: %{_topdir}/ROOT
AutoReqProv: no

%description
grepcidr IP address search locate application
%install
mkdir -p %{buildroot}/opt/unc/grepcidr-2.99
cp /home/hdemby/rpmbuild/BUILD/grepcidr-2.99/grepcidr %{buildroot}/opt/unc/
%files
%defattr(-,bin,bin)
/opt/unc/grepcidr

