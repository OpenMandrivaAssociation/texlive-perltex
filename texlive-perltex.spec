# revision 32576
# category Package
# catalog-ctan /macros/latex/contrib/perltex
# catalog-date 2012-06-12 18:08:23 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-perltex
Version:	2.1
Release:	12
Summary:	Define LaTeX macros in terms of Perl code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/perltex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-perltex.bin = %{EVRD}

%description
PerlTeX is a combination Perl script (perltex.pl) and LaTeX2e
package (perltex.sty) that, together, give the user the ability
to define LaTeX macros in terms of Perl code. Once defined, a
Perl macro becomes indistinguishable from any other LaTeX
macro. PerlTeX thereby combines LaTeX's typesetting power with
Perl's programmability. PerlTeX will make use of persistent
named pipes, and thereby run more efficiently, on operating
systems that offer them (mostly Unix-like systems). Also
provided is a switch to generate a PerlTeX-free, document-
specific, noperltex.sty that is useful when distributing a
document to places where PerlTeX is not available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/perltex
%{_texmfdistdir}/scripts/perltex/perltex.pl
%{_texmfdistdir}/tex/latex/perltex/perltex.sty
%doc %{_texmfdistdir}/doc/latex/perltex/README
%doc %{_texmfdistdir}/doc/latex/perltex/example.tex
%doc %{_texmfdistdir}/doc/latex/perltex/perltex.pdf
%doc %{_mandir}/man1/perltex.1*
%doc %{_texmfdistdir}/doc/man/man1/perltex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/latex/perltex/perltex.dtx
%doc %{_texmfdistdir}/source/latex/perltex/perltex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/perltex/perltex.pl perltex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
