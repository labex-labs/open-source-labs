# Écrivez votre première vue

Écrivons la première vue. Ouvrez le fichier `polls/views.py` et mettez le code Python suivant dedans :

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

C'est la vue la plus simple possible en Django. Pour appeler la vue, nous devons la mapper à une URL - et pour cela, nous avons besoin d'une configuration d'URL (URLconf).

Pour créer une URLconf dans le répertoire polls, créez un fichier appelé `urls.py`. Votre structure de répertoires d'application devrait maintenant ressembler à ceci :

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

Dans le fichier `polls/urls.py`, incluez le code suivant :

```python
from django.urls import path

from. import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

L'étape suivante consiste à pointer la configuration d'URL racine vers le module `polls.urls`. Dans `mysite/urls.py`, ajoutez une importation pour `django.urls.include` et insérez un `~django.urls.include` dans la liste `urlpatterns`, de sorte que vous obtenez :

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

La fonction `~django.urls.include` permet de référencer d'autres configurations d'URL.每当 Django 遇到 `~django.urls.include` 时，它会截断到该点为止匹配的 URL 的任何部分，并将剩余的字符串发送到包含的 URLconf 进行进一步处理。

L'idée derrière `~django.urls.include` est de faciliter l'utilisation des URLs en les connectant facilement. Étant donné que les sondages sont dans leur propre configuration d'URL (`polls/urls.py`), ils peuvent être placés sous "/polls/", ou sous "/fun_polls/", ou sous "/content/polls/", ou n'importe quel autre chemin racine, et l'application fonctionnera toujours.

> Quand utiliser `~django.urls.include()`
> Vous devriez toujours utiliser `include()` lorsque vous incluez d'autres modèles d'URL. `admin.site.urls` est l'unique exception à cela.

Vous avez maintenant connecté une vue `index` à la configuration d'URL. Vérifiez que cela fonctionne avec la commande suivante :

```bash
python manage.py runserver 0.0.0.0:8080
```

Accédez à <http://<url>/polls/> dans votre navigateur, et vous devriez voir le texte "_Hello, world. You're at the polls index._", que vous avez défini dans la vue `index`.

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

La fonction `~django.urls.path` est passée quatre arguments, deux requis : `route` et `view`, et deux optionnels : `kwargs` et `name`. À ce stade, il est utile de réviser à quoi servent ces arguments.

## Argument `~django.urls.path` : `route`

`route` est une chaîne de caractères qui contient un modèle d'URL. Lorsqu'il traite une requête, Django commence par le premier modèle dans `urlpatterns` et parcourt la liste, comparant l'URL demandée avec chaque modèle jusqu'à ce qu'il trouve un qui correspond.

Les modèles ne cherchent pas les paramètres GET et POST, ni le nom de domaine. Par exemple, dans une requête à `https://www.example.com/myapp/`, la configuration d'URL cherchera `myapp/`. Dans une requête à `https://www.example.com/myapp/?page=3`, la configuration d'URL cherchera également `myapp/`.

## Argument `~django.urls.path` : `view`

Lorsque Django trouve un modèle correspondant, il appelle la fonction de vue spécifiée avec un objet `~django.http.HttpRequest` en tant que premier argument et toutes les valeurs "capturées" à partir de la route en tant qu'arguments nommés. Nous donnerons un exemple de cela un peu plus loin.

## Argument `~django.urls.path` : `kwargs`

Des arguments nommés arbitraires peuvent être passés dans un dictionnaire à la vue cible. Nous n'allons pas utiliser cette fonctionnalité de Django dans le tutoriel.

## Argument `~django.urls.path` : `name`

Donner un nom à votre URL vous permet de vous y référer de manière non ambiguë d'autres parties de Django, en particulier à partir de templates. Cette fonction puissante vous permet de modifier globalement les modèles d'URL de votre projet tout en ne touchant qu'un seul fichier.
