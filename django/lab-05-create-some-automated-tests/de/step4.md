# Testen einer Ansicht

Die Umfrageanwendung ist ziemlich uneingeschränkt: Sie wird jede Frage veröffentlichen, einschließlich solcher, deren `pub_date`-Feld in der Zukunft liegt. Wir sollten dies verbessern. Ein `pub_date` in der Zukunft sollte bedeuten, dass die Frage zu diesem Zeitpunkt veröffentlicht wird, aber bis dahin unsichtbar.

## Ein Test für eine Ansicht

Als wir oben den Bug behebt haben, haben wir zuerst den Test geschrieben und dann den Code, um ihn zu beheben. Tatsächlich war das ein Beispiel für testgetriebene Entwicklung, aber es spielt eigentlich keine Rolle, in welcher Reihenfolge wir die Arbeit erledigen.

In unserem ersten Test haben wir uns eng auf das interne Verhalten des Codes konzentriert. Für diesen Test möchten wir überprüfen, wie es sich verhält, wenn ein Benutzer es über einen Webbrowser erlebt.

Bevor wir versuchen, etwas zu beheben, schauen wir uns die zur Verfügung stehenden Tools an.

## Der Django-Testclient

Django stellt einen Testclient `~django.test.Client` zur Verfügung, um die Interaktion eines Benutzers mit dem Code auf Ansichts Ebene zu simulieren. Wir können ihn in `tests.py` oder sogar in der `shell` verwenden.

Wir beginnen wieder mit der `shell`, wo wir ein paar Dinge tun müssen, die in `tests.py` nicht erforderlich sind. Das erste ist, die Testumgebung in der `shell` einzurichten:

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` installiert einen Template-Renderer, der uns ermöglicht, einige zusätzliche Attribute auf Antworten wie `response.context` zu untersuchen, die sonst nicht verfügbar wären. Beachten Sie, dass diese Methode _nicht_ eine Testdatenbank einrichtet, sodass die folgenden Befehle gegen die vorhandene Datenbank ausgeführt werden und die Ausgabe je nach den Fragen, die Sie bereits erstellt haben, etwas unterschiedlich aussehen kann. Sie können unerwartete Ergebnisse erhalten, wenn Ihre `TIME_ZONE` in `settings.py` nicht korrekt ist. Wenn Sie sich nicht daran erinnern, sie früher eingestellt zu haben, überprüfen Sie sie, bevor Sie fortfahren.

Als nächstes müssen wir die Testclient-Klasse importieren (später in `tests.py` werden wir die `django.test.TestCase`-Klasse verwenden, die ihren eigenen Client mitbringt, sodass dies nicht erforderlich sein wird):

```python
>>> from django.test import Client
>>> # Erstellen Sie eine Instanz des Clients für unseren Gebrauch
>>> client = Client()
```

Mit diesem eingerichtet können wir dem Client fragen, uns einige Arbeit zu leisten:

```python
>>> # Holen Sie sich eine Antwort von '/'
>>> response = client.get("/")
Not Found: /
>>> # Wir sollten von dieser Adresse eine 404 erwarten; wenn Sie stattdessen
>>> # einen "Invalid HTTP_HOST header"-Fehler und eine 400-Antwort sehen, haben
>>> # Sie wahrscheinlich den oben beschriebenen Aufruf von setup_test_environment()
>>> # übersehen.
>>> response.status_code
404
>>> # Andererseits sollten wir etwas auf '/polls/' finden
>>> # Wir verwenden'reverse()' anstelle einer hartcodierten URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## Verbesserung unserer Ansicht

Die Liste der Umfragen zeigt Umfragen an, die noch nicht veröffentlicht sind (d.h. die, die ein `pub_date` in der Zukunft haben). Lassen Sie uns das beheben.

In `**Form Processing and Cutting Down Our Code**` haben wir eine klassengebasierte Ansicht eingeführt, basierend auf `~django.views.generic.list.ListView`:

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
```

Wir müssen die `get_queryset()`-Methode ändern und so umgestalten, dass sie auch das Datum überprüft, indem es mit `timezone.now()` verglichen wird. Zunächst müssen wir einen Import hinzufügen:

```python
from django.utils import timezone
```

und dann müssen wir die `get_queryset`-Methode wie folgt ändern:

```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())` gibt einen QuerySet zurück, der `Question`s enthält, deren `pub_date` kleiner oder gleich - d.h. früher oder gleich - `timezone.now` ist.

## Testen unserer neuen Ansicht

Jetzt können Sie sich vergewissern, dass dies wie erwartet funktioniert, indem Sie `runserver` starten, die Website in Ihrem Browser laden, `Questions` mit Daten in der Vergangenheit und Zukunft erstellen und überprüfen, dass nur die veröffentlichten aufgelistet werden. Sie möchten nicht jedes Mal, wenn Sie eine Änderung vornehmen, die dies möglicherweise beeinflusst, dazu gezwungen sein, dies zu tun - also erstellen wir auch einen Test, basierend auf unserer obigen `shell`-Session.

Fügen Sie Folgendes zu `polls/tests.py` hinzu:

```python
from django.urls import reverse
```

und wir erstellen eine Kurzschreibfunktion, um Fragen zu erstellen, sowie eine neue Testklasse:

```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

Schauen wir uns einige davon genauer an.

Zunächst ist eine Frage-Kurzschreibfunktion, `create_question`, um einige Wiederholungen beim Erstellen von Fragen zu vermeiden.

`test_no_questions` erstellt keine Fragen, sondern überprüft die Nachricht: "No polls are available." und verifiziert, dass die `latest_question_list` leer ist. Beachten Sie, dass die `django.test.TestCase`-Klasse einige zusätzliche Assertionsmethoden bietet. In diesen Beispielen verwenden wir `~django.test.SimpleTestCase.assertContains()` und `~django.test.TransactionTestCase.assertQuerySetEqual()`.

In `test_past_question` erstellen wir eine Frage und überprüfen, dass sie in der Liste erscheint.

In `test_future_question` erstellen wir eine Frage mit einem `pub_date` in der Zukunft. Die Datenbank wird für jede Testmethode zurückgesetzt, sodass die erste Frage nicht mehr vorhanden ist, und daher sollte auch der Index keine Fragen enthalten.

Und so weiter. Tatsächlich verwenden wir die Tests, um eine Geschichte über die Admin-Eingabe und die Benutzererfahrung auf der Website zu erzählen und zu überprüfen, dass in jedem Zustand und für jede neue Änderung im Zustand des Systems die erwarteten Ergebnisse veröffentlicht werden.

## Testen der `DetailView`

Was wir haben, funktioniert gut; jedoch können Benutzer, auch wenn zukünftige Fragen nicht im _Index_ erscheinen, immer noch auf sie zugreifen, wenn sie die richtige URL kennen oder erraten. Wir müssen daher eine ähnliche Einschränkung für die `DetailView` hinzufügen:

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Wir sollten dann einige Tests hinzufügen, um zu überprüfen, dass eine `Question`, deren `pub_date` in der Vergangenheit ist, angezeigt werden kann, und dass eine mit einem `pub_date` in der Zukunft nicht angezeigt wird:

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## Ideen für weitere Tests

Wir sollten eine ähnliche `get_queryset`-Methode zu `ResultsView` hinzufügen und eine neue Testklasse für diese Ansicht erstellen. Es wird sehr ähnlich zu dem, was wir gerade erstellt haben; tatsächlich wird es eine Menge Wiederholungen geben.

Wir könnten unsere Anwendung auch auf andere Weise verbessern und dabei Tests hinzufügen. Beispielsweise ist es dumm, dass `Questions` auf der Website veröffentlicht werden können, die keine `Choices` haben. Unsere Ansichten könnten daher darauf prüfen und solche `Questions` ausschließen. Unsere Tests würden eine `Question` ohne `Choices` erstellen und dann testen, dass sie nicht veröffentlicht wird, sowie eine ähnliche `Question` _mit_ `Choices` erstellen und testen, dass sie _veröffentlicht_ wird.

Vielleicht sollten angemeldete Admin-Benutzer nicht veröffentlichte `Questions` sehen können, aber normale Besucher schon. Wieder: Alles, was zur Software hinzugefügt werden muss, um dies zu erreichen, sollte von einem Test begleitet werden, ob Sie den Test zuerst schreiben und dann den Code so gestalten, dass er den Test besteht, oder zuerst die Logik in Ihrem Code erarbeiten und dann einen Test schreiben, um es zu beweisen.

Nach einer gewissen Zeit werden Sie sicherlich auf Ihre Tests schauen und sich fragen, ob Ihr Code unter Testüberflutung leidet, was uns zu:
