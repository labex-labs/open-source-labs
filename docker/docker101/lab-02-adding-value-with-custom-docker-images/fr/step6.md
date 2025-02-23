# Comprendre les couches d'image

L'une des principales propriétés de conception de Docker est son utilisation du système de fichiers union.

Considérez le `Dockerfile` que nous avons créé précédemment :

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

Chacune de ces lignes est une couche. Chaque couche contient uniquement le delta, la différence ou les modifications par rapport aux couches précédentes. Pour assembler ces couches en un seul conteneur en cours d'exécution, Docker utilise le `système de fichiers union` pour superposer les couches de manière transparente en une seule vue.

Chaque couche de l'image est `en lecture seule`, sauf la couche la plus haute qui est créée pour le conteneur en cours d'exécution. La couche de conteneur en lecture/écriture implémente le "copier lors de l'écriture", ce qui signifie que les fichiers stockés dans les couches d'image inférieures sont extraits jusqu'à la couche de conteneur en lecture/écriture seulement lorsqu'il y a des modifications apportées à ces fichiers. Ces modifications sont ensuite stockées dans la couche de conteneur en cours d'exécution. La fonction "copier lors de l'écriture" est très rapide et, dans presque tous les cas, n'a pas d'effet notable sur les performances. Vous pouvez examiner quels fichiers ont été extraits jusqu'au niveau du conteneur avec la commande `docker diff`. Plus d'informations sur la façon d'utiliser `docker diff` peuvent être trouvées [ici](https://docs.docker.com/engine/reference/commandline/diff/).

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

Depuis les couches d'image sont `en lecture seule`, elles peuvent être partagées par des images et par des conteneurs en cours d'exécution. Par exemple, créer une nouvelle application Python avec son propre Dockerfile avec des couches de base similaires, partagera toutes les couches qu'elle avait en commun avec la première application Python.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

Vous pouvez également ressentir le partage des couches lorsque vous lancez plusieurs conteneurs à partir de la même image. Étant donné que les conteneurs utilisent les mêmes couches en lecture seule, vous pouvez imaginer que le lancement de conteneurs est très rapide et a une empreinte très faible sur l'hôte.

Vous pouvez remarquer qu'il y a des lignes dupliquées dans ce Dockerfile et dans le Dockerfile que vous avez créé plus tôt dans ce laboratoire. Bien que ce soit un exemple très simple, vous pouvez extraire les lignes communes de ces deux Dockerfiles dans un Dockerfile "de base", que vous pouvez ensuite pointer avec chacun de vos Dockerfiles enfants en utilisant la commande `FROM`.

La stratification d'image active le mécanisme de mise en cache Docker pour les builds et les poussées. Par exemple, la sortie de votre dernière commande `docker push` montre que certaines des couches de votre image existent déjà sur Docker Hub.

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

Pour examiner plus attentivement les couches, vous pouvez utiliser la commande `docker image history` de l'image Python que nous avons créée.

```bash
$ docker image history python-hello-world
```

Chaque ligne représente une couche de l'image. Vous remarquerez que les lignes supérieures correspondent à votre Dockerfile que vous avez créé, et les lignes suivantes sont extraites de l'image Python parent. Ne vous inquiétez pas des étiquettes "\<missing\>". Ce sont toujours des couches normales ; elles n'ont simplement pas été attribuées un ID par le système Docker.
