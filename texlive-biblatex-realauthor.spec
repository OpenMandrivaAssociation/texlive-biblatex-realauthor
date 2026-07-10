%global tl_name biblatex-realauthor
%global tl_revision 45865

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7.1a
Release:	%{tl_revision}.1
Summary:	Indicate the real author of a work
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-realauthor
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-realauthor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-realauthor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to use a new field "realauthor", which indicates the
real author of a work, when published in a pseudepigraphic name.

