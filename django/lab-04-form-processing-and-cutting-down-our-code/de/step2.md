# Verwenden von generischen Ansichten: Weniger Code ist besser

Die `detail()`-Ansicht (aus `**Creating the Public Interface Views**`) und die `results()`-Ansicht sind sehr kurz - und, wie oben erwähnt, redundant. Die `index()`-Ansicht, die eine Liste von Umfragen anzeigt, ist ähnlich.

Diese Ansichten repräsentieren einen häufigen Fall der grundlegenden Webentwicklung: das Abrufen von Daten aus der Datenbank gemäß einem Parameter, der in der URL übergeben wird, das Laden einer Vorlage und das Zurückgeben der gerenderten Vorlage. Da dies so häufig vorkommt, bietet Django einen Kurzweg, den "generischen Ansichten"-System.

Generische Ansichten abstrahieren häufige Muster bis zu einem Punkt, wo Sie sogar kein Python-Code schreiben müssen, um eine App zu schreiben.

Lassen Sie uns unsere Umfrage-App umstellen, um das generische Ansichten-System zu verwenden, so dass wir eine Menge unseren eigenen Codes löschen können. Wir müssen einige Schritte unternehmen, um die Umstellung durchzuführen. Wir werden:

1. Die URLconf umstellen.
2. Einige der alten, unnötigen Ansichten löschen.
3. Neue Ansichten auf der Grundlage von Djangos generischen Ansichten einführen.

Lesen Sie weiter für Details.

> Warum der Code-Umzug?

Allgemein gesehen werden Sie bei der Schreibung einer Django-App evaluieren, ob generische Ansichten für Ihr Problem geeignet sind, und Sie werden sie von Anfang an verwenden, anstatt Ihren Code halbwegs umzuarbeiten. Aber in diesem Tutorial wurde bislang bewusst darauf fokussiert, die Ansichten "auf die schwere Weise" zu schreiben, um auf die Kernkonzepte zu fokussieren.

Sie sollten Grundrechnen können, bevor Sie einen Taschenrechner verwenden.

## URLconf anpassen

Öffnen Sie zunächst die URLconf `polls/urls.py` und ändern Sie sie wie folgt:

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Beachten Sie, dass der Name des gematchten Musters in den Pfadzeichenfolgen des zweiten und dritten Musters von `<question_id>` zu `<pk>` geändert ist.

## Ansichten anpassen

Als nächstes werden wir unsere alten `index`, `detail` und `results`-Ansichten entfernen und stattdessen Djangos generische Ansichten verwenden. Um dies zu tun, öffnen Sie die Datei `polls/views.py` und ändern Sie sie wie folgt:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from.models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # wie oben, keine Änderungen erforderlich.
```

Wir verwenden hier zwei generische Ansichten: `~django.views.generic.list.ListView` und `~django.views.generic.detail.DetailView`. Die beiden Ansichten abstrahieren jeweils die Konzepte "Zeige eine Liste von Objekten an" und "Zeige eine Detailseite für einen bestimmten Objekttyp an".

- Jede generische Ansicht muss wissen, auf welchem Modell sie arbeiten wird. Dies wird mithilfe des `model`-Attributs bereitgestellt.
- Die `~django.views.generic.detail.DetailView`-generische Ansicht erwartet, dass der Primärschlüsselwert, der aus der URL abgerufen wird, `"pk"` genannt wird, daher haben wir `question_id` für die generischen Ansichten in `pk` geändert.

Standardmäßig verwendet die `~django.views.generic.detail.DetailView`-generische Ansicht eine Vorlage namens `<app name>/<model name>_detail.html`. Im unserem Fall würde sie die Vorlage `"polls/question_detail.html"` verwenden. Das `template_name`-Attribut wird verwendet, um Django mitzuteilen, dass eine bestimmte Vorlagenname statt des automatisch generierten Standardvorlagennamens verwendet werden soll. Wir geben auch den `template_name` für die `results`-Listenansicht an - dies gewährleistet, dass die Ergebnisansicht und die Detailansicht bei der Darstellung ein unterschiedliches Aussehen haben, obwohl sie beide hinter den Kulissen eine `~django.views.generic.detail.DetailView` sind.

Ähnlich verwendet die `~django.views.generic.list.ListView`-generische Ansicht eine Standardvorlage namens `<app name>/<model name>_list.html`; wir verwenden `template_name`, um `~django.views.generic.list.ListView` mitzuteilen, dass unsere vorhandene `"polls/index.html"`-Vorlage verwendet werden soll.

In früheren Teilen des Tutorials wurden den Vorlagen ein Kontext zur Verfügung gestellt, der die `question` und `latest_question_list`-Kontextvariablen enthält. Für `DetailView` wird die `question`-Variable automatisch bereitgestellt - da wir ein Django-Modell (`Question`) verwenden, kann Django einen passenden Namen für die Kontextvariable bestimmen. Für `ListView` ist jedoch die automatisch generierte Kontextvariable `question_list`. Um dies zu überschreiben, geben wir das `context_object_name`-Attribut an und geben an, dass wir `latest_question_list` statt dessen verwenden möchten. Als alternative Methode könnten Sie Ihre Vorlagen ändern, um den neuen Standardkontextvariablen zu entsprechen - aber es ist einfacher, Django mitzuteilen, welche Variable Sie möchten verwenden.

Starten Sie den Server und verwenden Sie Ihre neue Umfrage-App, die auf generischen Ansichten basiert.
