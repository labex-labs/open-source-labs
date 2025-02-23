# Ein 404-Fehler auslösen

Nun wollen wir uns der Frage-Detail-Ansicht widmen - der Seite, die den Frage-Text für eine bestimmte Umfrage anzeigt. Hier ist die Ansicht:

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

Das neue Konzept hier: Die Ansicht wirft die `~django.http.Http404`-Ausnahme, wenn eine Frage mit der angeforderten ID nicht existiert.

Wir werden später etwas darüber sprechen, was Sie in das `polls/detail.html`-Template einfügen könnten, aber wenn Sie das obige Beispiel schnell zum Laufen bringen möchten, reicht eine Datei, die nur enthält:

```html+django
{{ question }}
```

Das wird Ihnen für jetzt helfen.

## Ein Kurzschluss: `~django.shortcuts.get_object_or_404`

Es ist eine sehr häufige Vorgehensweise, `~django.db.models.query.QuerySet.get` zu verwenden und `~django.http.Http404` auszulösen, wenn das Objekt nicht existiert. Django bietet einen Kurzschluss an. Hier ist die `detail()`-Ansicht, neu geschrieben:

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

Die `~django.shortcuts.get_object_or_404`-Funktion nimmt ein Django-Modell als erstes Argument und eine beliebige Anzahl von Schlüsselwortargumenten entgegen, die sie an die `~django.db.models.query.QuerySet.get`-Funktion des Modells-Managers weitergibt. Sie wirft `~django.http.Http404`, wenn das Objekt nicht existiert.

Warum verwenden wir eine Hilfsfunktion `~django.shortcuts.get_object_or_404` anstatt automatisch die `~django.core.exceptions.ObjectDoesNotExist`-Ausnahmen auf einer höheren Ebene zu fangen oder das Model-API `~django.http.Http404` statt `~django.core.exceptions.ObjectDoesNotExist` auszulösen?

Weil das die Modellschicht mit der Ansichtsschicht verknüpfen würde. Eines der wichtigsten Designziele von Django ist die Aufrechterhaltung einer lose Kopplung. Einige kontrollierte Kopplung wird im `django.shortcuts`-Modul eingeführt.

Es gibt auch eine `~django.shortcuts.get_list_or_404`-Funktion, die genauso funktioniert wie `~django.shortcuts.get_object_or_404` - nur dass sie `~django.db.models.query.QuerySet.filter` statt `~django.db.models.query.QuerySet.get` verwendet. Sie wirft `~django.http.Http404`, wenn die Liste leer ist.
