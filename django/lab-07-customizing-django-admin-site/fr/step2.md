# Ajout d'objets liés

Tout va bien, nous avons notre page d'administration de Question, mais une `Question` a plusieurs `Choice`, et la page d'administration ne montre pas les choix.

Pour l'instant.

Il existe deux manières de résoudre ce problème. La première consiste à enregistrer `Choice` auprès de l'administrateur tout comme nous l'avons fait avec `Question` :

```python
from django.contrib import admin

from.models import Choice, Question

#...
admin.site.register(Choice)
```

Maintenant, "Choix" est une option disponible dans l'administrateur Django. Le formulaire "Ajouter un choix" ressemble à ceci :

![Add Choice form interface](../assets/20230908-16-09-57-eCXIdjZu.png)

Dans ce formulaire, le champ "Question" est une liste déroulante contenant toutes les questions de la base de données. Django sait qu'une `~django.db.models.ForeignKey` devrait être représentée dans l'administrateur sous forme d'une liste `<select>`. Dans notre cas, il n'existe qu'une question pour le moment.

Notez également le lien "Ajouter une autre question" à côté de "Question". Tout objet ayant une relation `ForeignKey` avec un autre en bénéficie gratuitement. Lorsque vous cliquez sur "Ajouter une autre question", vous obtiendrez une fenêtre pop-up avec le formulaire "Ajouter une question". Si vous ajoutez une question dans cette fenêtre et cliquez sur "Enregistrer", Django enregistrera la question dans la base de données et l'ajoutera dynamiquement comme choix sélectionné dans le formulaire "Ajouter un choix" que vous êtes en train de consulter.

Mais, en réalité, c'est une manière inefficace d'ajouter des objets `Choice` au système. Il serait préférable de pouvoir ajouter plusieurs Choix directement lorsque vous créez l'objet `Question`. Voyons comment faire.

Supprimez l'appel `register()` pour le modèle `Choice`. Ensuite, modifiez le code d'enregistrement de `Question` pour qu'il ressemble à ceci :

```python
from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Informations de date", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

Cela indique à Django : "Les objets `Choice` sont édités sur la page d'administration de `Question`. Par défaut, fournissez suffisamment de champs pour 3 choix."

Chargez la page "Ajouter une question" pour voir à quoi cela ressemble :

![Question admin with choices](../assets/20230908-16-11-09-tVqaXrGB.png)

Le fonctionnement est le suivant : Il y a trois emplacements pour les Choix liés - comme spécifié par `extra` - et chaque fois que vous revenez sur la page "Modifier" pour un objet déjà créé, vous obtenez trois emplacements supplémentaires.

À la fin des trois emplacements actuels, vous trouverez un lien "Ajouter un autre Choix". Si vous cliquez dessus, un nouvel emplacement sera ajouté. Si vous voulez supprimer l'emplacement ajouté, vous pouvez cliquer sur la croix en haut à droite de l'emplacement ajouté. Cette image montre un emplacement ajouté :

![Additional slot added dynamically](../assets/admin14t.png)

Cependant, un petit problème subsiste. Il faut beaucoup d'espace sur l'écran pour afficher tous les champs pour entrer les objets `Choice` liés. Pour cette raison, Django propose une manière tabulaire d'afficher les objets liés en ligne. Pour l'utiliser, modifiez la déclaration `ChoiceInline` pour qu'elle ressemble à ceci :

```python
class ChoiceInline(admin.TabularInline):
  ...
```

Avec cette `TabularInline` (au lieu de `StackedInline`), les objets liés sont affichés dans un format plus compact, basé sur un tableau :

![Tabular inline choices display](../assets/20230908-16-12-24-1nqRkbAI.png)

Notez qu'il y a une colonne supplémentaire "Supprimer?" qui permet de supprimer les lignes ajoutées en utilisant le bouton "Ajouter un autre Choix" et les lignes qui ont déjà été enregistrées.
