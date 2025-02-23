# Erste Schritte

Öffnen Sie ein Terminal auf der LabEx VM und führen Sie `docker -h` aus, um die Hilfeseite für die Docker-Befehlszeilenschnittstelle (CLI) anzuzeigen.

```bash
$ docker -h
Flag shorthand -h has been deprecated, please use --help

Usage: docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

...

Management Commands:
builder Manage builds
config Manage Docker configs
container Manage containers
engine Manage the docker engine
image Manage images
network Manage networks
node Manage Swarm nodes
plugin Manage plugins
secret Manage Docker secrets
service Manage services
stack Manage Docker stacks
swarm Manage Swarm
system Manage Docker
trust Manage trust on Docker images
volume Manage volumes
```

Die Docker-Befehlszeilenschnittstelle kann verwendet werden, um mehrere Funktionen des Docker-Engines zu verwalten. In diesem Lab werden wir uns hauptsächlich auf den `container`-Befehl konzentrieren.

Installieren Sie `podman` auf Ihrer LabEx VM.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

Wenn `podman` installiert ist, können Sie den alternativen Befehl ausführen, um ihn zu vergleichen.

```bash
sudo podman -h
```

Sie können zusätzlich die Version Ihrer Docker-Installation mit `docker version` überprüfen

```bash
docker version

Client:
Version: 20.10.21
...

Server:
Engine:
Version: 20.10.21
...
```

Sie stellen fest, dass Docker sowohl einen `Client` als auch einen `Server: Docker Engine` installiert. Wenn Sie beispielsweise den gleichen Befehl für podman ausführen, werden Sie nur eine CLI-Version sehen, da podman daemonlos läuft und auf eine OCI-kompatible Containerlaufzeit (runc, crun, runv etc.) zurückgreift, um mit dem Betriebssystem zu interagieren und die laufenden Container zu erstellen.

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
