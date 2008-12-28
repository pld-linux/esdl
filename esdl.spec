# TODO:
# - CFLAGS
Summary:	SDL and OpenGL functionality for erlang programs
Name:		esdl
Version:	0.96.0626
Release:	0.2
License:	BSD-like
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/esdl/%{name}-%{version}.src.tar.gz
# Source0-md5:	5007750ddd989319442e8e040db3b6dd
URL:		http://esdl.sourceforge.net/
BuildRequires:	erlang
BuildRequires:	SDL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ESDL is library that gives you access to SDL and Opengl functionality in your
erlang program. SDL handles 2d graphics, user events and audio while Opengl
handles 3d graphics.

%prep
%setup -q

%build
%{__make} \
	GL_LIBS="-lGL -lGLU"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html license.terms Readme
%{_libdir}/erlang/lib/%{name}
