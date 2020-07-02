#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmpy2
Version  : 2.0.8
Release  : 1
URL      : https://files.pythonhosted.org/packages/90/f4/9a2e384b325b69bc5827b9a6510a8fb4a51698c915c06a3f25a86458892a/gmpy2-2.0.8.zip
Source0  : https://files.pythonhosted.org/packages/90/f4/9a2e384b325b69bc5827b9a6510a8fb4a51698c915c06a3f25a86458892a/gmpy2-2.0.8.zip
Summary  : GMP/MPIR, MPFR, and MPC interface to Python 2.6+ and 3.x
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: gmpy2-license = %{version}-%{release}
Requires: gmpy2-python = %{version}-%{release}
Requires: gmpy2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : gmp-dev
BuildRequires : mpc-dev
BuildRequires : mpfr-dev

%description
Installing gmpy2 on Unix/Linux
------------------------------
Requirements
gmpy2 has only been tested with the most recent versions of GMP, MPFR and MPC.
Specifically, for integer and rational support, gmpy2 requires GMP 5.0.x or
later. To support multiple-precision floating point arithmetic, MPFR 3.1.x or
later is required. MPC 1.0.1 or later is required for complex arithmetic.

%package license
Summary: license components for the gmpy2 package.
Group: Default

%description license
license components for the gmpy2 package.


%package python
Summary: python components for the gmpy2 package.
Group: Default
Requires: gmpy2-python3 = %{version}-%{release}

%description python
python components for the gmpy2 package.


%package python3
Summary: python3 components for the gmpy2 package.
Group: Default
Requires: python3-core
Provides: pypi(gmpy2)

%description python3
python3 components for the gmpy2 package.


%prep
%setup -q -n gmpy2-2.0.8
cd %{_builddir}/gmpy2-2.0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593710325
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gmpy2
cp %{_builddir}/gmpy2-2.0.8/COPYING %{buildroot}/usr/share/package-licenses/gmpy2/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gmpy2-2.0.8/COPYING.LESSER %{buildroot}/usr/share/package-licenses/gmpy2/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmpy2/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gmpy2/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
