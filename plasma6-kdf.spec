Name:		plasma6-kdf
Summary:	View free disk space
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kdf
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdf-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Core5Compat)

%description
KDiskFree displays the available file devices (hard drive partitions,
floppy and CD/DVD drives, etc.) along with information on their capacity,
free space, type and mount point. It also allows you to mount and unmount
drives and view them in a file manager.

%files -f kdf.lang -f kcontrol.lang
%{_datadir}/qlogging-categories6/*.categories
%{_bindir}/kdf
%{_bindir}/kwikdisk
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.kdf.appdata.xml
%{_iconsdir}/*/*/*/*.png
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kdf.so

%libpackage kdfprivate %(echo %{version} |cut -d. -f1)
#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdf-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdf --with-html
%find_lang kcontrol --with-html
