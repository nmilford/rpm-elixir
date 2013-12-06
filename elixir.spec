# To Build:
#
# sudo yum -y install rpmdevtools erlang && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-elixir/master/elixir.spec -O ~/rpmbuild/SPECS/elixir.spec
# wget https://github.com/elixir-lang/elixir/archive/v0.11.2.tar.gz -O  ~/rpmbuild/SOURCES/v0.11.2.tar.gz
# rpmbuild -bb ~/rpmbuild/SPECS/elixir.spec

Name:      elixir
Version:   0.11.2
Release:   1
Summary:   The Elixir programming language for the Erlang VM.
License:   Apache 2.0
URL:       http://elixir-lang.org/
Group:     Development/Languages
Source0:   https://github.com/elixir-lang/elixir/archive/v%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Nathan Milford <nathan@milford.io>
BuildRequires: erlang
Requires: erlang

%description
Elixir is a functional, meta-programming aware language built on top of the
Erlang VM. It is a dynamic language with flexible syntax and macro support that
leverages Erlang's abilities to build concurrent, distributed and
fault-tolerant applications with hot code upgrades.


%prep
%setup -n %{name}-%{version}

%build
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/lib/elixir/*
/usr/local/bin/*
/usr/lib/elixir/*
/usr/bin/*


%changelog
* Fri Dec 06 2013 Nathan Milford <nathan@milford.io> 0.11.2-1
- bumped version.
* Sun Aug 04 2013 Nathan Milford <nathan@milford.io> 0.10.1-1
- Initial spec
