# [Optionnel] OverlayFS

OverlayFS est une implémentation de `union mount filesystem` pour Linux. Pour comprendre ce qu'est un volume Docker, il est utile de comprendre comment les couches et le système de fichiers fonctionnent dans Docker.

Pour démarrer un conteneur, Docker prend l'image en lecture seule et crée une nouvelle couche en lecture-écriture au-dessus. Pour visualiser les couches comme une seule, Docker utilise un système de fichiers Union ou OverlayFS (Overlay File System), plus précisément le pilote de stockage `overlay2`.

Pour voir les fichiers gérés par l'hôte Docker, vous avez besoin d'accéder au système de fichiers du processus Docker. En utilisant les drapeaux `--privilégié` et `--pid=host`, vous pouvez accéder à l'espace de noms d'identifiant de processus de l'hôte depuis l'intérieur d'un conteneur comme `busybox`. Vous pouvez ensuite naviguer vers le répertoire `/var/lib/docker/overlay2` de Docker pour voir les couches téléchargées qui sont gérées par Docker.

Pour afficher la liste actuelle des couches dans Docker :

```bash
$ docker run -it --privilégié --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

Téléchargez l'image `ubuntu` et vérifiez à nouveau :

```bash
docker pull ubuntu
docker run -it --privilégié --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

Tapez la commande pour voir à nouveau la liste des couches :

```
ls -l /var/lib/docker/overlay2/ & exit
```

Vous voyez que le téléchargement de l'image `ubuntu` a implicitement téléchargé 4 nouvelles couches :

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

Le pilote de stockage `overlay2` combine en fait différents répertoires sur l'hôte et les présente comme un seul répertoire.

- couche de base ou lowerdir,
- couche `diff` ou upperdir,
- couche d'overlay (vue de l'utilisateur), et
- répertoire `work`.

OverlayFS réfère aux répertoires inférieurs comme `lowerdir`, qui contient l'image de base et les couches en lecture seule (R/O) qui sont téléchargées.

Le répertoire supérieur est appelé `upperdir` et est la couche de conteneur en lecture-écriture (R/W).

La vue unifiée ou couche `overlay` est appelée `merged`.

Enfin, un `workdir` est requis, qui est un répertoire vide utilisé par overlay pour son utilisation interne.

Le pilote `overlay2` prend en charge jusqu'à 128 couches OverlayFS inférieures. Le répertoire `l` contient des identifiants de couche raccourcis sous forme de liens symboliques.

![Overlay2 Storage Driver](../assets/overlay2-driver.png)

Nettoyage :

```bash
docker system prune -a
clear
```
