# spec is based on MIB work

Name:		audiotag
Version:	0.19
Release:	2
Summary:	Command-line tool for mass tagging/renaming of audio files
License:	GPLv2
Group:		Sound
URL:		https://github.com/Daenyth/audiotag
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	id3lib
Requires:	flac
Requires:	atomicparsley

%description
Audiotag is a command-line tool for mass tagging/renaming of audio files.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_bindir}
%__install -m755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,)
%doc COPYING README ChangeLog
%{_bindir}/%{name}



%changelog
* Fri Feb 17 2012 Andrey Bondrov <abondrov@mandriva.org> 0.19-1
+ Revision: 776003
- imported package audiotag

