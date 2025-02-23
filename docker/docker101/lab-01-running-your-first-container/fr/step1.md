# Commencez

Ouvrez un terminal sur la machine virtuelle LabEx et exécutez `docker -h`, qui vous montrera la page d'aide de l'interface de ligne de commande (CLI) Docker.

```bash
$ docker -h
Le raccourci d'option -h est obsolète, veuillez utiliser --help

Usage: docker [OPTIONS] COMMAND

Un runtime autonome pour les conteneurs

...

Commandes de gestion :
builder Gérer les builds
config Gérer les configurations Docker
container Gérer les conteneurs
engine Gérer le moteur Docker
image Gérer les images
network Gérer les réseaux
node Gérer les nœuds Swarm
plugin Gérer les plugins
secret Gérer les secrets Docker
service Gérer les services
stack Gérer les piles Docker
swarm Gérer Swarm
system Gérer Docker
trust Gérer la confiance sur les images Docker
volume Gérer les volumes
```

La ligne de commande Docker peut être utilisée pour gérer plusieurs fonctionnalités du moteur Docker. Dans ce laboratoire, nous nous concentrerons principalement sur la commande `container`.

Installez `podman` sur votre machine virtuelle LabEx.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

Si `podman` est installé, vous pouvez exécuter la commande alternative pour comparer.

```bash
sudo podman -h
```

Vous pouvez également vérifier la version de votre installation Docker avec `docker version`

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

Vous constatez que Docker installe à la fois un `Client` et un `Server : Docker Engine`. Par exemple, si vous exécutez la même commande pour podman, vous ne verrez que la version de la CLI, car podman s'exécute sans démon et dépend d'un runtime de conteneur conforme à OCI (runc, crun, runv, etc.) pour interfacer avec le système d'exploitation et créer les conteneurs en cours d'exécution.

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
