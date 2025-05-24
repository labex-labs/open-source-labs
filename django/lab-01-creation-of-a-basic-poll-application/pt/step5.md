# Escreva sua primeira view

Vamos escrever a primeira view. Abra o arquivo `polls/views.py` e coloque o seguinte código Python nele:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Esta é a view mais simples possível em Django. Para chamar a view, precisamos mapeá-la para uma URL - e para isso precisamos de um URLconf.

Para criar um URLconf no diretório polls, crie um arquivo chamado `urls.py`. Seu diretório de aplicativo agora deve ser assim:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

No arquivo `polls/urls.py`, inclua o seguinte código:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

A próxima etapa é apontar o URLconf raiz para o módulo `polls.urls`. Em `mysite/urls.py`, adicione uma importação para `django.urls.include` e insira um `~django.urls.include` na lista `urlpatterns`, para que você tenha:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

A função `~django.urls.include` permite referenciar outros URLconfs. Sempre que Django encontra `~django.urls.include`, ele corta a parte da URL que correspondeu até aquele ponto e envia a string restante para o URLconf incluído para processamento adicional.

A ideia por trás de `~django.urls.include` é facilitar o plug-and-play de URLs. Como as enquetes estão em seu próprio URLconf (`polls/urls.py`), elas podem ser colocadas em "/polls/", ou em "/fun_polls/", ou em "/content/polls/", ou em qualquer outra raiz de caminho, e o aplicativo ainda funcionará.

> Quando usar `~django.urls.include()`
> Você sempre deve usar `include()` ao incluir outros padrões de URL. `admin.site.urls` é a única exceção a isso.

Você agora conectou uma view `index` ao URLconf. Verifique se está funcionando com o seguinte comando:

```bash
python manage.py runserver 0.0.0.0:8080
```

Vá para <http://<url>/polls/> no seu navegador e você deverá ver o texto "_Hello, world. You're at the polls index._", que você definiu na view `index`.

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

A função `~django.urls.path` recebe quatro argumentos, dois obrigatórios: `route` e `view`, e dois opcionais: `kwargs` e `name`. Neste ponto, vale a pena revisar para que servem esses argumentos.

## Argumento `~django.urls.path`: `route`

`route` é uma string que contém um padrão de URL. Ao processar uma solicitação, Django começa no primeiro padrão em `urlpatterns` e percorre a lista, comparando a URL solicitada com cada padrão até encontrar um que corresponda.

Os padrões não pesquisam parâmetros GET e POST, ou o nome de domínio. Por exemplo, em uma solicitação para `https://www.example.com/myapp/`, o URLconf procurará por `myapp/`. Em uma solicitação para `https://www.example.com/myapp/?page=3`, o URLconf também procurará por `myapp/`.

## Argumento `~django.urls.path`: `view`

Quando Django encontra um padrão correspondente, ele chama a função de view especificada com um objeto `~django.http.HttpRequest` como o primeiro argumento e quaisquer valores "capturados" da rota como argumentos de palavra-chave. Daremos um exemplo disso em breve.

## Argumento `~django.urls.path`: `kwargs`

Argumentos de palavra-chave arbitrários podem ser passados em um dicionário para a view de destino. Não vamos usar este recurso do Django no tutorial.

## Argumento `~django.urls.path`: `name`

Nomear sua URL permite que você se refira a ela de forma inequívoca de outras partes do Django, especialmente de dentro dos templates. Este recurso poderoso permite que você faça alterações globais nos padrões de URL do seu projeto, tocando apenas em um único arquivo.
