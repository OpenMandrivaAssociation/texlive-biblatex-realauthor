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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to use a new field "realauthor", which indicates the
real author of a work, when published in a pseudepigraphic name.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-realauthor
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/biblatex-realauthor.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/biblatex-realauthor.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/example-realauthor.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/example-realauthor.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/example-realauthor.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-realauthor/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-realauthor/realauthor.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-realauthor/realauthor.dbx
