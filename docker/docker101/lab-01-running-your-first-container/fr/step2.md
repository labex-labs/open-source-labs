# Exécutez votre premier conteneur

Nous allons utiliser l'interface de ligne de commande (CLI) Docker pour exécuter notre premier conteneur.

Ouvrez un terminal sur la machine virtuelle LabEx.

Exécutez la commande.

```bash
docker container run -t ubuntu top
```

Utilisez la commande `docker container run` pour exécuter un conteneur avec l'image `ubuntu` en utilisant la commande `top`. Le drapeau `-t` attribue un pseudo-terminal TTY dont nous avons besoin pour que `top` fonctionne correctement.

```bash
$ docker container run -it ubuntu top
Impossible de trouver l'image 'ubuntu:latest' localement
latest: Téléchargement depuis la bibliothèque/ubuntu
aafe6b5e13de: Téléchargement terminé
0a2b43a72660: Téléchargement terminé
18bdd1e546d2: Téléchargement terminé
8198342c3e05: Téléchargement terminé
f56970a44fd4: Téléchargement terminé
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Statut: Téléchargé une image plus récente pour ubuntu:latest
```

La commande `docker run` entraînera tout d'abord un `docker pull` pour télécharger l'image ubuntu sur votre hôte. Une fois téléchargée, elle démarrera le conteneur. La sortie du conteneur en cours d'exécution devrait ressembler à ceci :

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` est une utilité Linux qui affiche les processus sur un système et les classe par consommation de ressources. Remarquez qu'il n'y a qu'un seul processus dans cette sortie : c'est le processus `top` lui-même. Nous ne voyons pas les autres processus de notre hôte dans cette liste en raison de l'isolation de l'espace de noms PID.

Les conteneurs utilisent les espaces de noms Linux pour isoler les ressources système des autres conteneurs ou de l'hôte. L'espace de noms PID fournit une isolation pour les identifiants de processus. Si vous exécutez `top` à l'intérieur du conteneur, vous remarquerez qu'il affiche les processus à l'intérieur de l'espace de noms PID du conteneur, ce qui est très différent de ce que vous pouvez voir si vous exécutez `top` sur l'hôte.

Même si nous utilisons l'image `ubuntu`, il est important de noter que notre conteneur n'a pas son propre noyau. Il utilise le noyau de l'hôte et l'image `ubuntu` est utilisée uniquement pour fournir le système de fichiers et les outils disponibles sur un système ubuntu.

Inspectez le conteneur avec `docker container exec`

La commande `docker container exec` est un moyen d'"entrer" dans les espaces de noms d'un conteneur en cours d'exécution avec un nouveau processus.

Ouvrez un nouveau terminal. Sélectionnez `Terminal` > `Nouveau terminal`.

Dans le nouveau terminal, utilisez la commande `docker container ls` pour obtenir l'ID du conteneur en cours d'exécution que vous venez de créer.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

Ensuite, utilisez cet ID pour exécuter `bash` à l'intérieur de ce conteneur en utilisant la commande `docker container exec`. Puisque nous utilisons bash et que nous voulons interagir avec ce conteneur à partir de notre terminal, utilisez les drapeaux `-it` pour exécuter en mode interactif tout en attribuant un pseudo-terminal.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

Et voilà! Nous venons d'utiliser la commande `docker container exec` pour "entrer" dans les espaces de noms de notre conteneur avec notre processus bash. Utiliser `docker container exec` avec `bash` est un modèle courant pour inspecter un conteneur Docker.

Remarquez le changement dans le préfixe de votre terminal. Par exemple, `root@b3ad2a23fab3:/`. Cela indique que nous exécutons bash "à l'intérieur" de notre conteneur.

**Note** : Ce n'est pas la même chose que d'accéder à un hôte ou à une machine virtuelle séparée via ssh. Nous n'avons pas besoin d'un serveur ssh pour nous connecter à un processus bash. Rappelez-vous que les conteneurs utilisent des fonctionnalités au niveau du noyau pour réaliser l'isolation et que les conteneurs s'exécutent au-dessus du noyau. Notre conteneur n'est qu'un groupe de processus s'exécutant en isolation sur le même hôte, et nous pouvons utiliser `docker container exec` pour entrer dans cette isolation avec le processus `bash`. Après avoir exécuté `docker container exec`, le groupe de processus s'exécutant en isolation (c'est-à-dire notre conteneur) inclut `top` et `bash`.

Depuis le même terminal, exécutez `ps -ef` pour inspecter les processus en cours d'exécution.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

Vous devriez voir seulement le processus `top`, le processus `bash` et notre processus `ps`.

Pour comparer, quittez le conteneur et exécutez `ps -ef` ou `top` sur l'hôte. Ces commandes fonctionneront sur Linux ou Mac. Pour Windows, vous pouvez inspecter les processus en cours d'exécution à l'aide de `tasklist`.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Beaucoup de processus!
```

_Recherche technique approfondie_
PID n'est qu'un des espaces de noms Linux qui fournissent aux conteneurs une isolation des ressources système. Les autres espaces de noms Linux incluent :

- MNT - Monter et démonter des répertoires sans affecter les autres espaces de noms
- NET - Les conteneurs ont leur propre pile de réseau
- IPC - Mécanismes de communication interprocessus isolés tels que les files d'attente de messages.
- User - Vue isolée des utilisateurs sur le système
- UTC - Définir le nom d'hôte et le nom de domaine par conteneur

Ces espaces de noms fournissent ensemble l'isolation pour les conteneurs qui leur permettent de s'exécuter ensemble de manière sécurisée et sans conflit avec d'autres conteneurs s'exécutant sur le même système. Ensuite, nous démontrerons différentes utilisations des conteneurs et l'avantage de l'isolation lorsque nous exécutons plusieurs conteneurs sur le même hôte.

**Note** : Les espaces de noms sont une fonctionnalité du **Linux** noyau. Mais Docker vous permet d'exécuter des conteneurs sur Windows et Mac... Comment cela fonctionne-t-il? Le secret est qu'il est intégré dans le produit Docker ou le moteur Docker un sous-système Linux. Docker a open-sourcé ce sous-système Linux dans un nouveau projet : [LinuxKit](https://github.com/linuxkit/linuxkit). Être capable d'exécuter des conteneurs sur de nombreux plateformes différentes est un avantage de l'utilisation de l'outil Docker avec des conteneurs.

En plus de l'exécution de conteneurs Linux sur Windows en utilisant un sous-système Linux, les conteneurs natifs Windows sont désormais possibles grâce à la création de primitives de conteneurs sur le système d'exploitation Windows. Les conteneurs natifs Windows peuvent être exécutés sur Windows 10 ou Windows Server 2016 ou versions ultérieures.

**Note** : si vous exécutez cet exercice dans un terminal conteneurisé et exécutez la commande `ps -ef` dans le terminal, vous verrez toujours un ensemble limité de processus après avoir quitté la commande `exec`. Vous pouvez essayer d'exécuter la commande `ps -ef` dans un terminal sur votre machine locale pour voir tous les processus.

Nettoyez le conteneur exécutant les processus `top` en appuyant sur : `<ctrl>-c`, liste tous les conteneurs et supprimez les conteneurs par leur ID.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
