# Personnaliser l'aspect de votre _application_

Tout d'abord, créez un répertoire appelé `static` dans votre répertoire `polls`. Django cherchera les fichiers statiques là, de la même manière que Django trouve les templates dans `polls/templates/`.

La configuration `STATICFILES_FINDERS` de Django contient une liste de chercheurs qui savent découvrir les fichiers statiques à partir de diverses sources. L'un des paramètres par défaut est `AppDirectoriesFinder` qui recherche un sous-répertoire "static" dans chacun des `INSTALLED_APPS`, comme celui dans `polls` que nous venons de créer. Le site d'administration utilise la même structure de répertoire pour ses fichiers statiques.

Dans le répertoire `static` que vous venez de créer, créez un autre répertoire appelé `polls` et à l'intérieur de celui-ci, créez un fichier appelé `style.css`. En d'autres termes, votre feuille de style devrait se trouver à `polls/static/polls/style.css`. En raison de la façon dont le chercheur de fichiers statiques `AppDirectoriesFinder` fonctionne, vous pouvez vous référer à ce fichier statique dans Django sous le nom `polls/style.css`, de la même manière que vous référencez le chemin des templates.

## Espaçage des noms de fichiers statiques

Comme pour les templates, nous _pourrions_ peut-être nous passer de placer nos fichiers statiques directement dans `polls/static` (au lieu de créer un autre sous-répertoire `polls`), mais ce serait en fait une mauvaise idée. Django choisira le premier fichier statique qu'il trouvera dont le nom correspond, et si vous aviez un fichier statique avec le même nom dans une _autre_ application, Django ne serait pas capable de les distinguer. Nous devons être en mesure de pointer Django sur le bon fichier, et le meilleur moyen de s'assurer de cela est de les _espacer_. C'est-à-dire, en plaçant ces fichiers statiques à l'intérieur d'un _autre_ répertoire nommé pour l'application elle-même.

Placez le code suivant dans cette feuille de style (`polls/static/polls/style.css`):

```css
li a {
  color: green;
}
```

Ensuite, ajoutez le code suivant en haut de `polls/templates/polls/index.html`:

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

La balise de modèle `{% static %}` génère l'URL absolue des fichiers statiques.

Voilà tout ce que vous avez besoin de faire pour le développement.

Démarrez le serveur (ou le redémarrez s'il est déjà en cours d'exécution):

```bash
python manage.py runserver 0.0.0.0:8080
```

Rechargez l'onglet **Web 8080** et vous devriez voir que les liens de questions sont verts (style Django!) ce qui signifie que votre feuille de style a été correctement chargée.

![exemple de liens de questions verts](../assets/20230908-15-29-11-ztyI1umP.png)
