# Créer et construire l'image Docker

Maintenant, et si vous n'avez pas Python installé localement? Ne vous inquiétez pas! Parce que vous n'en avez pas besoin. L'un des avantages d'utiliser des conteneurs est que vous pouvez installer Python dans vos conteneurs, sans avoir besoin d'installer Python sur votre machine hôte.

Créez un `Dockerfile` en exécutant la commande suivante. (Copiez/collez le bloc de code entier)

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Un Dockerfile liste les instructions nécessaires pour construire une image Docker. Passons en revue le fichier ci-dessus ligne par ligne.

**FROM python:3.8-alpine**
C'est le point de départ de votre Dockerfile. Tout Dockerfile doit commencer par une ligne `FROM` qui est l'image de départ sur laquelle vous construirez vos couches.

Dans ce cas, nous sélectionnons la couche de base `python:3.8-alpine` (voir [Dockerfile pour python3.8/alpine3.12](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)) car elle a déjà la version de Python et de pip dont nous avons besoin pour exécuter notre application.

La version `alpine` signifie qu'elle utilise la distribution [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux), qui est considérablement plus petite que de nombreuses autres variétés de Linux, environ 8 Mo de taille, tandis qu'une installation minimale sur disque peut être d'environ 130 Mo. Une image plus petite signifie qu'elle téléchargera (déployera) beaucoup plus rapidement, et elle présente également des avantages en termes de sécurité car elle a une surface d'attaque plus réduite. [Alpine Linux](https://alpinelinux.org/downloads/) est une distribution Linux basée sur musl et BusyBox.

Ici, nous utilisons l'étiquette "3.8-alpine" pour l'image Python. Consultez les étiquettes disponibles pour l'image Python officielle sur le [Docker Hub](https://hub.docker.com/_/python/). Il est recommandé de choisir une étiquette spécifique lors de l'héritage d'une image parent afin de contrôler les modifications de la dépendance parentale. Si aucune étiquette n'est spécifiée, l'étiquette "latest" prend effet, qui est un pointeur dynamique qui pointe vers la dernière version d'une image.

Pour des raisons de sécurité, il est très important de comprendre les couches sur lesquelles vous construisez votre image Docker. Pour cette raison, il est fortement recommandé d'utiliser uniquement des images "officielles" trouvées sur le [docker hub](https://hub.docker.com/), ou des images non communautaires trouvées dans le docker-store. Ces images sont [vérifiées](https://docs.docker.com/docker-hub/official_repos/) pour répondre à certaines exigences de sécurité et ont également une excellente documentation pour les utilisateurs. Vous pouvez trouver plus d'informations sur cette [image de base Python](https://hub.docker.com/_/python), ainsi que sur toutes les autres images que vous pouvez utiliser, sur le [docker hub](https://hub.docker.com).

Pour une application plus complexe, vous pouvez avoir besoin d'utiliser une image `FROM` plus haut dans la chaîne. Par exemple, le [Dockerfile parent](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) de notre application Python commence par `FROM alpine`, puis spécifie une série de commandes `CMD` et `RUN` pour l'image. Si vous aviez besoin d'un contrôle plus fin, vous pourriez commencer par `FROM alpine` (ou une autre distribution) et exécuter ces étapes vous-même. Pour commencer, je recommande d'utiliser une image officielle qui répondra le plus précisément possible à vos besoins.

**RUN pip install flask**
La commande `RUN` exécute les commandes nécessaires pour configurer votre image pour votre application, telles que l'installation de packages, l'édition de fichiers ou la modification des permissions de fichiers. Dans ce cas, nous installons flask. Les commandes `RUN` sont exécutées lors de la construction et sont ajoutées aux couches de votre image.

**CMD ["python","app.py"]**
`CMD` est la commande qui est exécutée lorsque vous lancez un conteneur. Ici, nous utilisons `CMD` pour exécuter notre application Python.

Il ne peut y avoir qu'une seule commande `CMD` par Dockerfile. Si vous spécifiez plusieurs commandes `CMD`, alors la dernière commande `CMD` entrera en vigueur. Le parent `python:3.8-alpine` spécifie également une commande `CMD` (`CMD python3`). Vous pouvez trouver le Dockerfile pour l'image officielle `python:alpine` [ici](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile).

Vous pouvez utiliser directement l'image Python officielle pour exécuter des scripts Python sans installer Python sur votre hôte. Mais aujourd'hui, nous créons une image personnalisée pour inclure notre source, afin que nous puissions construire une image avec notre application et la distribuer dans d'autres environnements.

**COPY app.py /app.py**
Ceci copie le fichier `app.py` dans le répertoire local (où vous exécuterez `docker image build`) dans une nouvelle couche de l'image. Cette instruction est la dernière ligne du Dockerfile. Les couches qui changent fréquemment, telles que la copie du code source dans l'image, devraient être placées près du bas du fichier pour profiter pleinement du cache de couches Docker. Cela nous permet d'éviter de reconstruire les couches qui pourraient autrement être mises en cache. Par exemple, si il y avait un changement dans l'instruction `FROM`, cela invaliderait le cache pour toutes les couches suivantes de cette image. Nous le démontrerons un peu plus tard dans ce laboratoire.

Il peut sembler contre-intuitif de le placer après la ligne `CMD ["python","app.py"]`. Rappelez-vous, la ligne `CMD` est exécutée seulement lorsque le conteneur est démarré, donc nous n'aurons pas d'erreur `fichier non trouvé` ici.

Et voilà : un Dockerfile très simple. Vous trouverez une liste complète des commandes que vous pouvez insérer dans un Dockerfile [ici](https://docs.docker.com/engine/reference/builder/). Maintenant que nous avons défini notre Dockerfile, utilisons-le pour construire notre image Docker personnalisée.

Construit l'image Docker.

Ajoutez `-t` pour nommer votre image `python-hello-world`.

```bash
docker image build -t python-hello-world.
```

Vérifiez que votre image apparaît dans votre liste d'images.

```bash
docker image ls
```

**Remarque** que votre image de base `python:3.8-alpine` est également dans votre liste.

Vous pouvez exécuter une commande d'historique pour afficher l'historique d'une image et de ses couches,

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
