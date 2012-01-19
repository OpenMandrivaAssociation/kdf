Name:    kdf
Summary: View free disk space
Version: 4.8.0
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL:     http://utils.kde.org/projects/%name
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2

BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KDiskFree displays the available file devices (hard drive partitions,
floppy and CD/DVD drives, etc.) along with information on their capacity,
free space, type and mount point. It also allows you to mount and unmount
drives and view them in a file manager.

%files
%_kde_appsdir/kdf
%_kde_bindir/kdf
%_kde_bindir/kwikdisk
%_kde_libdir/kde4/kcm_kdf.so
%_kde_iconsdir/*/*/apps/kcmdf.*
%_kde_iconsdir/*/*/apps/kdf.*
%_kde_iconsdir/*/*/apps/kwikdisk.*
%_kde_datadir/applications/kde4/kdf.desktop
%_kde_datadir/applications/kde4/kwikdisk.desktop
%_kde_datadir/kde4/services/kcmdf.desktop
%_kde_docdir/HTML/*/kdf
%_kde_docdir/HTML/*/kcontrol/blockdevices

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

