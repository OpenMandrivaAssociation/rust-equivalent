# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate equivalent

Name:           rust-equivalent
Version:        1.0.1
Release:        1
Summary:        Traits for key comparison in maps
Group:          Development/Rust

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/equivalent
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.6

%global _description %{expand:
Traits for key comparison in maps.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(equivalent) = 1.0.1
Requires:       cargo
Requires:       rust >= 1.6

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(equivalent/default) = 1.0.1
Requires:       cargo
Requires:       crate(equivalent) = 1.0.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
