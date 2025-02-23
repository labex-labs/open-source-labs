# Déploiement d'un changement

L'application "hello world!" est surestimée, mettons à jour l'application pour qu'elle dise "Hello Beautiful World!" à la place.

## Mettre à jour `app.py`

Remplacez la chaîne "Hello World" par "Hello Beautiful World!" dans `app.py`. Vous pouvez mettre à jour le fichier avec la commande suivante. (Copiez/collez le bloc de code entier)

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## Rebuild and Push Your Image

Maintenant que votre application est mise à jour, vous devez répéter les étapes ci-dessus pour reconstruire votre application et la pousser vers le registre Docker Hub.

Tout d'abord, reconstruisez, cette fois-ci utilisez votre nom d'utilisateur Docker Hub dans la commande de construction :

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world.
```

Remarquez "Using cache" pour les étapes 1-3. Ces couches de l'image Docker ont déjà été construites et `docker image build` utilisera ces couches à partir du cache au lieu de les reconstruire.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Il existe également un mécanisme de mise en cache pour pousser les couches. Docker Hub a déjà toutes les couches sauf une d'un push antérieur, donc il ne pousse que la couche qui a changé.

Lorsque vous modifiez une couche, toutes les couches construites au-dessus de celle-ci devront être reconstruites. Chaque ligne dans un Dockerfile construit une nouvelle couche qui est construite sur la couche créée à partir des lignes précédentes. C'est pourquoi l'ordre des lignes dans notre Dockerfile est important. Nous avons optimisé notre Dockerfile de sorte que la couche la plus susceptible de changer (`COPY app.py /app.py`) soit la dernière ligne du Dockerfile. Généralement pour une application, vos modifications de code sont les plus fréquentes. Cette optimisation est particulièrement importante pour les processus CI/CD, où vous voulez que votre automatisation s'exécute le plus rapidement possible.
