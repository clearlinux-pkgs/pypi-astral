#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astral
Version  : 2.2
Release  : 28
URL      : https://files.pythonhosted.org/packages/ad/c3/76dfe55a68c48a1a6f3d2eeab2793ebffa9db8adfba82774a7e0f5f43980/astral-2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/c3/76dfe55a68c48a1a6f3d2eeab2793ebffa9db8adfba82774a7e0f5f43980/astral-2.2.tar.gz
Summary  : Calculations for the position of the sun and moon.
Group    : Development/Tools
License  : Apache-2.0
Requires: astral-license = %{version}-%{release}
Requires: astral-python = %{version}-%{release}
Requires: astral-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
======
        
        |travis_status| |pypi_ver|

%package license
Summary: license components for the astral package.
Group: Default

%description license
license components for the astral package.


%package python
Summary: python components for the astral package.
Group: Default
Requires: astral-python3 = %{version}-%{release}

%description python
python components for the astral package.


%package python3
Summary: python3 components for the astral package.
Group: Default
Requires: python3-core
Provides: pypi(astral)
Requires: pypi(pytz)

%description python3
python3 components for the astral package.


%prep
%setup -q -n astral-2.2
cd %{_builddir}/astral-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620625436
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astral
cp %{_builddir}/astral-2.2/LICENSE %{buildroot}/usr/share/package-licenses/astral/a8f3e29d5eab4420318de979754f5637d4bf2c3f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astral/a8f3e29d5eab4420318de979754f5637d4bf2c3f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
