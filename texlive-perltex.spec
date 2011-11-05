# revision 19702
# category Package
# catalog-ctan /macros/latex/contrib/perltex
# catalog-date 2010-07-24 23:20:00 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-perltex
Version:	2.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_texmfdir}/doc/man/man1/perltex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/latex/perltex/perltex.dtx
%doc %{_texmfdistdir}/source/latex/perltex/perltex.ins
%doc %{_tlpkgobjdir}/*.tlpobj

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
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
