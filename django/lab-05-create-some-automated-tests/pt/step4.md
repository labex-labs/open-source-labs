# Testando uma view

A aplicação polls é bastante indiscriminada: ela publicará qualquer pergunta, incluindo aquelas cujo campo `pub_date` está no futuro. Devemos melhorar isso. Definir um `pub_date` no futuro deve significar que a Question é publicada naquele momento, mas invisível até então.

## Um teste para uma view

Quando corrigimos o bug acima, escrevemos o teste primeiro e depois o código para corrigi-lo. Na verdade, esse foi um exemplo de desenvolvimento orientado a testes, mas não importa realmente em que ordem fazemos o trabalho.

Em nosso primeiro teste, nos concentramos de perto no comportamento interno do código. Para este teste, queremos verificar seu comportamento como seria experimentado por um usuário através de um navegador web.

Antes de tentar corrigir qualquer coisa, vamos dar uma olhada nas ferramentas à nossa disposição.

## O cliente de teste Django

O Django fornece um `~django.test.Client` de teste para simular um usuário interagindo com o código no nível da view. Podemos usá-lo em `tests.py` ou até mesmo no `shell`.

Começaremos novamente com o `shell`, onde precisamos fazer algumas coisas que não serão necessárias em `tests.py`. A primeira é configurar o ambiente de teste no `shell`:

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` instala um renderizador de template que nos permitirá examinar alguns atributos adicionais nas respostas, como `response.context`, que de outra forma não estariam disponíveis. Observe que este método _não_ configura um banco de dados de teste, portanto, o seguinte será executado em relação ao banco de dados existente e a saída pode diferir ligeiramente dependendo de quais perguntas você já criou. Você pode obter resultados inesperados se seu `TIME_ZONE` em `settings.py` não estiver correto. Se você não se lembra de defini-lo anteriormente, verifique-o antes de continuar.

Em seguida, precisamos importar a classe do cliente de teste (mais tarde em `tests.py` usaremos a classe `django.test.TestCase`, que vem com seu próprio cliente, então isso não será necessário):

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

Com isso pronto, podemos pedir ao cliente para fazer algum trabalho para nós:

```python
>>> # get a response from '/'
>>> response = client.get("/")
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## Melhorando nossa view

A lista de enquetes mostra enquetes que ainda não foram publicadas (ou seja, aquelas que têm um `pub_date` no futuro). Vamos corrigir isso.

Em `**Processamento de Formulários e Reduzindo Nosso Código**` introduzimos uma view baseada em classe, baseada em `~django.views.generic.list.ListView`:

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
```

Precisamos alterar o método `get_queryset()` e alterá-lo para que ele também verifique a data, comparando-a com `timezone.now()`. Primeiro, precisamos adicionar uma importação:

```python
from django.utils import timezone
```

e então devemos alterar o método `get_queryset` assim:

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

`Question.objects.filter(pub_date__lte=timezone.now())` retorna um queryset contendo `Question`s cujo `pub_date` é menor ou igual a - ou seja, anterior ou igual a - `timezone.now`.

## Testando nossa nova view

Agora você pode se certificar de que isso se comporta como esperado, iniciando o `runserver`, carregando o site em seu navegador, criando `Questions` com datas no passado e no futuro e verificando se apenas aquelas que foram publicadas estão listadas. Você não quer ter que fazer isso _toda vez que fizer qualquer alteração que possa afetar isso_ - então vamos também criar um teste, com base em nossa sessão `shell` acima.

Adicione o seguinte a `polls/tests.py`:

```python
from django.urls import reverse
```

e criaremos uma função de atalho para criar perguntas, bem como uma nova classe de teste:

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

Vamos analisar alguns deles mais de perto.

Primeiro, há uma função de atalho de pergunta, `create_question`, para tirar um pouco da repetição do processo de criação de perguntas.

`test_no_questions` não cria nenhuma pergunta, mas verifica a mensagem: "No polls are available." e verifica se `latest_question_list` está vazio. Observe que a classe `django.test.TestCase` fornece alguns métodos de asserção adicionais. Nesses exemplos, usamos `~django.test.SimpleTestCase.assertContains()` e `~django.test.TransactionTestCase.assertQuerySetEqual()`.

Em `test_past_question`, criamos uma pergunta e verificamos se ela aparece na lista.

Em `test_future_question`, criamos uma pergunta com um `pub_date` no futuro. O banco de dados é redefinido para cada método de teste, então a primeira pergunta não está mais lá e, portanto, novamente o índice não deve ter nenhuma pergunta nele.

E assim por diante. Na verdade, estamos usando os testes para contar uma história de entrada do administrador e experiência do usuário no site, e verificando que em cada estado e para cada nova mudança no estado do sistema, os resultados esperados são publicados.

## Testando o `DetailView`

O que temos funciona bem; no entanto, embora as perguntas futuras não apareçam no _índice_, os usuários ainda podem acessá-las se souberem ou adivinharem a URL correta. Então, precisamos adicionar uma restrição semelhante ao `DetailView`:

```python
class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Devemos então adicionar alguns testes para verificar se uma `Question` cujo `pub_date` está no passado pode ser exibida e que uma com um `pub_date` no futuro não pode:

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

## Ideias para mais testes

Devemos adicionar um método `get_queryset` semelhante a `ResultsView` e criar uma nova classe de teste para essa view. Será muito semelhante ao que acabamos de criar; na verdade, haverá muita repetição.

Também poderíamos melhorar nossa aplicação de outras maneiras, adicionando testes ao longo do caminho. Por exemplo, é bobo que `Questions` possam ser publicadas no site que não têm `Choices`. Portanto, nossas views poderiam verificar isso e excluir tais `Questions`. Nossos testes criariam uma `Question` sem `Choices` e, em seguida, testariam se ela não é publicada, bem como criariam uma `Question` semelhante _com_ `Choices` e testariam se ela _é_ publicada.

Talvez os usuários administradores logados devam ter permissão para ver `Questions` não publicadas, mas não visitantes comuns. Novamente: o que precisar ser adicionado ao software para realizar isso deve ser acompanhado por um teste, seja você escrevendo o teste primeiro e depois fazendo o código passar no teste, ou elaborando a lógica em seu código primeiro e depois escrevendo um teste para prová-lo.

Em um determinado momento, você certamente analisará seus testes e se perguntará se seu código está sofrendo de inchaço de teste, o que nos leva a:
