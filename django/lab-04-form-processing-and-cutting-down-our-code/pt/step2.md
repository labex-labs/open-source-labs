# Use generic views: Menos código é melhor

As views `detail()` (de `**Criando as Visões da Interface Pública**`) e `results()` são muito curtas -- e, como mencionado acima, redundantes. A view `index()`, que exibe uma lista de enquetes, é semelhante.

Essas views representam um caso comum de desenvolvimento web básico: obter dados do banco de dados de acordo com um parâmetro passado na URL, carregar um template e retornar o template renderizado. Como isso é tão comum, o Django fornece um atalho, chamado de sistema de "views genéricas".

As views genéricas abstraem padrões comuns a ponto de você nem precisar escrever código Python para escrever um aplicativo.

Vamos converter nosso aplicativo de enquete para usar o sistema de views genéricas, para que possamos excluir um monte de nosso próprio código. Teremos que seguir algumas etapas para fazer a conversão. Nós iremos:

1. Converter o URLconf.
2. Excluir algumas das views antigas e desnecessárias.
3. Introduzir novas views baseadas nas views genéricas do Django.

Leia para obter detalhes.

> Por que a troca de código?

Geralmente, ao escrever um aplicativo Django, você avaliará se as views genéricas são adequadas para o seu problema e as usará desde o início, em vez de refatorar seu código no meio do caminho. Mas este tutorial intencionalmente se concentrou em escrever as views "da maneira difícil" até agora, para focar nos conceitos principais.

Você deve saber matemática básica antes de começar a usar uma calculadora.

## Amend URLconf (Alterar URLconf)

Primeiro, abra o URLconf `polls/urls.py` e altere-o assim:

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Observe que o nome do padrão correspondente nas strings de caminho dos segundo e terceiro padrões mudou de `<question_id>` para `<pk>`.

## Amend views (Alterar views)

Em seguida, vamos remover nossas antigas views `index`, `detail` e `results` e usar as views genéricas do Django em vez disso. Para fazer isso, abra o arquivo `polls/views.py` e altere-o assim:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


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
    ...  # same as above, no changes needed.
```

Estamos usando duas views genéricas aqui: `~django.views.generic.list.ListView` e `~django.views.generic.detail.DetailView`. Respectivamente, essas duas views abstraem os conceitos de "exibir uma lista de objetos" e "exibir uma página de detalhes para um tipo específico de objeto".

- Cada view genérica precisa saber em qual model ela estará atuando. Isso é fornecido usando o atributo `model`.
- A view genérica `~django.views.generic.detail.DetailView` espera que o valor da chave primária capturado da URL seja chamado `"pk"`, então mudamos `question_id` para `pk` para as views genéricas.

Por padrão, a view genérica `~django.views.generic.detail.DetailView` usa um template chamado `<nome do aplicativo>/<nome do model>_detail.html`. Em nosso caso, ele usaria o template `"polls/question_detail.html"`. O atributo `template_name` é usado para dizer ao Django para usar um nome de template específico em vez do nome do template padrão autogerado. Também especificamos o `template_name` para a view de lista `results` -- isso garante que a view de resultados e a view de detalhes tenham uma aparência diferente quando renderizadas, embora ambas sejam um `~django.views.generic.detail.DetailView` nos bastidores.

Da mesma forma, a view genérica `~django.views.generic.list.ListView` usa um template padrão chamado `<nome do aplicativo>/<nome do model>_list.html`; usamos `template_name` para dizer ao `~django.views.generic.list.ListView` para usar nosso template `"polls/index.html"` existente.

Nas partes anteriores do tutorial, os templates foram fornecidos com um contexto que contém as variáveis de contexto `question` e `latest_question_list`. Para `DetailView`, a variável `question` é fornecida automaticamente -- como estamos usando um model Django (`Question`), o Django é capaz de determinar um nome apropriado para a variável de contexto. No entanto, para ListView, a variável de contexto gerada automaticamente é `question_list`. Para substituir isso, fornecemos o atributo `context_object_name`, especificando que queremos usar `latest_question_list` em vez disso. Como uma abordagem alternativa, você pode alterar seus templates para corresponder às novas variáveis de contexto padrão -- mas é muito mais fácil dizer ao Django para usar a variável que você deseja.

Execute o servidor e use seu novo aplicativo de enquete baseado em views genéricas.
