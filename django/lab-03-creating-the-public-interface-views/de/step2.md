# Weitere Ansichten schreiben

Fügen wir nun einige weitere Ansichten zu `polls/views.py` hinzu. Diese Ansichten unterscheiden sich etwas, da sie ein Argument entgegennehmen:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Verknüpfen Sie diese neuen Ansichten mit dem `polls.urls`-Modul, indem Sie die folgenden `~django.urls.path`-Aufrufe hinzufügen:

Bearbeiten Sie die Datei `polls/urls.py` und fügen Sie die folgenden Zeilen hinzu:

```python
from django.urls import path

from. import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Führen Sie nun den Server erneut aus:

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Wechseln Sie zur Registerkarte **Web 8080** bei `/polls/34/`. Es wird die `detail()`-Methode ausgeführt und das in der URL angegebene ID angezeigt. Versuchen Sie auch `/polls/34/results/` und `/polls/34/vote/` - diese werden die Platzhalter-Resultate und Abstimmungsseiten anzeigen.

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

Wenn jemand eine Seite von Ihrer Website anfordert - sagen wir `/polls/34/`, lädt Django das Python-Modul `mysite.urls`, da es durch die Einstellung `ROOT_URLCONF` angegeben ist. Es findet die Variable `urlpatterns` und läuft die Muster in der angegebenen Reihenfolge durch. Nachdem es die Übereinstimmung bei `'polls/'` gefunden hat, entfernt es den übereinstimmenden Text (`"polls/"`) und sendet den verbleibenden Text - `"34/"` - an die URL-Konfiguration von `'polls.urls'` für weitere Verarbeitung. Dort stimmt es mit `'<int:question_id>/'` überein, was zu einem Aufruf der `detail()`-Ansicht wie folgt führt:

```python
detail(request=<HttpRequest object>, question_id=34)
```

Der Teil `question_id=34` stammt aus `<int:question_id>`. Mit Hilfe von spitzen Klammern "fangt" man einen Teil der URL und sendet ihn als Schlüsselwortargument an die Ansichtsfunktion. Der Teil `question_id` der Zeichenfolge definiert den Namen, der verwendet wird, um das übereinstimmende Muster zu identifizieren, und der Teil `int` ist ein Konverter, der bestimmt, welche Muster diesem Teil des URL-Pfads entsprechen sollten. Das Doppelpunktzeichen (`:`) trennt den Konverter und den Muster-Namen voneinander.
