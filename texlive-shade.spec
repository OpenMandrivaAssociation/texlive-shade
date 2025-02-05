Name:		texlive-shade
Version:	22212
Release:	2
Summary:	Shade pieces of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/shade
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shade.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shade.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a shaded backdrop to a box of text. It
uses a Metafont font (provided) which generates to appropriate
shading dependent on the resolution used in the Metafont
printer parameters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/shade/shade.mf
%{_texmfdistdir}/tex/generic/shade/shade.tex
%doc %{_texmfdistdir}/doc/generic/shade/README
%doc %{_texmfdistdir}/doc/generic/shade/description.pdf
%doc %{_texmfdistdir}/doc/generic/shade/description.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
