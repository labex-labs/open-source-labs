# Schreiben eines minimalen Formulars

Lassen Sie uns die Umfrage-Detail-Vorlage (`polls/detail.html`) aus dem letzten Tutorial aktualisieren, sodass die Vorlage ein HTML `<form>`-Element enthält:

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

Eine schnelle Übersicht:

- Die obige Vorlage zeigt für jede Frageauswahl einen Radiobutton an. Der `value` jedes Radiobuttons ist die ID der zugehörigen Frageauswahl. Der `name` jedes Radiobuttons ist `"choice"`. Das bedeutet, wenn jemand einen der Radiobuttons auswählt und das Formular abgibt, wird es die POST-Daten `choice=#` senden, wobei \# die ID der ausgewählten Auswahl ist. Dies ist das grundlegende Konzept von HTML-Formularen.
- Wir setzen die `action` des Formulars auf `{% url 'polls:vote' question.id %}` und `method="post"`. Das Verwenden von `method="post"` (im Gegensatz zu `method="get"`) ist sehr wichtig, da das Absenden dieses Formulars die Daten auf der Serverseite ändern wird. Wann immer Sie ein Formular erstellen, das die Daten auf der Serverseite ändert, verwenden Sie `method="post"`. Dieser Tipp ist nicht speziell für Django; es ist allgemein gute Praxis im Web-Entwicklung.
- `forloop.counter` gibt an, wie oft der `for`-Tag seine Schleife durchlaufen hat.
- Da wir ein POST-Formular erstellen (was die Wirkung haben kann, Daten zu ändern), müssen wir uns um Cross-Site-Request-Forgery (CSRF) kümmern. Glücklicherweise müssen Sie sich nicht zu sehr darum kümmern, weil Django ein hilfreiches System zur Schutz vor diesem bietet. Kurz gesagt sollten alle POST-Formulare, die auf interne URLs gerichtet sind, das `{% csrf_token %}<csrf_token>`-Vorlagentag verwenden.

Lassen Sie uns nun eine Django-Ansicht erstellen, die die abgeschickten Daten verarbeitet und damit etwas macht. Denken Sie daran, dass wir in `**Creating the Public Interface Views**` eine URLconf für die Umfrageanwendung erstellt haben, die diese Zeile enthält:

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

Wir haben auch eine Dummy-Implementierung der `vote()`-Funktion erstellt. Lassen Sie uns eine echte Version erstellen. Fügen Sie Folgendes zu `polls/views.py` hinzu:

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question


#...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Zeige das Frageabstimmungsformular erneut an.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Geben Sie immer eine HttpResponseRedirect zurück, nachdem Sie
        # erfolgreich mit POST-Daten umgegangen sind. Dies verhindert, dass
        # Daten zweimal gesendet werden, wenn ein Benutzer die
        # Zurück-Taste drückt.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

Dieser Code enthält ein paar Dinge, die wir in diesem Tutorial noch nicht behandelt haben:

- `request.POST <django.http.HttpRequest.POST>` ist ein dictionary-ähnliches Objekt, das Ihnen ermöglicht, abgeschickte Daten nach Schlüsselnamen zuzugreifen. In diesem Fall gibt `request.POST['choice']` die ID der ausgewählten Auswahl als String zurück. Die Werte von `request.POST <django.http.HttpRequest.POST>` sind immer Strings.

  Beachten Sie, dass Django auch `request.GET
<django.http.HttpRequest.GET>` zur Zugang zu GET-Daten auf die gleiche Weise bietet - aber wir verwenden explizit `request.POST
<django.http.HttpRequest.POST>` in unserem Code, um sicherzustellen, dass die Daten nur über einen POST-Aufruf geändert werden.

- `request.POST['choice']` wird `KeyError` auslösen, wenn `choice` in den POST-Daten nicht angegeben wurde. Der obige Code überprüft auf `KeyError` und zeigt das Frageformular erneut an, wenn `choice` nicht angegeben ist.

- Nachdem die Stimmenzahl erhöht wurde, gibt der Code eine `~django.http.HttpResponseRedirect` zurück, statt einer normalen `~django.http.HttpResponse`. `~django.http.HttpResponseRedirect` nimmt einen einzelnen Parameter: die URL, zu der der Benutzer weitergeleitet wird (siehe den folgenden Punkt, wie wir in diesem Fall die URL konstruieren).

  Wie der Python-Kommentar oben zeigt, sollten Sie immer eine `~django.http.HttpResponseRedirect` zurückgeben, nachdem Sie erfolgreich mit POST-Daten umgegangen sind. Dieser Tipp ist nicht speziell für Django; es ist allgemein gute Praxis im Web-Entwicklung.

- Wir verwenden in diesem Beispiel die `~django.urls.reverse`-Funktion im `~django.http.HttpResponseRedirect`-Konstruktor. Diese Funktion hilft dabei, eine URL im View-Funktion nicht hartcodieren zu müssen. Es wird der Name der Ansicht übergeben, an die wir die Steuerung weitergeben möchten, und der variable Teil des URL-Patterns, das auf diese Ansicht zeigt. In diesem Fall wird, wenn wir die URLconf verwenden, die wir in `**Creating the Public Interface Views**` eingerichtet haben, dieser `~django.urls.reverse`-Aufruf eine Zeichenfolge wie diese zurückgeben:

      "/polls/3/results/"

  wobei die `3` der Wert von `question.id` ist. Die weitergeleitete URL ruft dann die `'results'`-Ansicht auf, um die Endseite anzuzeigen.

Wie in `**Creating the Public Interface Views**` erwähnt, ist `request` ein `~django.http.HttpRequest`-Objekt. Weitere Informationen zu `~django.http.HttpRequest`-Objekten finden Sie in der `request and
response documentation </ref/request-response>`.

Nachdem jemand in einer Frage abgestimmt hat, leitet die `vote()`-Ansicht zur Ergebnispage der Frage weiter. Schreiben Sie diese Ansicht:

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

Dies ist fast genau die gleiche wie die `detail()`-Ansicht aus **Creating the Public Interface Views**. Der einzige Unterschied ist der Vorlagenname. Wir werden diese Redundanz später beheben.

Erstellen Sie nun eine `polls/results.html`-Vorlage:

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

Gehen Sie nun in Ihrem Browser zu `/polls/1/` und stimmen Sie in der Frage ab. Sie sollten eine Ergebnispage sehen, die sich jedes Mal aktualisiert, wenn Sie abstimmen. Wenn Sie das Formular absenden, ohne eine Auswahl getroffen zu haben, sollten Sie die Fehlermeldung sehen.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![Poll voting form interface](../assets/20230908-10-37-07-p9ewKbe6.png)

**Hinweis:**

Der Code unserer `vote()`-Ansicht hat ein kleines Problem. Er ruft zunächst das `selected_choice`-Objekt aus der Datenbank ab, berechnet dann den neuen Wert von `votes` und speichert ihn dann wieder in der Datenbank. Wenn zwei Benutzer Ihrer Website _genau zur gleichen Zeit_ versuchen, abzustimmen, kann das schiefgehen: Für `votes` wird derselbe Wert, sagen wir 42, abgerufen. Dann wird für beide Benutzer der neue Wert von 43 berechnet und gespeichert, aber 44 wäre der erwartete Wert.

Dies wird als _Race Condition_ bezeichnet. Wenn Sie interessiert sind, können Sie `avoiding-race-conditions-using-f` lesen, um zu lernen, wie Sie dieses Problem lösen können.
