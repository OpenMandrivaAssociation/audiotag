Summary:	Command-line tool for mass tagging/renaming of audio files
Name:	audiotag
Version:	0.19
Release:	2
License:	GPLv2+
Group:	Sound
Url:	https://github.com/Daenyth/audiotag
Source0:	https://github.com/Daenyth/audiotag/archive/refs/tags/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	atomicparsley
Requires:	flac
Requires:	id3lib

%description
Audiotag is a command-line tool for mass tagging/renaming of audio files.

%files
%doc COPYING README ChangeLog
%{_bindir}/%{name}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Perl script: nothing to do


%install
# Go manually
mkdir -p %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}/%{name}
