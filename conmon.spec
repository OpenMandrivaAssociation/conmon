%undefine _debugsource_packages

Name: conmon
Version: 2.1.12
Release: 1
Source0: https://github.com/containers/conmon/archive/refs/tags/v%{version}.tar.gz
Summary: Tool for monitoring OCI containers and pods
URL: https://github.com/containers/conmon
License: Apache-2.0
Group: Servers
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(systemd)

%description
Conmon is a monitoring program and communication tool between a container
manager (like Podman or CRI-O) and an OCI runtime (like runc or crun) for
a single container.

Upon being launched, conmon (usually) double-forks to daemonize and detach
from the parent that launched it. It then launches the runtime as its child.
This allows managing processes to die in the foreground, but still be able
to watch over and connect to the child process (the container).

While the container runs, conmon does two things:

* Provides a socket for attaching to the container, holding open the
  container's standard streams and forwarding them over the socket.
* Writes the contents of the container's streams to a log file (or to
  the systemd journal) so they can be read after the container's death.
  p
Finally, upon the containers death, conmon will record its exit time and code
to be read by the managing programs.

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/conmon
%{_mandir}/man8/conmon.8*
