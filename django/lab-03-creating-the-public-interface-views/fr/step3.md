# Écrire des vues qui font réellement quelque chose

Chaque vue est responsable de faire l'une des deux choses suivantes : renvoyer un objet `~django.http.HttpResponse` contenant le contenu de la page demandée, ou lever une exception telle que `~django.http.Http404`. Le reste est à vous.

Votre vue peut lire des enregistrements dans une base de données, ou pas. Elle peut utiliser un système de gabarit tel que celui de Django - ou un système de gabarit Python tiers - ou pas. Elle peut générer un fichier PDF, produire un XML, créer un fichier ZIP sur le vol, tout ce que vous voulez, en utilisant les bibliothèques Python que vous voulez.

Tout ce que Django veut, c'est cet objet `~django.http.HttpResponse`. Ou une exception.

Par commodité, utilisons l'API de base de données de Django, que nous avons abordée dans le tutoriel 2. Voici une tentative pour une nouvelle vue `index()`, qui affiche les 5 dernières questions de sondage dans le système, séparées par des virgules, selon la date de publication :

Modifiez le fichier `polls/views.py` et changez-le pour qu'il ressemble à ceci :

```python
from django.http import HttpResponse

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Laissez les autres vues (detail, results, vote) inchangées
```

Il y a cependant un problème ici : la conception de la page est codée en dur dans la vue. Si vous voulez changer la façon dont la page se présente, vous devrez modifier ce code Python. Alors, utilisons le système de gabarit de Django pour séparer la conception du Python en créant un gabarit que la vue peut utiliser.

Tout d'abord, créez un répertoire appelé `templates` dans votre répertoire `polls`. Django cherchera les gabarits là-dedans.

La configuration `TEMPLATES` de votre projet décrit la manière dont Django chargera et affichera les gabarits. Le fichier de configuration par défaut configure un backend `DjangoTemplates` dont l'option `APP_DIRS <TEMPLATES-APP_DIRS>` est définie sur `True`. Par convention, `DjangoTemplates` cherche un sous-répertoire "templates" dans chacun des `INSTALLED_APPS`.

Dans le répertoire `templates` que vous venez de créer, créez un autre répertoire appelé `polls`, et à l'intérieur de celui-ci, créez un fichier appelé `index.html`. En d'autres termes, votre gabarit devrait se trouver à `polls/templates/polls/index.html`. En raison de la façon dont le chargeur de gabarits `app_directories` fonctionne comme décrit ci-dessus, vous pouvez vous référer à ce gabarit dans Django sous le nom `polls/index.html`.

## Espacage des noms de gabarit

Maintenant, nous _pourrions_ peut-être nous en sortir en mettant nos gabarits directement dans `polls/templates` (au lieu de créer un autre sous-répertoire `polls`), mais ce serait en fait une mauvaise idée. Django choisira le premier gabarit qu'il trouvera dont le nom correspond, et si vous aviez un gabarit avec le même nom dans une _autre_ application, Django ne serait pas capable de les distinguer.

Nous devons être en mesure de pointer Django vers le bon gabarit, et le meilleur moyen de s'assurer de cela est en les _espacant_. C'est-à-dire en mettant ces gabarits à l'intérieur d'un _autre_ répertoire nommé pour l'application elle-même.

Placez le code suivant dans ce gabarit :

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Remarque :

Pour que le tutoriel soit plus court, tous les exemples de gabarit utilisent un HTML incomplet. Dans vos propres projets, vous devriez utiliser [des documents HTML complets](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document).

Maintenant, mettons à jour notre vue `index` dans `polls/views.py` pour utiliser le gabarit :

```python
from django.http import HttpResponse
from django.template import loader

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

Ce code charge le gabarit appelé `polls/index.html` et lui passe un contexte. Le contexte est un dictionnaire qui associe les noms de variables de gabarit à des objets Python.

Exécutez le serveur à nouveau :

```bash
python manage.py runserver 0.0.0.0:8080
```

Chargez la page en pointant votre navigateur vers "/polls/", et vous devriez voir une liste à puces contenant la question "What's up" du tutoriel 2. Le lien pointe vers la page de détail de la question.

![Django polls index page](../assets/20230908-09-37-26-QMKEbUhb.png)

## Un raccourci : `~django.shortcuts.render`

C'est un usage très courant de charger un gabarit, de remplir un contexte et de renvoyer un objet `~django.http.HttpResponse` avec le résultat du gabarit affiché. Django propose un raccourci. Voici la vue complète `index()`, réécrite :

```python
from django.shortcuts import render

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Notez qu'une fois que nous l'avons fait dans toutes ces vues, nous n'avons plus besoin d'importer `~django.template.loader` et `~django.http.HttpResponse` (vous voudrez conserver `HttpResponse` si vous avez encore les méthodes d'esquisses pour `detail`, `results` et `vote`).

La fonction `~django.shortcuts.render` prend l'objet de requête comme premier argument, le nom du gabarit comme deuxième argument et un dictionnaire comme troisième argument optionnel. Elle renvoie un objet `~django.http.HttpResponse` du gabarit donné affiché avec le contexte donné.
