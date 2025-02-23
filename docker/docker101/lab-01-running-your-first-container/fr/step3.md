# Exécutez plusieurs conteneurs

## Explorer le Docker Hub

Le [Docker Hub](https://hub.docker.com/explore/) est le registre central public pour les images Docker, qui contient des images communautaires et officielles.

Lorsque vous recherchez des images, vous trouverez des filtres pour les images "Certifiées Docker", "Éditeur vérifié" et "Images officielles". Sélectionnez le filtre "Certifiées Docker" pour trouver des images considérées prêtes pour l'entreprise et testées avec le produit Docker Enterprise Edition. Il est important d'éviter d'utiliser du contenu non vérifié du Docker Store lors du développement de vos propres images destinées à être déployées dans un environnement de production. Ces images non vérifiées peuvent contenir des vulnérabilités de sécurité ou même du logiciel malveillant.

Dans l'étape 2 de ce laboratoire, nous allons démarrer quelques conteneurs en utilisant des images vérifiées du Docker Hub : un serveur web Nginx et une base de données MongoDB.

## Exécutez un serveur Nginx

Exécutons un conteneur en utilisant l'[image officielle Nginx](https://hub.docker.com/_/nginx) du Docker Hub.

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

Nous utilisons quelques drapeaux nouveaux ici. Le drapeau `--detach` exécutera ce conteneur en arrière-plan. Le drapeau `publish` publie le port 80 dans le conteneur (le port par défaut pour Nginx), via le port 8080 sur notre hôte. Rappelez-vous que l'espace de noms NET donne aux processus du conteneur leur propre pile de réseau. Le drapeau `--publish` est une fonctionnalité qui nous permet d'exposer le réseau à travers le conteneur sur l'hôte.

Comment savez-vous que le port 80 est le port par défaut pour Nginx? Parce que cela est indiqué dans la [documentation](https://hub.docker.com/_/nginx) sur le Docker Hub. En général, la documentation des images vérifiées est très bonne, et vous voudrez vous y référer lorsque vous exécutez des conteneurs à l'aide de ces images.

Nous spécifions également le drapeau `--name`, qui nomme le conteneur. Chaque conteneur a un nom, si vous ne le spécifiez pas, Docker vous en attribuera un aléatoirement. Spécifier votre propre nom facilite l'exécution de commandes ultérieures sur votre conteneur car vous pouvez référencer le nom au lieu de l'ID du conteneur. Par exemple : `docker container inspect nginx` au lieu de `docker container inspect 5e1`.

Depuis que c'est la première fois que vous exécutez le conteneur Nginx, il téléchargera l'image Nginx du Docker Store. Les conteneurs suivants créés à partir de l'image Nginx utiliseront l'image existante située sur votre hôte.

Nginx est un serveur web léger. Vous pouvez accéder au serveur Nginx dans l'onglet **Web 8080** de la machine virtuelle LabEx. Basculez dessus et rafraîchissez la page pour voir la sortie de Nginx.

![étape 2 nginx](../assets/20230829-11-16-04-BazUogDa.png)

## Exécutez un serveur `mongo` DB

Maintenant, exécutons un serveur MongoDB. Nous utiliserons l'[image officielle MongoDB](https://hub.docker.com/_/mongo) du Docker Hub. Au lieu d'utiliser l'image `latest` (qui est la valeur par défaut si aucun tag n'est spécifié), nous utiliserons une version spécifique de l'image mongo : 4.4.

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

Encore une fois, puisque c'est la première fois que nous exécutons un conteneur mongo, nous téléchargerons l'image mongo du Docker Store. Nous utilisons le drapeau `--publish` pour exposer le port mongo 27017 sur notre hôte. Nous devons utiliser un port autre que 8080 pour la mappage hôte, car ce port est déjà exposé sur notre hôte. Consultez à nouveau la [documentation officielle](https://hub.docker.com/_/mongo) sur le Docker Hub pour obtenir plus de détails sur l'utilisation de l'image mongo.

Voyez la sortie de MongoDB en utilisant `0.0.0.0:8081` dans le navigateur web. Vous devriez voir un message qui retournera un avertissement de la part de MongoDB.

![Sortie d'avertissement du serveur MongoDB](../assets/20230829-11-19-23-PkodKK48.png)

Vérifiez vos conteneurs en cours d'exécution avec `docker container ls`

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." Il y a moins d'une seconde Up il y a 2 secondes 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." Il y a 17 secondes Up il y a 19 secondes 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" Il y a 5 minutes Up il y a 5 minutes priceless_kepler
```

Vous devriez voir qu'il existe un conteneur serveur web Nginx et un conteneur MongoDB en cours d'exécution sur votre hôte. Notez que nous n'avons pas configuré ces conteneurs pour communiquer entre eux.

Vous pouvez voir les noms "nginx" et "mongo" que nous avons donnés à nos conteneurs, et le nom aléatoire (dans mon cas "priceless_kepler") qui a été généré pour le conteneur ubuntu. Vous pouvez également voir les mappages de ports que nous avons spécifiés avec le drapeau `--publish`. Pour plus de détails sur ces conteneurs en cours d'exécution, vous pouvez utiliser la commande `docker container inspect [container id`.

Une chose que vous pourriez remarquer est que le conteneur mongo exécute la commande `docker-entrypoint`. Il s'agit du nom de l'exécutable qui est exécuté lorsque le conteneur est démarré. L'image mongo nécessite une certaine configuration préalable avant de démarrer le processus de base de données. Vous pouvez voir exactement ce que le script fait en le consultant sur [github](https://github.com/docker-library/mongo). En général, vous pouvez trouver le lien vers la source github à partir de la page de description de l'image sur le site web du Docker Store.

Les conteneurs sont autonomes et isolés, ce qui signifie que nous pouvons éviter les conflits potentiels entre les conteneurs avec différentes dépendances système ou de runtime. Par exemple : déployer une application qui utilise Java 7 et une autre application qui utilise Java 8 sur le même hôte. Ou exécuter plusieurs conteneurs Nginx qui ont tous le port 80 comme port d'écoute par défaut (si vous les exposez sur l'hôte en utilisant le drapeau `--publish`, les ports sélectionnés pour l'hôte doivent être uniques). Les avantages d'isolation sont possibles grâce aux espaces de noms Linux.

**Note** : Vous n'avez pas dû installer quoi que ce soit sur votre hôte (autre que Docker) pour exécuter ces processus! Chaque conteneur inclut les dépendances dont il a besoin à l'intérieur du conteneur, donc vous n'avez pas besoin d'installer quoi que ce soit directement sur votre hôte.

Exécuter plusieurs conteneurs sur le même hôte nous permet de tirer pleinement parti des ressources (processeur, mémoire, etc.) disponibles sur un seul hôte. Cela peut entraîner d'importantes économies de coûts pour une entreprise.

Alors que l'exécution directe d'images à partir du Docker Hub peut être utile parfois, il est plus utile de créer des images personnalisées et de se référer aux images officielles comme point de départ pour ces images. Nous plongerons dans la construction de nos propres images personnalisées dans le laboratoire 2.
