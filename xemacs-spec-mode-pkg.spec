Summary:	Major mode for editing RPM .spec files
Summary(pl):	Tryb g³ówny do edycji RPM-owych plików .spec
Name:		xemacs-spec-mode-pkg
Version:	0.09
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	%{name}-%{version}.tar.gz
#Source1:	http://www.xemacs.org/~stigb/rpm-spec-mode.el
Requires:	xemacs
Requires:	xemacs-pc-pkg
Requires:	xemacs-cc-mode-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Major mode for editing RPM .spec files.

%description -l pl
Tryb g³ówny do edycji RPM-owych plików .spec.

%prep
%setup  -q -c %{name}-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/spec-mode

install rpm-spec-mode.el  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/spec-mode

cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/spec-mode/auto-autoloads.el
(autoload 'rpm-spec-mode "rpm-spec-mode.el" "RPM spec mode." t)
(setq auto-mode-alist (append '(("\\\\.spec" . rpm-spec-mode))
                                auto-mode-alist))

(add-hook 'rpm-spec-mode-hook 'turn-on-font-lock)
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*
