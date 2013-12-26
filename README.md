rpm-elixir
==========

An RPM spec file to build the Elixir programming language for the Erlang VM.

To Build:

`sudo yum -y install rpmdevtools erlang && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-elixir/master/elixir.spec -O ~/rpmbuild/SPECS/elixir.spec`

`wget https://github.com/elixir-lang/elixir/archive/v0.12.0.tar.gz -O  ~/rpmbuild/SOURCES/v0.12.0.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/elixir.spec`
