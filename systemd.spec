#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : systemd
Version  : 238
Release  : 171
URL      : https://github.com/systemd/systemd/archive/v238.tar.gz
Source0  : https://github.com/systemd/systemd/archive/v238.tar.gz
Summary  : systemd Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: systemd-bin
Requires: systemd-config
Requires: systemd-autostart
Requires: systemd-lib
Requires: systemd-data
Requires: systemd-doc
Requires: systemd-locales
Requires: dnf-plugins-core
Requires: meson
Requires: libcap
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : bzip2-dev
BuildRequires : cryptsetup-dev
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : docbook-xml
BuildRequires : elfutils-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : gettext-dev
BuildRequires : glib-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : iptables-dev
BuildRequires : iptables-dev32
BuildRequires : kmod-dev
BuildRequires : kmod-dev32
BuildRequires : libcap-dev
BuildRequires : libcap-dev32
BuildRequires : libcgroup-dev
BuildRequires : libffi-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgcrypt-dev32
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
BuildRequires : readline-dev
BuildRequires : shadow
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
BuildRequires : util-linux-extras
BuildRequires : zlib-dev32
Patch1: 0001-Fix-preprocessor-issues-with-MS_MOVE-not-getting-def.patch
Patch2: 0002-basic-macros-rename-noreturn-into-_noreturn_.patch
Patch3: 0003-Re-shrunk-the-PCI-vendor-ID-list-to-include-only-Int.patch
Patch4: 0004-journal-raise-compression-threshold.patch
Patch5: 0005-journal-clearout-drop-kmsg.patch
Patch6: 0006-core-use-mmap-to-load-files.patch
Patch7: 0007-Build-drop-pam-nsswitch-ship-legacy-tmpfiles.patch
Patch8: 0008-journal-flush-var-kmsg-after-starting.patch
Patch9: 0009-logind-pam-fix-systemd-user-to-include-common-sessio.patch
Patch10: 0010-analyze-increase-precision.patch
Patch11: 0011-sd-event-return-malloc-memory-reserves-when-main-loo.patch
Patch12: 0012-efi-boot-generator-Do-not-automount-boot-partition.patch
Patch13: 0013-core-do-not-apply-presets.patch
Patch14: 0014-locale-setup-set-default-locale-to-a-unicode-one.patch
Patch15: 0015-mount-setup-mount-kernel-fs-by-default.patch
Patch16: 0016-Ship-default-services-in-system-unit-dir.patch
Patch17: 0017-bootctl-Add-force-option-to-enable-chroot-install-re.patch
Patch18: 0018-kernel-install-Support-alternate-root-usage-via-SUBD.patch
Patch19: 0019-bootctl-Handle-gummiboot-systemd-migration.patch
Patch20: 0020-tmpfiles-Make-var-cache-ldconfig-world-readable.patch
Patch21: 0021-Set-a-default-unique-hostname-when-it-is-either-clr-.patch
Patch22: 0022-more-udev-children-workers.patch
Patch23: 0023-not-load-iptables.patch
Patch24: 0024-Add-journal-flush-service-for-Microsoft-Azure-VMs.patch
Patch25: 0025-Disable-resolved-as-default-resolver-write-at-boot.patch
Patch26: 0026-Enable-BBR-Bottleneck-Bandwidth-and-RTT.patch
Patch27: 0027-network-online-complete-once-one-link-is-online-not-.patch
Patch28: 0028-DHCP-retry-faster.patch
Patch29: 0029-Remove-libm-memory-overhead.patch
Patch30: 0030-udev-log-also-device-path.patch
Patch31: 0031-skip-not-present-ACPI-devices.patch
Patch32: 0032-Ensure-var-run-is-never-a-directory.patch
Patch33: 0033-Make-timesyncd-a-simple-service.patch
Patch34: 0034-Compile-udev-with-O3.patch
Patch35: 0035-Don-t-wait-for-utmp-at-shutdown.patch
Patch36: 0036-Don-t-do-transient-hostnames-we-set-ours-already.patch

%description
systemd System and Service Manager
DETAILS:
http://0pointer.de/blog/projects/systemd.html

%package autostart
Summary: autostart components for the systemd package.
Group: Default

%description autostart
autostart components for the systemd package.


%package bin
Summary: bin components for the systemd package.
Group: Binaries
Requires: systemd-data
Requires: systemd-config
Obsoletes: systemd-boot
Provides: systemd-boot
Obsoletes: systemd-console
Provides: systemd-console
Obsoletes: systemd-coredump
Provides: systemd-coredump
Obsoletes: systemd-cryptsetup
Provides: systemd-cryptsetup

%description bin
bin components for the systemd package.


%package config
Summary: config components for the systemd package.
Group: Default

%description config
config components for the systemd package.


%package data
Summary: data components for the systemd package.
Group: Data

%description data
data components for the systemd package.


%package dev
Summary: dev components for the systemd package.
Group: Development
Requires: systemd-lib
Requires: systemd-bin
Requires: systemd-data
Provides: systemd-devel

%description dev
dev components for the systemd package.


%package dev32
Summary: dev32 components for the systemd package.
Group: Default
Requires: systemd-lib32
Requires: systemd-bin
Requires: systemd-data
Requires: systemd-dev

%description dev32
dev32 components for the systemd package.


%package doc
Summary: doc components for the systemd package.
Group: Documentation

%description doc
doc components for the systemd package.


%package extras
Summary: extras components for the systemd package.
Group: Default
Obsoletes: systemd-hwdb
Provides: systemd-hwdb
Obsoletes: systemd-polkit
Provides: systemd-polkit

%description extras
extras components for the systemd package.


%package lib
Summary: lib components for the systemd package.
Group: Libraries
Requires: systemd-data
Obsoletes: systemd-lib
Provides: systemd-lib

%description lib
lib components for the systemd package.


%package lib32
Summary: lib32 components for the systemd package.
Group: Default
Requires: systemd-data
Requires: libcap

%description lib32
lib32 components for the systemd package.


%package locales
Summary: locales components for the systemd package.
Group: Default
Obsoletes: systemd-locale
Provides: systemd-locale

%description locales
locales components for the systemd package.


%prep
%setup -q -n systemd-238
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
pushd ..
cp -a systemd-238 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526580983
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Ddefault-hierarchy=legacy \
-Dsmack=false \
-Dsysvinit-path= \
-Dsysvrcnd_path= \
-Dxz=false \
-Dgcrypt=false \
-Dlz4=false  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
CFLAGS="$CFLAGS -m32" CXXFLAGS="$CXXFLAGS -m32" LDFLAGS="$LDFLAGS -m32" PKG_CONFIG_PATH="/usr/lib32/pkgconfig" meson --libdir=/usr/lib32 --prefix /usr --buildtype=plain -Ddefault-hierarchy=legacy \
-Dsmack=false \
-Dsysvinit-path= \
-Dsysvrcnd_path= \
-Dxz=false \
-Dgcrypt=false \
-Dlz4=false -Dlibcryptsetup=false \
-Dgnutls=false \
-Dlibcurl=false \
-Delfutils=false builddir
ninja -v -C builddir
popd

%install
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang systemd
## make_install_append content
rm -f %{buildroot}/usr/lib/sysusers.d/basic.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-remote.conf
rmdir %{buildroot}/usr/lib/sysusers.d
rm -f %{buildroot}/usr/lib/systemd/libsystemd-shared.so
rm -f %{buildroot}/etc/systemd/journald.conf
rm -f %{buildroot}/etc/systemd/logind.conf
rm -f %{buildroot}/etc/systemd/resolved.conf
rm -f %{buildroot}/etc/systemd/system.conf
rm -f %{buildroot}/etc/systemd/timesyncd.conf
rm -f %{buildroot}/etc/systemd/user.conf
rm -f %{buildroot}/etc/udev/udev.conf
rmdir %{buildroot}/etc/udev/hwdb.d
rmdir %{buildroot}/etc/udev/rules.d
rmdir %{buildroot}/etc/udev
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
rm -f %{buildroot}/etc/xdg/systemd/user
rm -f %{buildroot}/usr/lib/environment.d/99-environment.conf
mv %{buildroot}/etc/pam.d %{buildroot}/usr/share/.
mkdir -p %{buildroot}/usr/lib/udev/hwdb.d/20
mv %{buildroot}/usr/lib/udev/hwdb.d/20-* %{buildroot}/usr/lib/udev/hwdb.d/20
builddir/udevadm hwdb --root %{buildroot} --update --usr
mv %{buildroot}/usr/lib/udev/hwdb.d/20/* %{buildroot}/usr/lib/udev/hwdb.d/
rmdir %{buildroot}/usr/lib/udev/hwdb.d/20
builddir/journalctl --root %{buildroot} --update-catalog
mkdir -p %{buildroot}/usr/lib/systemd/system-coredump
ln -s ../../../bin/crashprobe %{buildroot}/usr/lib/systemd/system-coredump/crashprobe
rm -rvf %{buildroot}/usr/lib/kernel
rm -rvf %{buildroot}/var/lib/polkit-1
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/systemd-timesyncd.service %{buildroot}/usr/share/clr-service-restart/systemd-timesyncd.service
ln -sf /usr/lib/systemd/system/systemd-resolved.service %{buildroot}/usr/share/clr-service-restart/systemd-resolved.service
ln -sf /usr/lib/systemd/system/systemd-udevd.service %{buildroot}/usr/share/clr-service-restart/systemd-udevd.service
ln -sf /usr/lib/systemd/system/systemd-journald.service %{buildroot}/usr/share/clr-service-restart/systemd-journald.service
## make_install_append end

%files
%defattr(-,root,root,-)
%exclude /usr/lib/udev/cdrom_id
%exclude /usr/lib/udev/collect
%exclude /usr/lib/udev/hwdb.d/20-OUI.hwdb
%exclude /usr/lib/udev/hwdb.d/20-acpi-vendor.hwdb
%exclude /usr/lib/udev/hwdb.d/20-bluetooth-vendor-product.hwdb
%exclude /usr/lib/udev/hwdb.d/20-net-ifname.hwdb
%exclude /usr/lib/udev/hwdb.d/20-pci-classes.hwdb
%exclude /usr/lib/udev/hwdb.d/20-pci-vendor-model.hwdb
%exclude /usr/lib/udev/hwdb.d/20-sdio-classes.hwdb
%exclude /usr/lib/udev/hwdb.d/20-sdio-vendor-model.hwdb
%exclude /usr/lib/udev/hwdb.d/20-usb-classes.hwdb
%exclude /usr/lib/udev/hwdb.d/60-evdev.hwdb
%exclude /usr/lib/udev/hwdb.d/60-keyboard.hwdb
%exclude /usr/lib/udev/hwdb.d/60-sensor.hwdb
%exclude /usr/lib/udev/hwdb.d/70-mouse.hwdb
%exclude /usr/lib/udev/hwdb.d/70-pointingstick.hwdb
%exclude /usr/lib/udev/hwdb.d/70-touchpad.hwdb
%exclude /usr/lib/udev/mtd_probe
%exclude /usr/lib/udev/v4l_id
%exclude /var/lib/systemd/catalog/database
/usr/lib/modprobe.d/systemd.conf
/usr/lib/rpm/macros.d/macros.systemd
/usr/lib/udev/ata_id
/usr/lib/udev/hwdb.bin
/usr/lib/udev/hwdb.d/20-usb-vendor-model.hwdb
/usr/lib/udev/hwdb.d/70-joystick.hwdb
/usr/lib/udev/scsi_id

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/local-fs.target.wants/systemd-remount-fs.service
/usr/lib/systemd/system/local-fs.target.wants/tmp.mount
/usr/lib/systemd/system/machines.target.wants/var-lib-machines.mount
/usr/lib/systemd/system/multi-user.target.wants/getty.target
/usr/lib/systemd/system/multi-user.target.wants/remote-fs.target
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/multi-user.target.wants/systemd-logind.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-networkd.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-resolved.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-user-sessions.service
/usr/lib/systemd/system/network-online.target.wants/systemd-networkd-wait-online.service
/usr/lib/systemd/system/remote-fs.target.wants/var-lib-machines.mount
/usr/lib/systemd/system/sockets.target.wants/systemd-coredump.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-initctl.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald-audit.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-networkd.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-udevd-control.socket
/usr/lib/systemd/system/sockets.target.wants/systemd-udevd-kernel.socket
/usr/lib/systemd/system/sysinit.target.wants/cryptsetup.target
/usr/lib/systemd/system/sysinit.target.wants/kmod-static-nodes.service
/usr/lib/systemd/system/sysinit.target.wants/proc-sys-fs-binfmt_misc.automount
/usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/usr/lib/systemd/system/sysinit.target.wants/systemd-binfmt.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush-msft.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-journald.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-modules-load.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-random-seed.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-sysctl.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-timesyncd.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-udevd.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-update-utmp.service
/usr/lib/systemd/system/timers.target.wants/systemd-tmpfiles-clean.timer

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/systemd-firstboot
%exclude /usr/bin/systemd-hwdb
%exclude /usr/bin/systemd-sysusers
/usr/bin/bootctl
/usr/bin/busctl
/usr/bin/coredumpctl
/usr/bin/halt
/usr/bin/hostnamectl
/usr/bin/init
/usr/bin/journalctl
/usr/bin/kernel-install
/usr/bin/localectl
/usr/bin/loginctl
/usr/bin/machinectl
/usr/bin/networkctl
/usr/bin/poweroff
/usr/bin/reboot
/usr/bin/runlevel
/usr/bin/shutdown
/usr/bin/systemctl
/usr/bin/systemd-analyze
/usr/bin/systemd-ask-password
/usr/bin/systemd-cat
/usr/bin/systemd-cgls
/usr/bin/systemd-cgtop
/usr/bin/systemd-delta
/usr/bin/systemd-detect-virt
/usr/bin/systemd-escape
/usr/bin/systemd-inhibit
/usr/bin/systemd-machine-id-setup
/usr/bin/systemd-mount
/usr/bin/systemd-notify
/usr/bin/systemd-nspawn
/usr/bin/systemd-path
/usr/bin/systemd-resolve
/usr/bin/systemd-run
/usr/bin/systemd-socket-activate
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-tmpfiles
/usr/bin/systemd-tty-ask-password-agent
/usr/bin/systemd-umount
/usr/bin/telinit
/usr/bin/timedatectl
/usr/bin/udevadm

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/sysctl.d/50-coredump.conf
%exclude /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
%exclude /usr/lib/systemd/system-generators/systemd-system-update-generator
%exclude /usr/lib/systemd/system/ldconfig.service
%exclude /usr/lib/systemd/system/local-fs.target.wants/systemd-remount-fs.service
%exclude /usr/lib/systemd/system/local-fs.target.wants/tmp.mount
%exclude /usr/lib/systemd/system/machines.target.wants/var-lib-machines.mount
%exclude /usr/lib/systemd/system/multi-user.target.wants/getty.target
%exclude /usr/lib/systemd/system/multi-user.target.wants/remote-fs.target
%exclude /usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
%exclude /usr/lib/systemd/system/multi-user.target.wants/systemd-logind.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/systemd-networkd.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/systemd-resolved.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/systemd-user-sessions.service
%exclude /usr/lib/systemd/system/network-online.target.wants/systemd-networkd-wait-online.service
%exclude /usr/lib/systemd/system/remote-fs.target.wants/var-lib-machines.mount
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-coredump.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-initctl.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-journald-audit.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-networkd.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-udevd-control.socket
%exclude /usr/lib/systemd/system/sockets.target.wants/systemd-udevd-kernel.socket
%exclude /usr/lib/systemd/system/sysinit.target.wants/cryptsetup.target
%exclude /usr/lib/systemd/system/sysinit.target.wants/kmod-static-nodes.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/proc-sys-fs-binfmt_misc.automount
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-binfmt.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush-msft.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-journald.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-modules-load.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-random-seed.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-sysctl.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-timesyncd.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-udevd.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-update-utmp.service
%exclude /usr/lib/systemd/system/system-update-cleanup.service
%exclude /usr/lib/systemd/system/system-update.target
%exclude /usr/lib/systemd/system/systemd-firstboot.service
%exclude /usr/lib/systemd/system/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/systemd-journal-catalog-update.service
%exclude /usr/lib/systemd/system/systemd-journal-upload.service
%exclude /usr/lib/systemd/system/systemd-sysusers.service
%exclude /usr/lib/systemd/system/systemd-tmpfiles-setup-dev.service
%exclude /usr/lib/systemd/system/systemd-update-done.service
%exclude /usr/lib/systemd/system/timers.target.wants/systemd-tmpfiles-clean.timer
%exclude /usr/lib/systemd/system/var-lib-machines.mount
%exclude /usr/lib/systemd/systemd-journal-upload
%exclude /usr/lib/systemd/systemd-update-done
%exclude /usr/lib/udev/rules.d/60-cdrom_id.rules
%exclude /usr/lib/udev/rules.d/60-persistent-alsa.rules
%exclude /usr/lib/udev/rules.d/60-persistent-storage-tape.rules
%exclude /usr/lib/udev/rules.d/60-persistent-v4l.rules
%exclude /usr/lib/udev/rules.d/70-joystick.rules
%exclude /usr/lib/udev/rules.d/75-probe_mtd.rules
%exclude /usr/lib/udev/rules.d/78-sound-card.rules
/usr/lib/sysctl.d/50-default.conf
/usr/lib/systemd/boot/efi/linuxx64.efi.stub
/usr/lib/systemd/boot/efi/systemd-bootx64.efi
/usr/lib/systemd/catalog/systemd.be.catalog
/usr/lib/systemd/catalog/systemd.be@latin.catalog
/usr/lib/systemd/catalog/systemd.bg.catalog
/usr/lib/systemd/catalog/systemd.catalog
/usr/lib/systemd/catalog/systemd.de.catalog
/usr/lib/systemd/catalog/systemd.fr.catalog
/usr/lib/systemd/catalog/systemd.it.catalog
/usr/lib/systemd/catalog/systemd.pl.catalog
/usr/lib/systemd/catalog/systemd.pt_BR.catalog
/usr/lib/systemd/catalog/systemd.ru.catalog
/usr/lib/systemd/catalog/systemd.zh_CN.catalog
/usr/lib/systemd/catalog/systemd.zh_TW.catalog
/usr/lib/systemd/libsystemd-shared-238.so
/usr/lib/systemd/network/80-container-host0.network
/usr/lib/systemd/network/80-container-ve.network
/usr/lib/systemd/network/80-container-vz.network
/usr/lib/systemd/network/99-default.link
/usr/lib/systemd/resolv.conf
/usr/lib/systemd/system-coredump/crashprobe
/usr/lib/systemd/system-generators/systemd-cryptsetup-generator
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
/usr/lib/systemd/system-generators/systemd-gpt-auto-generator
/usr/lib/systemd/system-generators/systemd-veritysetup-generator
/usr/lib/systemd/system-preset/90-systemd.preset
/usr/lib/systemd/system/autovt@.service
/usr/lib/systemd/system/basic.target
/usr/lib/systemd/system/bluetooth.target
/usr/lib/systemd/system/console-getty.service
/usr/lib/systemd/system/container-getty@.service
/usr/lib/systemd/system/cryptsetup-pre.target
/usr/lib/systemd/system/cryptsetup.target
/usr/lib/systemd/system/ctrl-alt-del.target
/usr/lib/systemd/system/dbus-org.freedesktop.hostname1.service
/usr/lib/systemd/system/dbus-org.freedesktop.locale1.service
/usr/lib/systemd/system/dbus-org.freedesktop.login1.service
/usr/lib/systemd/system/dbus-org.freedesktop.machine1.service
/usr/lib/systemd/system/dbus-org.freedesktop.network1.service
/usr/lib/systemd/system/dbus-org.freedesktop.resolve1.service
/usr/lib/systemd/system/dbus-org.freedesktop.timedate1.service
/usr/lib/systemd/system/debug-shell.service
/usr/lib/systemd/system/default.target
/usr/lib/systemd/system/emergency.service
/usr/lib/systemd/system/emergency.target
/usr/lib/systemd/system/exit.target
/usr/lib/systemd/system/final.target
/usr/lib/systemd/system/getty-pre.target
/usr/lib/systemd/system/getty.target
/usr/lib/systemd/system/getty@.service
/usr/lib/systemd/system/graphical.target
/usr/lib/systemd/system/halt.target
/usr/lib/systemd/system/hibernate.target
/usr/lib/systemd/system/hybrid-sleep.target
/usr/lib/systemd/system/initrd-cleanup.service
/usr/lib/systemd/system/initrd-fs.target
/usr/lib/systemd/system/initrd-parse-etc.service
/usr/lib/systemd/system/initrd-root-device.target
/usr/lib/systemd/system/initrd-root-fs.target
/usr/lib/systemd/system/initrd-switch-root.service
/usr/lib/systemd/system/initrd-switch-root.target
/usr/lib/systemd/system/initrd-udevadm-cleanup-db.service
/usr/lib/systemd/system/initrd.target
/usr/lib/systemd/system/kexec.target
/usr/lib/systemd/system/kmod-static-nodes.service
/usr/lib/systemd/system/local-fs-pre.target
/usr/lib/systemd/system/local-fs.target
/usr/lib/systemd/system/machine.slice
/usr/lib/systemd/system/machines.target
/usr/lib/systemd/system/multi-user.target
/usr/lib/systemd/system/network-online.target
/usr/lib/systemd/system/network-pre.target
/usr/lib/systemd/system/network.target
/usr/lib/systemd/system/nss-lookup.target
/usr/lib/systemd/system/nss-user-lookup.target
/usr/lib/systemd/system/paths.target
/usr/lib/systemd/system/poweroff.target
/usr/lib/systemd/system/printer.target
/usr/lib/systemd/system/proc-sys-fs-binfmt_misc.automount
/usr/lib/systemd/system/proc-sys-fs-binfmt_misc.mount
/usr/lib/systemd/system/quotaon.service
/usr/lib/systemd/system/reboot.target
/usr/lib/systemd/system/remote-cryptsetup.target
/usr/lib/systemd/system/remote-fs-pre.target
/usr/lib/systemd/system/remote-fs.target
/usr/lib/systemd/system/rescue.service
/usr/lib/systemd/system/rescue.target
/usr/lib/systemd/system/rpcbind.target
/usr/lib/systemd/system/runlevel0.target
/usr/lib/systemd/system/runlevel1.target
/usr/lib/systemd/system/runlevel2.target
/usr/lib/systemd/system/runlevel3.target
/usr/lib/systemd/system/runlevel4.target
/usr/lib/systemd/system/runlevel5.target
/usr/lib/systemd/system/runlevel6.target
/usr/lib/systemd/system/serial-getty@.service
/usr/lib/systemd/system/shutdown.target
/usr/lib/systemd/system/sigpwr.target
/usr/lib/systemd/system/sleep.target
/usr/lib/systemd/system/slices.target
/usr/lib/systemd/system/smartcard.target
/usr/lib/systemd/system/sockets.target
/usr/lib/systemd/system/sound.target
/usr/lib/systemd/system/suspend.target
/usr/lib/systemd/system/swap.target
/usr/lib/systemd/system/sysinit.target
/usr/lib/systemd/system/syslog.socket
/usr/lib/systemd/system/systemd-ask-password-console.path
/usr/lib/systemd/system/systemd-ask-password-console.service
/usr/lib/systemd/system/systemd-ask-password-wall.path
/usr/lib/systemd/system/systemd-ask-password-wall.service
/usr/lib/systemd/system/systemd-backlight@.service
/usr/lib/systemd/system/systemd-binfmt.service
/usr/lib/systemd/system/systemd-coredump.socket
/usr/lib/systemd/system/systemd-coredump@.service
/usr/lib/systemd/system/systemd-exit.service
/usr/lib/systemd/system/systemd-fsck-root.service
/usr/lib/systemd/system/systemd-fsck@.service
/usr/lib/systemd/system/systemd-halt.service
/usr/lib/systemd/system/systemd-hibernate-resume@.service
/usr/lib/systemd/system/systemd-hibernate.service
/usr/lib/systemd/system/systemd-hostnamed.service
/usr/lib/systemd/system/systemd-hybrid-sleep.service
/usr/lib/systemd/system/systemd-initctl.service
/usr/lib/systemd/system/systemd-initctl.socket
/usr/lib/systemd/system/systemd-journal-flush-msft.service
/usr/lib/systemd/system/systemd-journal-flush.service
/usr/lib/systemd/system/systemd-journald-audit.socket
/usr/lib/systemd/system/systemd-journald-dev-log.socket
/usr/lib/systemd/system/systemd-journald.service
/usr/lib/systemd/system/systemd-journald.socket
/usr/lib/systemd/system/systemd-kexec.service
/usr/lib/systemd/system/systemd-localed.service
/usr/lib/systemd/system/systemd-logind.service
/usr/lib/systemd/system/systemd-machine-id-commit.service
/usr/lib/systemd/system/systemd-machined.service
/usr/lib/systemd/system/systemd-modules-load.service
/usr/lib/systemd/system/systemd-networkd-wait-online.service
/usr/lib/systemd/system/systemd-networkd.service
/usr/lib/systemd/system/systemd-networkd.socket
/usr/lib/systemd/system/systemd-nspawn@.service
/usr/lib/systemd/system/systemd-poweroff.service
/usr/lib/systemd/system/systemd-quotacheck.service
/usr/lib/systemd/system/systemd-random-seed.service
/usr/lib/systemd/system/systemd-reboot.service
/usr/lib/systemd/system/systemd-remount-fs.service
/usr/lib/systemd/system/systemd-resolved.service
/usr/lib/systemd/system/systemd-rfkill.service
/usr/lib/systemd/system/systemd-rfkill.socket
/usr/lib/systemd/system/systemd-suspend.service
/usr/lib/systemd/system/systemd-sysctl.service
/usr/lib/systemd/system/systemd-timedated.service
/usr/lib/systemd/system/systemd-timesyncd.service
/usr/lib/systemd/system/systemd-tmpfiles-clean.service
/usr/lib/systemd/system/systemd-tmpfiles-clean.timer
/usr/lib/systemd/system/systemd-tmpfiles-setup.service
/usr/lib/systemd/system/systemd-udev-settle.service
/usr/lib/systemd/system/systemd-udev-trigger.service
/usr/lib/systemd/system/systemd-udevd-control.socket
/usr/lib/systemd/system/systemd-udevd-kernel.socket
/usr/lib/systemd/system/systemd-udevd.service
/usr/lib/systemd/system/systemd-update-utmp.service
/usr/lib/systemd/system/systemd-user-sessions.service
/usr/lib/systemd/system/systemd-vconsole-setup.service
/usr/lib/systemd/system/systemd-volatile-root.service
/usr/lib/systemd/system/time-sync.target
/usr/lib/systemd/system/timers.target
/usr/lib/systemd/system/tmp.mount
/usr/lib/systemd/system/umount.target
/usr/lib/systemd/system/user.slice
/usr/lib/systemd/system/user@.service
/usr/lib/systemd/systemd
/usr/lib/systemd/systemd-ac-power
/usr/lib/systemd/systemd-backlight
/usr/lib/systemd/systemd-binfmt
/usr/lib/systemd/systemd-cgroups-agent
/usr/lib/systemd/systemd-coredump
/usr/lib/systemd/systemd-cryptsetup
/usr/lib/systemd/systemd-dissect
/usr/lib/systemd/systemd-fsck
/usr/lib/systemd/systemd-growfs
/usr/lib/systemd/systemd-hibernate-resume
/usr/lib/systemd/systemd-hostnamed
/usr/lib/systemd/systemd-initctl
/usr/lib/systemd/systemd-journald
/usr/lib/systemd/systemd-localed
/usr/lib/systemd/systemd-logind
/usr/lib/systemd/systemd-machined
/usr/lib/systemd/systemd-makefs
/usr/lib/systemd/systemd-modules-load
/usr/lib/systemd/systemd-networkd
/usr/lib/systemd/systemd-networkd-wait-online
/usr/lib/systemd/systemd-quotacheck
/usr/lib/systemd/systemd-random-seed
/usr/lib/systemd/systemd-remount-fs
/usr/lib/systemd/systemd-reply-password
/usr/lib/systemd/systemd-resolved
/usr/lib/systemd/systemd-rfkill
/usr/lib/systemd/systemd-shutdown
/usr/lib/systemd/systemd-sleep
/usr/lib/systemd/systemd-socket-proxyd
/usr/lib/systemd/systemd-sulogin-shell
/usr/lib/systemd/systemd-sysctl
/usr/lib/systemd/systemd-timedated
/usr/lib/systemd/systemd-timesyncd
/usr/lib/systemd/systemd-udevd
/usr/lib/systemd/systemd-update-utmp
/usr/lib/systemd/systemd-user-sessions
/usr/lib/systemd/systemd-vconsole-setup
/usr/lib/systemd/systemd-veritysetup
/usr/lib/systemd/systemd-volatile-root
/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator
/usr/lib/systemd/user-preset/90-systemd.preset
/usr/lib/systemd/user/basic.target
/usr/lib/systemd/user/bluetooth.target
/usr/lib/systemd/user/default.target
/usr/lib/systemd/user/exit.target
/usr/lib/systemd/user/graphical-session-pre.target
/usr/lib/systemd/user/graphical-session.target
/usr/lib/systemd/user/paths.target
/usr/lib/systemd/user/printer.target
/usr/lib/systemd/user/shutdown.target
/usr/lib/systemd/user/smartcard.target
/usr/lib/systemd/user/sockets.target
/usr/lib/systemd/user/sound.target
/usr/lib/systemd/user/systemd-exit.service
/usr/lib/systemd/user/systemd-tmpfiles-clean.service
/usr/lib/systemd/user/systemd-tmpfiles-clean.timer
/usr/lib/systemd/user/systemd-tmpfiles-setup.service
/usr/lib/systemd/user/timers.target
/usr/lib/tmpfiles.d/etc.conf
/usr/lib/tmpfiles.d/home.conf
/usr/lib/tmpfiles.d/journal-nocow.conf
/usr/lib/tmpfiles.d/legacy.conf
/usr/lib/tmpfiles.d/systemd-nologin.conf
/usr/lib/tmpfiles.d/systemd-nspawn.conf
/usr/lib/tmpfiles.d/systemd.conf
/usr/lib/tmpfiles.d/tmp.conf
/usr/lib/tmpfiles.d/var.conf
/usr/lib/tmpfiles.d/x11.conf
/usr/lib/udev/rules.d/50-udev-default.rules
/usr/lib/udev/rules.d/60-block.rules
/usr/lib/udev/rules.d/60-drm.rules
/usr/lib/udev/rules.d/60-evdev.rules
/usr/lib/udev/rules.d/60-input-id.rules
/usr/lib/udev/rules.d/60-persistent-input.rules
/usr/lib/udev/rules.d/60-persistent-storage.rules
/usr/lib/udev/rules.d/60-sensor.rules
/usr/lib/udev/rules.d/60-serial.rules
/usr/lib/udev/rules.d/64-btrfs.rules
/usr/lib/udev/rules.d/70-mouse.rules
/usr/lib/udev/rules.d/70-power-switch.rules
/usr/lib/udev/rules.d/70-touchpad.rules
/usr/lib/udev/rules.d/70-uaccess.rules
/usr/lib/udev/rules.d/71-seat.rules
/usr/lib/udev/rules.d/73-seat-late.rules
/usr/lib/udev/rules.d/75-net-description.rules
/usr/lib/udev/rules.d/80-drivers.rules
/usr/lib/udev/rules.d/80-net-setup-link.rules
/usr/lib/udev/rules.d/90-vconsole.rules
/usr/lib/udev/rules.d/99-systemd.rules

%files data
%defattr(-,root,root,-)
%exclude /usr/share/polkit-1/actions/org.freedesktop.hostname1.policy
%exclude /usr/share/polkit-1/actions/org.freedesktop.locale1.policy
%exclude /usr/share/polkit-1/actions/org.freedesktop.login1.policy
%exclude /usr/share/polkit-1/actions/org.freedesktop.machine1.policy
%exclude /usr/share/polkit-1/actions/org.freedesktop.systemd1.policy
%exclude /usr/share/polkit-1/actions/org.freedesktop.timedate1.policy
%exclude /usr/share/polkit-1/rules.d/systemd-networkd.rules
/usr/share/bash-completion/completions/bootctl
/usr/share/bash-completion/completions/busctl
/usr/share/bash-completion/completions/coredumpctl
/usr/share/bash-completion/completions/hostnamectl
/usr/share/bash-completion/completions/journalctl
/usr/share/bash-completion/completions/kernel-install
/usr/share/bash-completion/completions/localectl
/usr/share/bash-completion/completions/loginctl
/usr/share/bash-completion/completions/machinectl
/usr/share/bash-completion/completions/networkctl
/usr/share/bash-completion/completions/systemctl
/usr/share/bash-completion/completions/systemd-analyze
/usr/share/bash-completion/completions/systemd-cat
/usr/share/bash-completion/completions/systemd-cgls
/usr/share/bash-completion/completions/systemd-cgtop
/usr/share/bash-completion/completions/systemd-delta
/usr/share/bash-completion/completions/systemd-detect-virt
/usr/share/bash-completion/completions/systemd-nspawn
/usr/share/bash-completion/completions/systemd-path
/usr/share/bash-completion/completions/systemd-resolve
/usr/share/bash-completion/completions/systemd-run
/usr/share/bash-completion/completions/timedatectl
/usr/share/bash-completion/completions/udevadm
/usr/share/clr-service-restart/systemd-journald.service
/usr/share/clr-service-restart/systemd-resolved.service
/usr/share/clr-service-restart/systemd-timesyncd.service
/usr/share/clr-service-restart/systemd-udevd.service
/usr/share/dbus-1/services/org.freedesktop.systemd1.service
/usr/share/dbus-1/system-services/org.freedesktop.hostname1.service
/usr/share/dbus-1/system-services/org.freedesktop.locale1.service
/usr/share/dbus-1/system-services/org.freedesktop.login1.service
/usr/share/dbus-1/system-services/org.freedesktop.machine1.service
/usr/share/dbus-1/system-services/org.freedesktop.network1.service
/usr/share/dbus-1/system-services/org.freedesktop.resolve1.service
/usr/share/dbus-1/system-services/org.freedesktop.systemd1.service
/usr/share/dbus-1/system-services/org.freedesktop.timedate1.service
/usr/share/dbus-1/system.d/org.freedesktop.hostname1.conf
/usr/share/dbus-1/system.d/org.freedesktop.locale1.conf
/usr/share/dbus-1/system.d/org.freedesktop.login1.conf
/usr/share/dbus-1/system.d/org.freedesktop.machine1.conf
/usr/share/dbus-1/system.d/org.freedesktop.network1.conf
/usr/share/dbus-1/system.d/org.freedesktop.resolve1.conf
/usr/share/dbus-1/system.d/org.freedesktop.systemd1.conf
/usr/share/dbus-1/system.d/org.freedesktop.timedate1.conf
/usr/share/pam.d/systemd-user
/usr/share/pkgconfig/systemd.pc
/usr/share/pkgconfig/udev.pc
/usr/share/polkit-1/actions/org.freedesktop.resolve1.policy
/usr/share/systemd/kbd-model-map
/usr/share/systemd/language-fallback-map
/usr/share/zsh/site-functions/_bootctl
/usr/share/zsh/site-functions/_busctl
/usr/share/zsh/site-functions/_coredumpctl
/usr/share/zsh/site-functions/_hostnamectl
/usr/share/zsh/site-functions/_journalctl
/usr/share/zsh/site-functions/_kernel-install
/usr/share/zsh/site-functions/_localectl
/usr/share/zsh/site-functions/_loginctl
/usr/share/zsh/site-functions/_machinectl
/usr/share/zsh/site-functions/_networkctl
/usr/share/zsh/site-functions/_sd_hosts_or_user_at_host
/usr/share/zsh/site-functions/_sd_machines
/usr/share/zsh/site-functions/_sd_outputmodes
/usr/share/zsh/site-functions/_sd_unit_files
/usr/share/zsh/site-functions/_systemctl
/usr/share/zsh/site-functions/_systemd
/usr/share/zsh/site-functions/_systemd-analyze
/usr/share/zsh/site-functions/_systemd-delta
/usr/share/zsh/site-functions/_systemd-inhibit
/usr/share/zsh/site-functions/_systemd-nspawn
/usr/share/zsh/site-functions/_systemd-resolve
/usr/share/zsh/site-functions/_systemd-run
/usr/share/zsh/site-functions/_systemd-tmpfiles
/usr/share/zsh/site-functions/_timedatectl
/usr/share/zsh/site-functions/_udevadm

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/systemd/_sd-common.h
/usr/include/systemd/sd-bus-protocol.h
/usr/include/systemd/sd-bus-vtable.h
/usr/include/systemd/sd-bus.h
/usr/include/systemd/sd-daemon.h
/usr/include/systemd/sd-event.h
/usr/include/systemd/sd-id128.h
/usr/include/systemd/sd-journal.h
/usr/include/systemd/sd-login.h
/usr/include/systemd/sd-messages.h
/usr/lib64/libsystemd.so
/usr/lib64/libudev.so
/usr/lib64/pkgconfig/libsystemd.pc
/usr/lib64/pkgconfig/libudev.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsystemd.so
/usr/lib32/libudev.so
/usr/lib32/pkgconfig/32libsystemd.pc
/usr/lib32/pkgconfig/32libudev.pc
/usr/lib32/pkgconfig/libsystemd.pc
/usr/lib32/pkgconfig/libudev.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/systemd/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/systemd-hwdb
/usr/bin/systemd-sysusers
/usr/lib/systemd/system/systemd-sysusers.service
/usr/lib/systemd/system/var-lib-machines.mount
/usr/lib/udev/cdrom_id
/usr/lib/udev/collect
/usr/lib/udev/hwdb.d/20-OUI.hwdb
/usr/lib/udev/hwdb.d/20-acpi-vendor.hwdb
/usr/lib/udev/hwdb.d/20-bluetooth-vendor-product.hwdb
/usr/lib/udev/hwdb.d/20-net-ifname.hwdb
/usr/lib/udev/hwdb.d/20-pci-classes.hwdb
/usr/lib/udev/hwdb.d/20-pci-vendor-model.hwdb
/usr/lib/udev/hwdb.d/20-sdio-classes.hwdb
/usr/lib/udev/hwdb.d/20-sdio-vendor-model.hwdb
/usr/lib/udev/hwdb.d/20-usb-classes.hwdb
/usr/lib/udev/hwdb.d/60-evdev.hwdb
/usr/lib/udev/hwdb.d/60-keyboard.hwdb
/usr/lib/udev/hwdb.d/60-sensor.hwdb
/usr/lib/udev/hwdb.d/70-mouse.hwdb
/usr/lib/udev/hwdb.d/70-pointingstick.hwdb
/usr/lib/udev/hwdb.d/70-touchpad.hwdb
/usr/lib/udev/mtd_probe
/usr/lib/udev/rules.d/60-cdrom_id.rules
/usr/lib/udev/rules.d/60-persistent-alsa.rules
/usr/lib/udev/rules.d/60-persistent-storage-tape.rules
/usr/lib/udev/rules.d/60-persistent-v4l.rules
/usr/lib/udev/rules.d/70-joystick.rules
/usr/lib/udev/rules.d/75-probe_mtd.rules
/usr/lib/udev/rules.d/78-sound-card.rules
/usr/lib/udev/v4l_id
/usr/share/polkit-1/actions/org.freedesktop.hostname1.policy
/usr/share/polkit-1/actions/org.freedesktop.locale1.policy
/usr/share/polkit-1/actions/org.freedesktop.login1.policy
/usr/share/polkit-1/actions/org.freedesktop.machine1.policy
/usr/share/polkit-1/actions/org.freedesktop.systemd1.policy
/usr/share/polkit-1/actions/org.freedesktop.timedate1.policy
/usr/share/polkit-1/rules.d/systemd-networkd.rules

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnss_myhostname.so.2
/usr/lib64/libnss_mymachines.so.2
/usr/lib64/libnss_resolve.so.2
/usr/lib64/libnss_systemd.so.2
/usr/lib64/libsystemd.so.0
/usr/lib64/libsystemd.so.0.22.0
/usr/lib64/libudev.so.1
/usr/lib64/libudev.so.1.6.10
/usr/lib64/security/pam_systemd.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnss_myhostname.so.2
/usr/lib32/libnss_mymachines.so.2
/usr/lib32/libnss_resolve.so.2
/usr/lib32/libnss_systemd.so.2
/usr/lib32/libsystemd.so.0
/usr/lib32/libsystemd.so.0.22.0
/usr/lib32/libudev.so.1
/usr/lib32/libudev.so.1.6.10
/usr/lib32/security/pam_systemd.so

%files locales -f systemd.lang
%defattr(-,root,root,-)

