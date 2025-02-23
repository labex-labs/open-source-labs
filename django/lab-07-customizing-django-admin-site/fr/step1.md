# Personnaliser le formulaire d'administration

En enregistrant le modèle `Question` avec `admin.site.register(Question)`, Django a été capable de construire une représentation de formulaire par défaut. Souvent, vous voudrez personnaliser l'apparence et le fonctionnement du formulaire d'administration. Vous le ferez en informant Django des options que vous souhaitez lorsque vous enregistrez l'objet.

Voyons comment cela fonctionne en réordonnant les champs du formulaire d'édition. Remplacez la ligne `admin.site.register(Question)` par :

Modifiez le fichier `~/project/mysite/polls/admin.py` pour qu'il ressemble à ceci :

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

Vous suivrez ce modèle - créer une classe d'administration de modèle, puis la passer en tant que deuxième argument à `admin.site.register()` - chaque fois que vous devrez changer les options d'administration pour un modèle.

Exécutez le serveur de développement Django :

```bash
cd ~/project/mysite
python manage.py runserver
```

Ouvrez `http://127.0.0.1:8000/admin/` dans Firefox de l'environnement de bureau et cliquez sur le lien "Questions". Vous devriez voir un formulaire qui ressemble à ceci.

Ce changement particulier ci-dessus fait en sorte que la "Date de publication" soit avant le champ "Question" :

![Admin form field reorder](../assets/20230908-16-06-41-wiBfnHS8.png)

Cela n'est pas impressionnant avec seulement deux champs, mais pour les formulaires d'administration avec des dizaines de champs, choisir un ordre intuitif est un détail d'ergonomie important.

Et parlant de formulaires avec des dizaines de champs, vous pouvez vouloir diviser le formulaire en groupes de champs :

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Informations de date", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

Le premier élément de chaque tuple dans `~django.contrib.admin.ModelAdmin.fieldsets` est le titre du groupe de champs. Voici à quoi ressemble maintenant notre formulaire :

![Admin form with fieldsets](../assets/20230908-16-08-19-HOzMJWFG.png)
