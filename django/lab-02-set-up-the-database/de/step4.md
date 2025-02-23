# Mit der API experimentieren

Lassen Sie uns nun in die interaktive Python-Shell springen und mit der kostenlosen API experimentieren, die Ihnen Django zur Verfügung stellt. Um die Python-Shell aufzurufen, verwenden Sie diesen Befehl:

```bash
python manage.py shell
```

Wir verwenden dies anstelle von einfach "python" zu tippen, weil `manage.py` die Umgebungsvariable `DJANGO_SETTINGS_MODULE` setzt, die Django den Python-Importpfad zu Ihrer `mysite/settings.py`-Datei gibt.

Sobald Sie in der Shell sind, erkunden Sie die `Datenbank-API </topics/db/queries>`:

```python
>>> from polls.models import Choice, Question  # Importieren Sie die Modellklassen, die wir gerade geschrieben haben.

# Es sind noch keine Fragen im System.
>>> Question.objects.all()
<QuerySet []>

# Erstellen Sie eine neue Frage.
# Die Unterstützung für Zeitzonen ist in der Standard-Einstellungsdatei aktiviert, so dass
# Django ein Datum und Uhrzeit mit Zeitzone für pub_date erwartet. Verwenden Sie timezone.now()
# anstelle von datetime.datetime.now() und es wird das Richtige tun.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Speichern Sie das Objekt in der Datenbank. Sie müssen save() explizit aufrufen.
>>> q.save()

# Jetzt hat es eine ID.
>>> q.id
1

# Greifen Sie auf die Modellfeldwerte über Python-Attribute zu.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# Ändern Sie die Werte, indem Sie die Attribute ändern und dann save() aufrufen.
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() zeigt alle Fragen in der Datenbank an.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Warten Sie einen Moment. `<Question: Question object (1)>` ist keine hilfreiche Darstellung dieses Objekts. Lassen Sie uns das beheben, indem wir das `Question`-Modell (in der Datei `polls/models.py`) bearbeiten und eine `~django.db.models.Model.__str__`-Methode zu `Question` und `Choice` hinzufügen:

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

Es ist wichtig, `~django.db.models.Model.__str__`-Methoden zu Ihren Modellen hinzuzufügen, nicht nur für Ihre eigene Bequemlichkeit, wenn Sie mit dem interaktiven Prompt arbeiten, sondern auch, weil die Darstellungen von Objekten in der gesamten automatisch generierten Django-Admin verwendet werden.

Lassen Sie uns auch eine benutzerdefinierte Methode zu diesem Modell hinzufügen:

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Beachten Sie die Hinzufügung von `import datetime` und `from django.utils import timezone`, um auf das standardmäßige Python-`datetime`-Modul und die Zeitzonenbezogenen Hilfsprogramme von Django in `django.utils.timezone` zu verweisen. Wenn Sie nicht vertraut mit der Zeitzonenbehandlung in Python sind, können Sie mehr in den `Zeitzonenunterstützungsdokumentationen </topics/i18n/timezones>` lernen.

Speichern Sie diese Änderungen und starten Sie eine neue Python-interaktive Shell, indem Sie **erneut `python manage.py shell` ausführen**:

```python
>>> from polls.models import Choice, Question

# Stellen Sie sicher, dass unsere __str__()-Hinzufügung funktioniert.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django bietet eine umfangreiche Datenbank-Such-API, die vollständig durch
# Schlüsselwortargumente gesteuert wird.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Holen Sie sich die Frage, die dieses Jahr veröffentlicht wurde.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Fordern Sie eine ID an, die nicht existiert, dies wird eine Ausnahme auslösen.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Question matching query does not exist.

# Das Suchen nach einem Primärschlüssel ist der häufigste Fall, daher bietet Django eine
# Abkürzung für exakte Primärschlüssel-Suchen.
# Folgendes ist identisch zu Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Stellen Sie sicher, dass unsere benutzerdefinierte Methode funktioniert.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Geben Sie der Question ein paar Choices. Der create-Aufruf konstruiert ein neues
# Choice-Objekt, führt die INSERT-Anweisung aus, fügt die Wahl der Menge der verfügbaren
# Wahlen hinzu und gibt das neue Choice-Objekt zurück. Django erstellt
# eine Menge, um die "andere Seite" einer ForeignKey-Beziehung
# (z.B. die Wahl einer Frage) zu speichern, die über die API abgerufen werden kann.
>>> q = Question.objects.get(pk=1)

# Zeigen Sie alle Choices aus der zugehörigen Objektmenge an - bisher keine.
>>> q.choice_set.all()
<QuerySet []>

# Erstellen Sie drei Choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice-Objekte haben API-Zugang zu ihren zugehörigen Question-Objekten.
>>> c.question
<Question: What's up?>

# Und umgekehrt: Question-Objekte haben Zugang zu Choice-Objekten.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# Die API folgt automatisch Beziehungen, soweit Sie es benötigen.
# Verwenden Sie doppelte Unterstriche, um Beziehungen zu trennen.
# Dies funktioniert so tief wie Sie möchten; es gibt keine Grenze.
# Finden Sie alle Choices für jede Frage, deren pub_date in diesem Jahr ist
# (verwenden Sie die zuvor erstellte 'current_year'-Variable).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Lassen Sie uns eine der Choices löschen. Verwenden Sie dafür delete().
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

Weitere Informationen zu Modellbeziehungen finden Sie unter `Zugreifen auf verwandte Objekte
</ref/models/relations>`. Weitere Informationen zu Verwendung von doppelten Unterstrichen zur Durchführung von Feldsuche über die API finden Sie unter `Feldsuche <field-lookups-intro>`. Vollständige Details zur Datenbank-API finden Sie in unserer `Datenbank-API-Referenz
</topics/db/queries>`.
