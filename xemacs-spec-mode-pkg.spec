Summary:	Major mode for editing RPM .spec files
Summary(pl):	Tryb g³ówny do edycji RPM-owych pliów .spec
Name:		xemacs-spec-mode-pkg
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	xemacs-pld-extras-0.21.tgz
#Source1:	http://www.xemacs.org/~stigb/rpm-spec-mode.el
Requires:	xemacs
Requires:	xemacs-pc-pkg
Requires:	xemacs-cc-mode-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
	
%description

%description -l pl

%prep
%setup  -q -c %{name}-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/spec-mode

install ./xemacs-pld-extras/rpm-spec-mode.el  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/spec-mode

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
