Name: qtapplication
Version: 0.0.1
Release: alt1

Summary: Minimal Qt Application
Summary(ru_RU.UTF-8): Минимальное Qt приложение

License: LGPLv3+
Group: Education
Url: https://github.com/boringplace/qtapplication

Source: %name-%version.tar

%description
Minimal graphical Qt application building with cmake

%description -l ru_RU.UTF-8
Минимальное графическое Qt приложение сосбираемое с с помощью cmake

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%changelog
* Mon Apr 20 2020 Valery Sinelnikov <greh@altlinux.org> 0.0.1-alt1
- Initial first build of application

