%define		_class		PEAR
%define		_subclass	PackageFileManager_GUI_Gtk
%define		_status		stable
%define		_pearname	PEAR_PackageFileManager_GUI_Gtk

Summary:	%{_pearname} - A PHP-GTK frontend for the PEAR_PackageFileManager class
Summary(pl.UTF-8):	%{_pearname} - Frontend PHP-GTK do klasy PEAR_PackageFileManager
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2f2951f0b9f4fc3d2cb3b37bb1592588
URL:		http://pear.php.net/package/PEAR_PackageFileManager_GUI_Gtk/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Gtk_FileDrop >= 0.1.0
Requires:	php-pear-PEAR >= 1:1.3.5
Requires:	php-pear-PEAR_PackageFileManager >= 1.5.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP-GTK 1 frontend for the PEAR_PackageFileManager class. It makes
it easier for developers to create and maintain PEAR package.xml
files.

Features:
- Update existing package files or create new ones
- Import values from an existing package file
- Drag-n-Drop package directory into the application for easy loading
- Set package level information (package name, description, etc.)
- Set release level information (version, release notes, etc.)
- Easily add maintainers
- Browse package files as a tree and click to add a dependency
- Add install time global and file replacements
- Package file preview window
- Package the package using the new package file

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Frontend PHP-GTK1 do klasy PEAR_PackageFileManager. Ułatwia
developerom tworzenie i opiekę nad plikami package.xml.

Możliwości:
- aktualizacja istniejących lub tworzenie nowych plików package.xml,
- import ustawień z istniejących plików,
- przeciągnij-i-upuść katalog do okna aplikacji celem wczytania
  informacji,
- określanie informacji o pakiecie (nazwa, opis, itp.),
- określanie informacji o wydaniu (wersja, wydanie, itp.),
- łatwe dodawanie opiekunów,
- przeglądanie plików w postaci drzewa oraz możliwość dodania
  zależności przez kliknięcie,
- dodawanie globalnych oraz lokalnych zastąpień w plikach na etapie
  instalacji,
- okno podglądu pakietu,
- tworzenie pakietu przy użyciu nowego pliku package.xml.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/PEAR/PackageFileManager/GUI
%{php_pear_dir}/PEAR/PackageFileManager/GUI/Gtk.php
