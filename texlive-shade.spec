# revision 22212
# category Package
# catalog-ctan /macros/generic/shade
# catalog-date 2011-04-25 22:01:30 +0200
# catalog-license lppl1
# catalog-version 1
Name:		texlive-shade
Version:	1
Release:	1
Summary:	Shade pieces of text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/shade
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shade.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shade.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a shaded backdrop to a box of text. It
uses a Metafont font (provided) which generates to appropriate
shading dependent on the resolution used in the Metafont
printer parameters.

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
%{_texmfdistdir}/fonts/source/public/shade/shade.mf
%{_texmfdistdir}/tex/generic/shade/shade.tex
%doc %{_texmfdistdir}/doc/generic/shade/README
%doc %{_texmfdistdir}/doc/generic/shade/description.pdf
%doc %{_texmfdistdir}/doc/generic/shade/description.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
