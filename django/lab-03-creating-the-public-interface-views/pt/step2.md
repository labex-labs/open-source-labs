# Escrevendo mais views

Agora, vamos adicionar mais algumas views a `polls/views.py`. Essas views são ligeiramente diferentes, porque recebem um argumento:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Conecte essas novas views ao módulo `polls.urls` adicionando as seguintes chamadas `~django.urls.path`:

Edite o arquivo `polls/urls.py` e adicione as seguintes linhas:

```python
from django.urls import path

from . import views

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

Agora, execute o servidor novamente:

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Mude para a aba **Web 8080**, em `/polls/34/`. Ele executará o método `detail()` e exibirá qualquer ID que você fornecer na URL. Tente `/polls/34/results/` e `/polls/34/vote/` também -- estes exibirão os resultados e as páginas de votação de espaço reservado.

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

Quando alguém solicita uma página do seu site -- por exemplo, `/polls/34/`, o Django carregará o módulo Python `mysite.urls` porque ele é apontado pela configuração `ROOT_URLCONF`. Ele encontra a variável chamada `urlpatterns` e percorre os padrões em ordem. Depois de encontrar a correspondência em `'polls/'`, ele remove o texto correspondente (`"polls/"`) e envia o texto restante -- `"34/"` -- para a URLconf 'polls.urls' para processamento adicional. Lá, ele corresponde a `'<int:question_id>/'`, resultando em uma chamada para a view `detail()` da seguinte forma:

```python
detail(request=<HttpRequest object>, question_id=34)
```

A parte `question_id=34` vem de `<int:question_id>`. O uso de colchetes angulares "captura" parte da URL e a envia como um argumento de palavra-chave para a função de view. A parte `question_id` da string define o nome que será usado para identificar o padrão correspondente, e a parte `int` é um conversor que determina quais padrões devem corresponder a esta parte do caminho da URL. Os dois pontos (`:`) separam o conversor e o nome do padrão.
