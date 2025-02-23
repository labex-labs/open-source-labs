# Pousser vers un registre central

Accédez à [Docker Hub](https://hub.docker.com) et créez un compte si vous n'en avez pas déjà. Alternativement, vous pouvez également utiliser [https://quay.io](https://quay.io) par exemple.

Pour ce laboratoire, nous utiliserons Docker Hub comme notre registre central. Docker Hub est un service gratuit pour stocker des images disponibles publiquement, ou vous pouvez payer pour stocker des images privées. Accédez au site web [Docker Hub](https://hub.docker.com) et créez un compte gratuit.

La plupart des organisations qui utilisent intensément Docker installeront leur propre registre en interne. Pour simplifier les choses, nous utiliserons Docker Hub, mais les concepts suivants s'appliquent à tout registre.

Connexion

Vous pouvez vous connecter au compte du registre d'images en tapant `docker login` sur votre terminal, ou si vous utilisez podman, tapez `podman login`.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<votre_nom_docker>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Mot de passe :
AVERTISSEMENT! Votre mot de passe sera stocké en clair dans /home/labex/.docker/config.json.
Configurez un assistant de credentials pour supprimer cet avertissement. Consultez
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Connexion réussie
```

Taguez votre image avec votre nom d'utilisateur

La convention de nommage de Docker Hub est de taguer votre image avec [nom d'utilisateur dockerhub]/[nom d'image]. Pour ce faire, nous allons taguer notre image `python-hello-world` précédemment créée pour qu'elle corresponde à ce format.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Poussez votre image vers le registre

Une fois que nous avons une image correctement taguée, nous pouvons utiliser la commande `docker push` pour pousser notre image vers le registre Docker Hub.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Consultez votre image sur Docker Hub dans votre navigateur

Accédez à [Docker Hub](https://hub.docker.com) et allez dans votre profil pour voir votre image nouvellement téléchargée à `https://hub.docker.com/repository/docker/<nom_dockerhub>/python-hello-world`.

Maintenant que votre image est sur Docker Hub, d'autres développeurs et opérations peuvent utiliser la commande `docker pull` pour déployer votre image dans d'autres environnements.

**Remarque** : Les images Docker contiennent toutes les dépendances dont elles ont besoin pour exécuter une application à l'intérieur de l'image. Cela est pratique car nous n'avons plus à gérer la dérive d'environnement (différences de versions) lorsque nous dépendons de dépendances installées sur chaque environnement dans lequel nous déployons. Nous n'avons pas non plus à passer par des étapes supplémentaires pour provisionner ces environnements. Juste une étape : installer Docker, et vous êtes prêt.
