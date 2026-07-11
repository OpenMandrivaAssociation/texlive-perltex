%global tl_name perltex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Define LaTeX macros in terms of Perl code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/perltex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perltex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(perltex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PerlTeX is a combination Perl script (perltex.pl) and LaTeX2e package
(perltex.sty) that, together, give the user the ability to define LaTeX
macros in terms of Perl code. Once defined, a Perl macro becomes
indistinguishable from any other LaTeX macro. PerlTeX thereby combines
LaTeX's typesetting power with Perl's programmability. PerlTeX will make
use of persistent named pipes, and thereby run more efficiently, on
operating systems that offer them (mostly Unix-like systems). Also
provided is a switch to generate a PerlTeX-free, document-specific,
noperltex.sty that is useful when distributing a document to places
where PerlTeX is not available.

