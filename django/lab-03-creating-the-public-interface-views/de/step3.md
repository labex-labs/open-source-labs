# Ansichten schreiben, die tatsächlich etwas tun

Jede Ansicht ist für eine der beiden folgenden Aufgaben verantwortlich: entweder einen `~django.http.HttpResponse`-Objekt zurückzugeben, das den Inhalt der angeforderten Seite enthält, oder eine Ausnahme wie `~django.http.Http404` zu werfen. Der Rest liegt an Ihnen.

Ihre Ansicht kann Datenbankaufzeichnungen lesen oder auch nicht. Sie kann ein Template-System wie das von Django verwenden - oder ein Drittanbieter-Python-Template-System - oder auch nicht. Sie kann eine PDF-Datei generieren, XML ausgeben, eine ZIP-Datei im Lauf der Zeit erstellen, alles, was Sie möchten, mit beliebigen Python-Bibliotheken, die Sie möchten.

Alles, was Django will, ist dieses `~django.http.HttpResponse`. Oder eine Ausnahme.

Damit es praktisch ist, verwenden wir die eigene Datenbank-API von Django, die wir im Tutorial 2 behandelt haben. Hier ist eine erste Version einer neuen `index()`-Ansicht, die die fünf neuesten Umfragen in der System anzeigt, getrennt durch Kommas, gemäß dem Veröffentlichungsdatum:

Bearbeiten Sie die Datei `polls/views.py` und ändern Sie sie so, dass sie wie folgt aussieht:

```python
from django.http import HttpResponse

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Lassen Sie die restlichen Ansichten (detail, results, vote) unverändert
```

Es gibt hier jedoch ein Problem: Die Design der Seite ist im Code der Ansicht festcodiert. Wenn Sie die Art, wie die Seite aussieht, ändern möchten, müssen Sie diesen Python-Code bearbeiten. Deshalb verwenden wir das Template-System von Django, um das Design von Python zu trennen, indem wir ein Template erstellen, das die Ansicht verwenden kann.

Erstellen Sie zunächst ein Verzeichnis namens `templates` in Ihrem `polls`-Verzeichnis. Django wird dort nach Templates suchen.

Die `TEMPLATES`-Einstellung Ihres Projekts beschreibt, wie Django Templates laden und rendern wird. Die Standard-Einstellungsdatei konfiguriert einen `DjangoTemplates`-Backend, dessen Option `APP_DIRS <TEMPLATES-APP_DIRS>` auf `True` gesetzt ist. Konventionell sucht `DjangoTemplates` in jedem der `INSTALLED_APPS` ein Unterverzeichnis namens "templates".

Innerhalb des gerade erstellten `templates`-Verzeichnisses erstellen Sie ein weiteres Verzeichnis namens `polls`, und innerhalb davon erstellen Sie eine Datei namens `index.html`. Mit anderen Worten, Ihr Template sollte sich unter `polls/templates/polls/index.html` befinden. Aufgrund der Art, wie der `app_directories`-Template-Loader funktioniert, wie oben beschrieben, können Sie auf dieses Template innerhalb von Django als `polls/index.html` verweisen.

## Template-Namensraum

Wir _könnten_ möglicherweise damit auskommen, unsere Templates direkt in `polls/templates` zu platzieren (anstatt ein weiteres `polls`-Unterverzeichnis zu erstellen), aber es wäre tatsächlich ein schlechter Gedanke. Django wird das erste Template auswählen, dessen Name übereinstimmt, und wenn Sie ein Template mit demselben Namen in einer _anderen_ Anwendung hätten, wäre Django nicht in der Lage, zwischen ihnen zu unterscheiden.

Wir müssen Django in der Lage sein, auf das richtige zu verweisen, und der beste Weg, dies sicherzustellen, ist, indem wir sie _namespacing_. Das heißt, indem wir diese Templates in _einem anderen_ Verzeichnis ablegen, das nach der Anwendung selbst benannt ist.

Fügen Sie den folgenden Code in das Template ein:

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

Hinweis:

Um das Tutorial kürzer zu halten, verwenden alle Template-Beispiele unvollständiges HTML. In Ihren eigenen Projekten sollten Sie [vollständige HTML-Dokumente](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document) verwenden.

Lassen Sie uns nun unsere `index`-Ansicht in `polls/views.py` aktualisieren, um das Template zu verwenden:

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

Dieser Code lädt das Template namens `polls/index.html` und übergibt ihm einen Kontext. Der Kontext ist ein Dictionary, das Template-Variablennamen auf Python-Objekte abbildet.

Starten Sie den Server erneut:

```bash
python manage.py runserver 0.0.0.0:8080
```

Laden Sie die Seite, indem Sie Ihren Browser auf "/polls/" zeigen, und Sie sollten eine aufzählungsweise aufgelistete Liste sehen, die die Frage "What's up" aus Tutorial 2 enthält. Der Link führt zur Detailseite der Frage.

![Django polls index page](../assets/20230908-09-37-26-QMKEbUhb.png)

## Ein Kurzschluss: `~django.shortcuts.render`

Es ist eine sehr häufige Vorgehensweise, ein Template zu laden, einen Kontext zu füllen und ein `~django.http.HttpResponse`-Objekt mit dem Ergebnis des gerenderten Templates zurückzugeben. Django bietet einen Kurzschluss an. Hier ist die vollständige `index()`-Ansicht, neu geschrieben:

```python
from django.shortcuts import render

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Beachten Sie, dass wir dies in allen diesen Ansichten getan haben, brauchen wir nicht mehr `~django.template.loader` und `~django.http.HttpResponse` zu importieren (Sie sollten `HttpResponse` behalten, wenn Sie immer noch die Stub-Methoden für `detail`, `results` und `vote` haben).

Die `~django.shortcuts.render`-Funktion nimmt das Request-Objekt als erstes Argument, einen Template-Namen als zweites Argument und ein Dictionary als optionales drittes Argument entgegen. Sie gibt ein `~django.http.HttpResponse`-Objekt des angegebenen Templates zurück, das mit dem angegebenen Kontext gerendert wurde.
