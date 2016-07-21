Name:		kdf
Summary:	View free disk space
Version:	16.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kdf
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

%description
KDiskFree displays the available file devices (hard drive partitions,
floppy and CD/DVD drives, etc.) along with information on their capacity,
free space, type and mount point. It also allows you to mount and unmount
drives and view them in a file manager.

%files
%{_kde_appsdir}/kdf
%{_kde_bindir}/kdf
%{_kde_bindir}/kwikdisk
%{_kde_libdir}/kde4/kcm_kdf.so
%{_kde_iconsdir}/*/*/apps/kcmdf.*
%{_kde_iconsdir}/*/*/apps/kdf.*
%{_kde_iconsdir}/*/*/apps/kwikdisk.*
%{_kde_applicationsdir}/kdf.desktop
%{_kde_applicationsdir}/kwikdisk.desktop
%{_kde_services}/kcmdf.desktop
%{_kde_docdir}/HTML/*/kdf
%{_kde_docdir}/HTML/*/kcontrol/blockdevices

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

