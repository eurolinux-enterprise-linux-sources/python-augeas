# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 9 || 0%{?rhel} >= 6
%bcond_without egg
%endif

%global with_python3 0

Name:		python-augeas
Version:	0.5.0
Release:	2%{?dist}
Summary:	Python bindings to augeas
Group:		Development/Languages
License:	LGPLv2+
URL:		http://augeas.net/
Source0:	http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	augeas-libs
BuildArch:	noarch

BuildRequires:	python-setuptools python-devel
%if 0%{?with_python3}
BuildRequires:	python3-setuptools python3-devel
%endif # with_python3

%description
python-augeas is a set of Python bindings around augeas.


%if 0%{?with_python3}
%package -n python3-augeas
Summary:	Python 3 bindings to augeas
Requires:	augeas-libs

%description -n python3-augeas
python3-augeas is a set of Python bindings around augeas.
%endif # with_python3


%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS"
%{__python} setup.py build_ext -i
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build_ext -i
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%files
%doc COPYING AUTHORS README.txt
%{python_sitelib}/augeas.py*
%if %{with egg}
%{python_sitelib}/*augeas*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-augeas
%doc COPYING AUTHORS README.txt
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Mon Sep 22 2014 Tomas Radej <tradej@redhat.com> - 0.5.0-2
- Added Python 3 subpackage

* Thu Sep 04 2014 Greg Swift <gregswift@gmail.com> - 0.5.0-1
- Version 0.5.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Greg Swift <gregswift@gmail.com> - 0.4.1-5
- add python-ctypes dependency (rhbz#1020239)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Greg Swift <gregswift@gmail.com> 0.4.1-1
- version 0.4.1
- include egg only on F-9, RHEL-6 and later

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 18 2011 Harald Hoyer <harald@redhat.com> 0.3.0-7
- only include egg-info, if fedora >=9 or rhel >= 6
Resolves: rhbz#661452

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.0-2
- Rebuild for Python 2.6

* Tue Sep 09 2008 Harald Hoyer <harald@redhat.com> 0.3.0-1
- version 0.3.0

* Thu Jul 03 2008 Harald Hoyer <harald@redhat.com> 0.2.1-1
- version 0.2.1

* Wed Jun 11 2008 Harald Hoyer <harald@redhat.com> 0.2.0-1
- switched to noarch, dlopen/ python bindings

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-4
- version to import in CVS (rhbz#444945)

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-3
- set mode of _augeas.so to 0755

* Mon May 05 2008 Harald Hoyer <harald@redhat.com> 0.1.0-2
- wildcard to catch egg-info in case it is build

* Fri May 02 2008 Harald Hoyer <harald@redhat.com> 0.1.0-1
- new version

* Wed Apr 16 2008 Harald Hoyer <harald@redhat.com> - 0.0.8-1
- initial version
