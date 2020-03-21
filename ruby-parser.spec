#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	parser
Summary:	A Ruby parser written in pure Ruby
Name:		ruby-%{pkgname}
Version:	2.5.1.2
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	f94bfd2b3efeabb109ad86a6210a0140
URL:		http://github.com/whitequark/parser
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.2
BuildRequires:	ruby-cliver < 0.4
BuildRequires:	ruby-cliver >= 0.3.0
BuildRequires:	ruby-coveralls
BuildRequires:	ruby-gauntlet
BuildRequires:	ruby-json_pure
BuildRequires:	ruby-kramdown
BuildRequires:	ruby-mime-types < 2
BuildRequires:	ruby-mime-types >= 1.25
BuildRequires:	ruby-minitest < 6
BuildRequires:	ruby-minitest >= 5.0
BuildRequires:	ruby-racc = 1.4.9
BuildRequires:	ruby-rake < 1
BuildRequires:	ruby-rake >= 0.9
BuildRequires:	ruby-simplecov < 1
BuildRequires:	ruby-simplecov >= 0.7
BuildRequires:	ruby-simplecov-sublime-ruby-coverage
BuildRequires:	ruby-yard
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Ruby parser written in pure Ruby.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ruby-parse
%attr(755,root,root) %{_bindir}/ruby-rewrite
%{ruby_vendorlibdir}/parser.rb
%{ruby_vendorlibdir}/parser
%{ruby_vendorlibdir}/gauntlet_parser.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
