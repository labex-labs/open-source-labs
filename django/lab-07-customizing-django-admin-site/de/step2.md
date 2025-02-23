# Hinzufügen von verknüpften Objekten

Okay, wir haben unsere Frage-Admin-Seite, aber eine `Frage` hat mehrere `Wahlmöglichkeiten`, und die Admin-Seite zeigt die Wahlmöglichkeiten nicht an.

Noch nicht.

Es gibt zwei Möglichkeiten, dieses Problem zu lösen. Die erste besteht darin, `Wahlmöglichkeit` wie bei `Frage` bei der Admin zu registrieren:

```python
from django.contrib import admin

from.models import Choice, Question

#...
admin.site.register(Choice)
```

Jetzt ist "Wahlmöglichkeiten" eine verfügbare Option im Django-Admin. Das Formular "Wahlmöglichkeit hinzufügen" sieht so aus:

![Add Choice form interface](../assets/20230908-16-09-57-eCXIdjZu.png)

In diesem Formular ist das Feld "Frage" ein Auswahlkästchen, das jede Frage in der Datenbank enthält. Django weiß, dass eine `~django.db.models.ForeignKey` im Admin als `<select>`-Kästchen dargestellt werden sollte. Im Moment existiert hier nur eine Frage.

Beachten Sie auch den Link "Eine weitere Frage hinzufügen" neben "Frage". Jedes Objekt mit einer `ForeignKey`-Beziehung zu einem anderen bekommt diesen kostenlos. Wenn Sie auf "Eine weitere Frage hinzufügen" klicken, erhalten Sie ein Popup-Fenster mit dem Formular "Frage hinzufügen". Wenn Sie in diesem Fenster eine Frage hinzufügen und auf "Speichern" klicken, speichert Django die Frage in der Datenbank und fügt sie dynamisch als ausgewählte Wahlmöglichkeit auf dem Formular "Wahlmöglichkeit hinzufügen" hinzu, das Sie betrachten.

Allerdings ist dies auf Dauer eine ineffiziente Weise, `Wahlmöglichkeit`-Objekte zum System hinzuzufügen. Es wäre besser, wenn Sie eine Reihe von Wahlmöglichkeiten direkt hinzufügen könnten, wenn Sie das `Frage`-Objekt erstellen. Machen wir das möglich.

Entfernen Sie den `register()`-Aufruf für das `Wahlmöglichkeit`-Modell. Anschließend bearbeiten Sie den Registrierungs-Code für `Frage` wie folgt:

```python
from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

Dies sagt Django: "`Wahlmöglichkeit`-Objekte werden auf der Frage-Admin-Seite bearbeitet. Standardmäßig werden genug Felder für 3 Wahlmöglichkeiten bereitgestellt."

Laden Sie die Seite "Frage hinzufügen", um zu sehen, wie das aussieht:

![Question admin with choices](../assets/20230908-16-11-09-tVqaXrGB.png)

Es funktioniert so: Es gibt drei Plätze für verknüpfte Wahlmöglichkeiten - wie durch `extra` angegeben - und jedes Mal, wenn Sie zur "Ändern"-Seite für ein bereits erstelltes Objekt zurückkehren, erhalten Sie weitere drei zusätzliche Plätze.

Am Ende der drei aktuellen Plätze finden Sie einen Link "Eine weitere Wahlmöglichkeit hinzufügen". Wenn Sie darauf klicken, wird ein neuer Platz hinzugefügt. Wenn Sie den hinzugefügten Platz entfernen möchten, können Sie auf das X oben rechts im hinzugefügten Platz klicken. Dieses Bild zeigt einen hinzugefügten Platz:

![Additional slot added dynamically](../assets/admin14t.png)

Es gibt jedoch ein kleines Problem. Es benötigt viel Bildschirmplatz, um alle Felder für das Eingeben von verknüpften `Wahlmöglichkeit`-Objekten anzuzeigen. Aus diesem Grund bietet Django eine tabellarische Möglichkeit, inline-verknüpfte Objekte anzuzeigen. Um sie zu verwenden, ändern Sie die `ChoiceInline`-Deklaration wie folgt:

```python
class ChoiceInline(admin.TabularInline):
 ...
```

Mit dieser `TabularInline` (anstelle von `StackedInline`) werden die verknüpften Objekte in einem kompakteren, tabellenbasierten Format angezeigt:

![Tabular inline choices display](../assets/20230908-16-12-24-1nqRkbAI.png)

Beachten Sie, dass es eine zusätzliche Spalte "Löschen?" gibt, die es ermöglicht, Zeilen zu entfernen, die mit der Schaltfläche "Eine weitere Wahlmöglichkeit hinzufügen" hinzugefügt wurden, sowie Zeilen, die bereits gespeichert wurden.
