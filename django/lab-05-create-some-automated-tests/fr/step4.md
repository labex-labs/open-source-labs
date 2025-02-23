# Tester une vue

L'application de sondages est assez indiscriminée : elle publiera n'importe quelle question, y compris celles dont le champ `pub_date` est dans l'avenir. Nous devrions améliorer cela. Fixer une date de publication dans l'avenir devrait signifier que la question est publiée à ce moment-là, mais invisible jusqu'à ce moment.

## Un test pour une vue

Lorsque nous avons corrigé le bogue ci-dessus, nous avons écrit le test d'abord puis le code pour le corriger. En fait, c'était un exemple de développement guidé par les tests, mais il n'est pas vraiment important dans quel ordre nous effectuons le travail.

Dans notre premier test, nous avons concentré notre attention sur le comportement interne du code. Pour ce test, nous voulons vérifier son comportement tel qu'il serait perçu par un utilisateur via un navigateur web.

Avant d'essayer de corriger quoi que ce soit, jetons un coup d'œil aux outils dont nous disposons.

## Le client de test de Django

Django fournit un client de test `~django.test.Client` pour simuler un utilisateur interagissant avec le code au niveau de la vue. Nous pouvons l'utiliser dans `tests.py` ou même dans le `shell`.

Nous allons recommencer avec le `shell`, où nous devons faire quelques choses qui ne seront pas nécessaires dans `tests.py`. La première est de configurer l'environnement de test dans le `shell` :

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` installe un afficheur de gabarit qui nous permettra d'examiner certains attributs supplémentaires sur les réponses telles que `response.context` qui ne seraient pas disponibles autrement. Notez que cette méthode _ne_ configure _pas_ une base de données de test, donc ce qui suit sera exécuté sur la base de données existante et la sortie peut différer légèrement selon les questions que vous avez déjà créées. Vous pouvez obtenir des résultats inattendus si votre `TIME_ZONE` dans `settings.py` n'est pas correcte. Si vous ne vous souvenez pas de l'avoir configurée plus tôt, vérifiez-la avant de continuer.

Ensuite, nous devons importer la classe de client de test (plus tard dans `tests.py` nous utiliserons la classe `django.test.TestCase`, qui a son propre client, donc cela ne sera pas nécessaire) :

```python
>>> from django.test import Client
>>> # créez une instance du client pour notre utilisation
>>> client = Client()
```

Avec tout cela prêt, nous pouvons demander au client de faire quelques travaux pour nous :

```python
>>> # obtenez une réponse de '/'
>>> response = client.get("/")
Page introuvable : /
>>> # nous devrions nous attendre à un 404 de cette adresse ; si au lieu de cela vous voyez une
>>> # erreur "Invalid HTTP_HOST header" et une réponse 400, vous avez probablement
>>> # omis l'appel à setup_test_environment() décrit plus tôt.
>>> response.status_code
404
>>> # d'un autre côté, nous devrions trouver quelque chose à '/polls/'
>>> # nous utiliserons'reverse()' plutôt qu'une URL codée en dur
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## Amélioration de notre vue

La liste des sondages montre des sondages qui ne sont pas encore publiés (c'est-à-dire ceux qui ont une date de publication dans l'avenir). Corrigeons cela.

Dans `**Traitement des formulaires et réduction de notre code**`, nous avons introduit une vue basée sur une classe, basée sur `~django.views.generic.list.ListView` :

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Retourne les cinq dernières questions publiées."""
        return Question.objects.order_by("-pub_date")[:5]
```

Nous devons modifier la méthode `get_queryset()` et la changer de sorte qu'elle vérifie également la date en la comparant avec `timezone.now()`. Tout d'abord, nous devons ajouter une importation :

```python
from django.utils import timezone
```

puis nous devons modifier la méthode `get_queryset` comme ceci :

```python
def get_queryset(self):
    """
    Retourne les cinq dernières questions publiées (sans inclure celles qui sont
    programmées pour être publiées dans l'avenir).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())` renvoie un ensemble de requêtes contenant des `Question` dont la `pub_date` est inférieure ou égale à - c'est-à-dire antérieure ou égale à - `timezone.now`.

## Tester notre nouvelle vue

Maintenant, vous pouvez vous assurer que cela se comporte comme prévu en démarrant `runserver`, en chargeant le site dans votre navigateur, en créant des `Questions` avec des dates passées et futures, et en vérifiant que seules celles qui ont été publiées sont listées. Vous ne voulez pas devoir le faire _chaque fois que vous apportez un changement qui pourrait affecter cela_ - donc créons également un test, basé sur notre session `shell` ci-dessus.

Ajoutez le code suivant à `polls/tests.py` :

```python
from django.urls import reverse
```

et nous créerons une fonction raccourcie pour créer des questions ainsi qu'une nouvelle classe de test :

```python
def create_question(question_text, days):
    """
    Crée une question avec le `question_text` donné et publiée avec un décalage
    de `days` par rapport à maintenant (négatif pour les questions publiées
    dans le passé, positif pour les questions qui n'ont pas encore été publiées).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Si aucune question n'existe, un message approprié est affiché.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun sondage n'est disponible.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Les questions avec une pub_date dans le passé sont affichées sur
        la page d'accueil.
        """
        question = create_question(question_text="Question passée.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Les questions avec une pub_date dans l'avenir ne sont pas affichées sur
        la page d'accueil.
        """
        create_question(question_text="Question future.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Aucun sondage n'est disponible.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Même si des questions passées et futures existent, seule la question passée
        est affichée.
        """
        question = create_question(question_text="Question passée.", days=-30)
        create_question(question_text="Question future.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        La page d'accueil des questions peut afficher plusieurs questions.
        """
        question1 = create_question(question_text="Question passée 1.", days=-30)
        question2 = create_question(question_text="Question passée 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

Regardons de plus près certains d'entre eux.

Tout d'abord, il y a une fonction raccourcie pour les questions, `create_question`, pour éviter de répéter le processus de création de questions.

`test_no_questions` ne crée pas de questions, mais vérifie le message : "Aucun sondage n'est disponible." et vérifie que `latest_question_list` est vide. Notez que la classe `django.test.TestCase` fournit quelques méthodes d'assertion supplémentaires. Dans ces exemples, nous utilisons `~django.test.SimpleTestCase.assertContains()` et `~django.test.TransactionTestCase.assertQuerySetEqual()`.

Dans `test_past_question`, nous créons une question et vérifions qu'elle apparaît dans la liste.

Dans `test_future_question`, nous créons une question avec une `pub_date` dans l'avenir. La base de données est réinitialisée pour chaque méthode de test, donc la première question n'est plus là, et donc à nouveau l'index ne devrait pas avoir de questions.

Et ainsi de suite. En fait, nous utilisons les tests pour raconter une histoire d'entrée d'administrateur et d'expérience utilisateur sur le site, et vérifions que à chaque état et pour chaque nouveau changement d'état du système, les résultats attendus sont publiés.

## Tester la `DetailView`

Ce que nous avons fonctionne bien ; cependant, même si les questions futures n'apparaissent pas dans l'_index_, les utilisateurs peuvent toujours y accéder s'ils connaissent ou devinent l'URL correcte. Nous devons donc ajouter une contrainte similaire à `DetailView` :

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        Exclut toute question qui n'est pas encore publiée.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Nous devrions ensuite ajouter quelques tests pour vérifier qu'une `Question` dont la `pub_date` est dans le passé peut être affichée, et qu'une question avec une `pub_date` dans l'avenir ne l'est pas :

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        La vue détaillée d'une question avec une pub_date dans l'avenir
        renvoie une erreur 404 non trouvée.
        """
        future_question = create_question(question_text="Question future.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        La vue détaillée d'une question avec une pub_date dans le passé
        affiche le texte de la question.
        """
        past_question = create_question(question_text="Question passée.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## Idées pour plus de tests

Nous devrions ajouter une méthode `get_queryset` similaire à `ResultsView` et créer une nouvelle classe de test pour cette vue. Cela sera très similaire à ce que nous venons de créer ; en fait, il y aura beaucoup de répétition.

Nous pourrions également améliorer notre application d'autres manières, en ajoutant des tests le long du chemin. Par exemple, il est absurde que des `Questions` puissent être publiées sur le site sans avoir de `Choices`. Donc, nos vues pourraient vérifier cela et exclure de telles `Questions`. Nos tests créeraient une `Question` sans `Choices` puis testeraient qu'elle n'est pas publiée, ainsi que créer une `Question` similaire _avec_ `Choices`, et testeraient qu'elle _est_ publiée.

Peut-être que les administrateurs connectés devraient être autorisés à voir les `Questions` non publiées, mais pas les visiteurs ordinaires. Encore une fois : tout ce qui doit être ajouté au logiciel pour accomplir cela devrait être accompagné d'un test, que vous écriviez le test d'abord puis que vous fassiez passer le code au test, ou que vous élaboriez d'abord la logique dans votre code puis écriviez un test pour la prouver.

À un certain moment, vous allez certainement regarder vos tests et vous demander si votre code souffre d'un gonflement de tests, ce qui nous amène à :
