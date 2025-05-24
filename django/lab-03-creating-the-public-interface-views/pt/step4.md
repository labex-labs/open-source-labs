# Levantando um erro 404

Agora, vamos abordar a view de detalhes da pergunta -- a página que exibe o texto da pergunta para uma determinada enquete. Aqui está a view:

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

O novo conceito aqui: A view levanta a exceção `~django.http.Http404` se uma pergunta com o ID solicitado não existir.

Discutiremos o que você pode colocar naquele template `polls/detail.html` um pouco mais tarde, mas se você quiser fazer o exemplo acima funcionar rapidamente, um arquivo contendo apenas:

```html+django
{{ question }}
```

irá te iniciar por agora.

## Um atalho: `~django.shortcuts.get_object_or_404`

É um idioma muito comum usar `~django.db.models.query.QuerySet.get` e levantar `~django.http.Http404` se o objeto não existir. O Django fornece um atalho. Aqui está a view `detail()`, reescrita:

```python
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

A função `~django.shortcuts.get_object_or_404` recebe um modelo Django como seu primeiro argumento e um número arbitrário de argumentos de palavra-chave, que ele passa para a função `~django.db.models.query.QuerySet.get` do gerenciador do modelo. Ele levanta `~django.http.Http404` se o objeto não existir.

Por que usamos uma função auxiliar `~django.shortcuts.get_object_or_404` em vez de capturar automaticamente as exceções `~django.core.exceptions.ObjectDoesNotExist` em um nível superior, ou fazer com que a API do modelo levante `~django.http.Http404` em vez de `~django.core.exceptions.ObjectDoesNotExist`?

Porque isso acoplaria a camada do modelo à camada da view. Um dos principais objetivos de design do Django é manter o acoplamento frouxo. Algum acoplamento controlado é introduzido no módulo `django.shortcuts`.

Há também uma função `~django.shortcuts.get_list_or_404`, que funciona como `~django.shortcuts.get_object_or_404` -- exceto usando `~django.db.models.query.QuerySet.filter` em vez de `~django.db.models.query.QuerySet.get`. Ele levanta `~django.http.Http404` se a lista estiver vazia.
