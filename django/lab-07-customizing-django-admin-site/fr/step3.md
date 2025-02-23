# Personnaliser la liste de modification de l'administrateur

Maintenant que la page d'administration de Question semble bonne, apportons quelques ajustements à la page "liste de modification" - celle qui affiche toutes les questions du système.

Voici à quoi elle ressemble pour l'instant :

![Polls change list page](../assets/admin04t.png)

Par défaut, Django affiche la `str()` de chaque objet. Mais parfois, il serait plus utile de pouvoir afficher des champs individuels. Pour cela, utilisez l'option d'administration `~django.contrib.admin.ModelAdmin.list_display`, qui est un tuple de noms de champs à afficher, en colonnes, sur la page de liste de modification de l'objet :

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date"]
```

Pour être sûr, ajoutons également la méthode `was_published_recently()` de `**Configurez la base de données**` :

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

Maintenant, la page de liste de modification des questions ressemble à ceci :

![Question change list view](../assets/20230908-16-14-08-GNY2lggF.png)

Vous pouvez cliquer sur les en-têtes de colonne pour trier par ces valeurs - sauf dans le cas de l'en-tête `was_published_recently`, car le tri par la sortie d'une méthode arbitraire n'est pas supporté. Notez également que l'en-tête de colonne pour `was_published_recently` est, par défaut, le nom de la méthode (avec les tirets remplacés par des espaces), et que chaque ligne contient la représentation sous forme de chaîne de la sortie.

Vous pouvez améliorer cela en utilisant le décorateur `~django.contrib.admin.display` sur cette méthode (dans `polls/models.py`), comme suit :

```python
from django.contrib import admin


class Question(models.Model):
    #...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Publié récemment?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Pour plus d'informations sur les propriétés configurables via le décorateur, consultez `~django.contrib.admin.ModelAdmin.list_display`.

Modifiez à nouveau votre fichier `polls/admin.py` et ajoutez une amélioration à la page de liste de modification de `Question` : des filtres en utilisant `~django.contrib.admin.ModelAdmin.list_filter`. Ajoutez la ligne suivante à `QuestionAdmin` :

```python
list_filter = ["pub_date"]
```

Cela ajoute une barre latérale "Filtrer" qui permet aux utilisateurs de filtrer la liste de modification par le champ `pub_date` :

![Admin list filter sidebar](../assets/20230908-16-16-39-otfMNyYo.png)

Le type de filtre affiché dépend du type de champ sur lequel vous filtrez. Comme `pub_date` est un `~django.db.models.DateTimeField`, Django sait donner des options de filtrage appropriées : "Toute date", "Aujourd'hui", "Derniers 7 jours", "Ce mois-ci", "Cette année".

Cela prend forme bien. Ajoutons une fonction de recherche :

```python
search_fields = ["question_text"]
```

Cela ajoute une zone de recherche en haut de la liste de modification. Lorsque quelqu'un entre des termes de recherche, Django cherchera dans le champ `question_text`. Vous pouvez utiliser autant de champs que vous le souhaitez - bien que, car cela utilise une requête `LIKE` en arrière-plan, limiter le nombre de champs de recherche à un nombre raisonnable facilitera la recherche dans votre base de données.

Il est également opportun de noter que les listes de modification vous donnent une pagination gratuite. La valeur par défaut est d'afficher 100 éléments par page. `Pagination des listes de modification
<django.contrib.admin.ModelAdmin.list_per_page>`, `zones de recherche
<django.contrib.admin.ModelAdmin.search_fields>`, `filtres
<django.contrib.admin.ModelAdmin.list_filter>`, `hiérarchies de dates
<django.contrib.admin.ModelAdmin.date_hierarchy>` et `tri des en-têtes de colonne <django.contrib.admin.ModelAdmin.list_display>` fonctionnent toutes ensemble comme vous le pensez.
