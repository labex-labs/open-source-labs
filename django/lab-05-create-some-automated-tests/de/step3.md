# Schreiben unseres ersten Tests

## Wir identifizieren einen Bug

Zum Glück gibt es in der `Umfrage`-Anwendung einen kleinen Bug, den wir sofort beheben können: Die Methode `Question.was_published_recently()` gibt `True` zurück, wenn die `Question` innerhalb des letzten Tages veröffentlicht wurde (was korrekt ist), aber auch wenn das `pub_date`-Feld der `Question` in der Zukunft liegt (was sicherlich nicht der Fall ist).

Bestätigen Sie den Bug, indem Sie die `shell` verwenden, um die Methode für eine Frage zu überprüfen, deren Datum in der Zukunft liegt:

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # Erstellen Sie eine Question-Instanz mit pub_date 30 Tage in der Zukunft
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # Wurde sie kürzlich veröffentlicht?
>>> future_question.was_published_recently()
True
```

Da Dinge in der Zukunft nicht „kürzlich“ sind, ist dies eindeutig falsch.

## Erstellen eines Tests, um den Bug aufzudecken

Was wir gerade in der `shell` getan haben, um das Problem zu testen, können wir genauso in einem automatisierten Test tun. Lassen Sie uns daher das in einen automatisierten Test umwandeln.

Ein üblicher Ort für die Tests einer Anwendung ist die `tests.py`-Datei der Anwendung; das Testsystem findet automatisch Tests in jeder Datei, deren Name mit `test` beginnt.

Fügen Sie Folgendes in die `tests.py`-Datei in der `Umfrage`-Anwendung hinzu:

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() gibt False für Fragen zurück, deren pub_date
        in der Zukunft liegt.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Hier haben wir eine Unterklasse von `django.test.TestCase` erstellt, die eine Methode enthält, die eine `Question`-Instanz mit einem `pub_date` in der Zukunft erstellt. Wir überprüfen dann die Ausgabe von `was_published_recently()` – die _sollte_ `False` sein.

## Ausführen von Tests

Im Terminal können wir unseren Test ausführen:

```bash
python manage.py test polls
```

und Sie werden etwas wie Folgendes sehen:

```shell

```

> Anderer Fehler?

Wenn Sie hier stattdessen einen `NameError` erhalten, haben Sie vielleicht einen Schritt in `Teil 2 <tutorial02-import-timezone>` übersehen, in dem wir die Imports von `datetime` und `timezone` in `polls/models.py` hinzugefügt haben. Kopieren Sie die Imports aus diesem Abschnitt und versuchen Sie, Ihre Tests erneut auszuführen.

Was passiert ist Folgendes:

- `manage.py test polls` suchte nach Tests in der `Umfrage`-Anwendung
- es fand eine Unterklasse der `django.test.TestCase`-Klasse
- es erstellte eine spezielle Datenbank zum Zwecke des Tests
- es suchte nach Testmethoden – solchen, deren Namen mit `test` beginnen
- in `test_was_published_recently_with_future_question` erstellte es eine `Question`-Instanz, deren `pub_date`-Feld 30 Tage in der Zukunft ist
  -... und mit der `assertIs()`-Methode stellte es fest, dass ihre `was_published_recently()` `True` zurückgibt, obwohl wir wollten, dass sie `False` zurückgibt

Der Test informiert uns, welcher Test fehlgeschlagen ist und sogar die Zeile, an der der Fehler aufgetreten ist.

## Beheben des Bugs

Wir wissen bereits, was das Problem ist: `Question.was_published_recently()` sollte `False` zurückgeben, wenn sein `pub_date` in der Zukunft liegt. Ändern Sie die Methode in `models.py`, sodass sie nur `True` zurückgibt, wenn das Datum auch in der Vergangenheit liegt:

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

und führen Sie den Test erneut aus:

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

Nachdem wir einen Bug identifiziert haben, haben wir einen Test geschrieben, der ihn aufdeckt, und den Bug im Code korrigiert, sodass unser Test bestanden wird.

In Zukunft könnten viele andere Dinge mit unserer Anwendung schiefgehen, aber wir können sicher sein, dass wir diesen Bug nicht versehentlich wieder einführen, da das Ausführen des Tests uns sofort warnen wird. Wir können diese kleine Teilmenge der Anwendung als sicher für immer betrachten.

## Umfassendere Tests

Während wir hier sind, können wir die Methode `was_published_recently()` weiter festlegen; tatsächlich wäre es eher peinlich, wenn wir bei der Behebung eines Bugs einen anderen eingeführt hätten.

Fügen Sie zwei weitere Testmethoden zur gleichen Klasse hinzu, um das Verhalten der Methode umfassender zu testen:

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() gibt False für Fragen zurück, deren pub_date
    älter als 1 Tag ist.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() gibt True für Fragen zurück, deren pub_date
    innerhalb des letzten Tages liegt.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

Und jetzt haben wir drei Tests, die bestätigen, dass `Question.was_published_recently()` sinnvolle Werte für vergangene, aktuelle und zukünftige Fragen zurückgibt.

Wiederum ist `Umfrage` eine minimale Anwendung, aber wie komplex auch immer sie in Zukunft wird und mit welchen anderen Code sie interagiert, wir haben jetzt die Gewähr, dass die Methode, für die wir Tests geschrieben haben, wie erwartet verhalten wird.
