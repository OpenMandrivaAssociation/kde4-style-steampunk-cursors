Summary:	"SteampunK Powered Linux" mouse cursors theme
Name:		kde4-style-steampunk-cursors
Version:	3.0
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=161001
Source0:	http://kde-look.org/CONTENT/content-files/161001-SteampunK.tar.gz
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" mouse cursors.

%files
%{_iconsdir}/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644
find . -type d | xargs chmod 0755

%build
# nothing

%install
mkdir -p %{buildroot}%{_iconsdir}

cp -r SteampunK %{buildroot}%{_iconsdir}/

