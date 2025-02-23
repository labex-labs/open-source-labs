# Anpassen des Admin-Formulars

Durch die Registrierung des `Question`-Modells mit `admin.site.register(Question)` konnte Django eine Standardformdarstellung erstellen. Oft möchten Sie anpassen, wie das Admin-Formular aussieht und funktioniert. Sie tun dies, indem Sie Django die Optionen mitteilen, die Sie möchten, wenn Sie das Objekt registrieren.

Schauen wir, wie dies funktioniert, indem wir die Felder im Bearbeitungsformular neu anordnen. Ersetzen Sie die Zeile `admin.site.register(Question)` durch:

Bearbeiten Sie die Datei `~/project/mysite/polls/admin.py`, so dass sie wie folgt aussieht:

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

Sie werden dieses Muster befolgen - erstellen Sie eine ModelAdmin-Klasse und übergeben Sie sie als zweites Argument an `admin.site.register()` - jedes Mal, wenn Sie die Admin-Optionen für ein Modell ändern müssen.

Starten Sie den Django-Entwicklungsserver:

```bash
cd ~/project/mysite
python manage.py runserver
```

Öffnen Sie `http://127.0.0.1:8000/admin/` in Firefox des Desktop-Umgebungs und klicken Sie auf den Link "Fragen". Sie sollten ein Formular sehen, das wie folgt aussieht.

Dieser spezifische Änderung oben bewirkt, dass das "Veröffentlichungsdatum" vor dem Feld "Frage" erscheint:

![Admin form field reorder](../assets/20230908-16-06-41-wiBfnHS8.png)

Dies ist mit nur zwei Feldern nicht beeindruckend, aber für Admin-Formulare mit mehreren Dutzend Feldern ist die Auswahl einer intuitiven Reihenfolge ein wichtiger Usability-Detail.

Und wenn es um Formulare mit mehreren Dutzend Feldern geht, möchten Sie vielleicht das Formular in Feldergruppen unterteilen:

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

Das erste Element jedes Tuples in `~django.contrib.admin.ModelAdmin.fieldsets` ist der Titel der Feldgruppe. So sieht unser Formular jetzt aus:

![Admin form with fieldsets](../assets/20230908-16-08-19-HOzMJWFG.png)
