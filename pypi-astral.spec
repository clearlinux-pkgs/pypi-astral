#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-astral
Version  : 2.2
Release  : 36
URL      : https://files.pythonhosted.org/packages/ad/c3/76dfe55a68c48a1a6f3d2eeab2793ebffa9db8adfba82774a7e0f5f43980/astral-2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/c3/76dfe55a68c48a1a6f3d2eeab2793ebffa9db8adfba82774a7e0f5f43980/astral-2.2.tar.gz
Summary  : Calculations for the position of the sun and moon.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-astral-license = %{version}-%{release}
Requires: pypi-astral-python = %{version}-%{release}
Requires: pypi-astral-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(dataclasses)
BuildRequires : pypi(poetry)
BuildRequires : pypi(pytz)

%description
======
        
        |travis_status| |pypi_ver|

%package license
Summary: license components for the pypi-astral package.
Group: Default

%description license
license components for the pypi-astral package.


%package python
Summary: python components for the pypi-astral package.
Group: Default
Requires: pypi-astral-python3 = %{version}-%{release}

%description python
python components for the pypi-astral package.


%package python3
Summary: python3 components for the pypi-astral package.
Group: Default
Requires: python3-core
Provides: pypi(astral)
Requires: pypi(dataclasses)
Requires: pypi(pytz)

%description python3
python3 components for the pypi-astral package.


%prep
%setup -q -n astral-2.2
cd %{_builddir}/astral-2.2
pushd ..
cp -a astral-2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656356939
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-astral
cp %{_builddir}/astral-2.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-astral/a8f3e29d5eab4420318de979754f5637d4bf2c3f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-astral/a8f3e29d5eab4420318de979754f5637d4bf2c3f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
