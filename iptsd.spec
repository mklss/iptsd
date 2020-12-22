%global debug_package %{nil}

Name: iptsd
Version: 0.3
Release: 1%{?dist}
Summary: Userspace daemon for Intel Precise Touch & Stylus
License: GPLv2+

URL: https://github.com/linux-surface/iptsd
Source: {{{ git_dir_pack }}}

BuildRequires: meson
BuildRequires: gcc
BuildRequires: inih-devel
BuildRequires: systemd-rpm-macros

Requires: inih

%description
iptsd is a userspace daemon that processes touch events from the IPTS
kernel driver, and sends them back to the kernel using uinput devices.

%prep
{{{ git_dir_setup_macro }}}

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%check
%meson_test

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/ipts.conf
%{_bindir}/%{name}
%{_bindir}/ipts-dbg
%{_unitdir}/%{name}.service
%{_udevrulesdir}/50-ipts.rules
%{_datadir}/ipts/*
