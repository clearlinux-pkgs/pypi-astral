#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astral
Version  : 1.6.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/cc/cc/65ca157e967756a8f08b1cf1c0a1a30c83ed32c50dbe83c557874ce101ca/astral-1.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/cc/65ca157e967756a8f08b1cf1c0a1a30c83ed32c50dbe83c557874ce101ca/astral-1.6.1.tar.gz
Summary  : Calculations for the position of the sun and moon.
Group    : Development/Tools
License  : Apache-2.0
Requires: astral-python3
Requires: astral-python
Requires: pytz
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : pytz
BuildRequires : requests

%description
======
        
        |travis_status| |pypi_ver|

%package python
Summary: python components for the astral package.
Group: Default
Requires: astral-python3

%description python
python components for the astral package.


%package python3
Summary: python3 components for the astral package.
Group: Default
Requires: python3-core

%description python3
python3 components for the astral package.


%prep
%setup -q -n astral-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534604419
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
