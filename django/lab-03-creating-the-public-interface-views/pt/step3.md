# Escreva views que realmente façam algo

Cada view é responsável por fazer uma de duas coisas: retornar um objeto `~django.http.HttpResponse` contendo o conteúdo para a página solicitada, ou lançar uma exceção como `~django.http.Http404`. O resto depende de você.

Sua view pode ler registros de um banco de dados, ou não. Ela pode usar um sistema de template como o do Django -- ou um sistema de template Python de terceiros -- ou não. Ela pode gerar um arquivo PDF, gerar XML, criar um arquivo ZIP na hora, qualquer coisa que você quiser, usando as bibliotecas Python que você quiser.

Tudo o que o Django quer é um `~django.http.HttpResponse`. Ou uma exceção.

Como é conveniente, vamos usar a própria API de banco de dados do Django, que cobrimos no Tutorial 2. Aqui está uma tentativa de uma nova view `index()`, que exibe as últimas 5 perguntas da enquete no sistema, separadas por vírgulas, de acordo com a data de publicação:

Edite o arquivo `polls/views.py` e altere-o para que se pareça com isto:

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Deixe o resto das views (detail, results, vote) inalterado
```

Há um problema aqui, no entanto: o design da página é codificado na view. Se você quiser mudar a aparência da página, terá que editar este código Python. Então, vamos usar o sistema de template do Django para separar o design do Python, criando um template que a view possa usar.

Primeiro, crie um diretório chamado `templates` em seu diretório `polls`. O Django procurará templates lá.

A configuração `TEMPLATES` do seu projeto descreve como o Django carregará e renderizará os templates. O arquivo de configurações padrão configura um backend `DjangoTemplates` cuja opção `APP_DIRS <TEMPLATES-APP_DIRS>` está definida como `True`. Por convenção, `DjangoTemplates` procura um subdiretório "templates" em cada um dos `INSTALLED_APPS`.

Dentro do diretório `templates` que você acabou de criar, crie outro diretório chamado `polls` e, dentro dele, crie um arquivo chamado `index.html`. Em outras palavras, seu template deve estar em `polls/templates/polls/index.html`. Por causa de como o carregador de template `app_directories` funciona, conforme descrito acima, você pode se referir a este template dentro do Django como `polls/index.html`.

## Namespacing de template

Agora, _poderíamos_ nos safar colocando nossos templates diretamente em `polls/templates` (em vez de criar outro subdiretório `polls`), mas na verdade seria uma má ideia. O Django escolherá o primeiro template que encontrar cujo nome corresponda, e se você tivesse um template com o mesmo nome em uma aplicação _diferente_, o Django não conseguiria distinguir entre eles.

Precisamos ser capazes de apontar o Django para o correto, e a melhor maneira de garantir isso é _namespacing_ (definir namespace) eles. Ou seja, colocando esses templates dentro de _outro_ diretório nomeado para a própria aplicação.

Coloque o seguinte código nesse template:

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Observação:

Para tornar o tutorial mais curto, todos os exemplos de template usam HTML incompleto. Em seus próprios projetos, você deve usar [documentos HTML completos](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document).

Agora, vamos atualizar nossa view `index` em `polls/views.py` para usar o template:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

Esse código carrega o template chamado `polls/index.html` e passa um contexto para ele. O contexto é um dicionário que mapeia nomes de variáveis de template para objetos Python.

Execute o servidor novamente:

```bash
python manage.py runserver 0.0.0.0:8080
```

Carregue a página apontando seu navegador para "/polls/", e você deverá ver uma lista com marcadores contendo a pergunta "What's up" do Tutorial 2. O link aponta para a página de detalhes da pergunta.

![Django polls index page](../assets/20230908-09-37-26-QMKEbUhb.png)

## Um atalho: `~django.shortcuts.render`

É um idioma muito comum carregar um template, preencher um contexto e retornar um objeto `~django.http.HttpResponse` com o resultado do template renderizado. O Django fornece um atalho. Aqui está a view `index()` completa, reescrita:

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Observe que, uma vez que fizemos isso em todas essas views, não precisamos mais importar `~django.template.loader` e `~django.http.HttpResponse` (você vai querer manter `HttpResponse` se ainda tiver os métodos stub para `detail`, `results` e `vote`).

A função `~django.shortcuts.render` recebe o objeto de solicitação como seu primeiro argumento, um nome de template como seu segundo argumento e um dicionário como seu terceiro argumento opcional. Ele retorna um objeto `~django.http.HttpResponse` do template fornecido renderizado com o contexto fornecido.
