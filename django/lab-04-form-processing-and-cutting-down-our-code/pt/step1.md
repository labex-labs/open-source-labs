# Escreva um formulário mínimo

Vamos atualizar nosso template de detalhes da enquete (`polls/detail.html`) do último tutorial, para que o template contenha um elemento HTML `<form>`:

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

Uma rápida análise:

- O template acima exibe um botão de rádio para cada opção da pergunta. O `value` de cada botão de rádio é o ID da opção da pergunta associada. O `name` de cada botão de rádio é `"choice"`. Isso significa que, quando alguém seleciona um dos botões de rádio e envia o formulário, ele enviará os dados POST `choice=#`, onde # é o ID da opção selecionada. Este é o conceito básico de formulários HTML.
- Definimos o `action` do formulário como `{% url 'polls:vote' question.id %}`, e definimos `method="post"`. Usar `method="post"` (em oposição a `method="get"`) é muito importante, porque o ato de enviar este formulário alterará dados no lado do servidor. Sempre que você criar um formulário que altera dados no lado do servidor, use `method="post"`. Esta dica não é específica do Django; é uma boa prática de desenvolvimento web em geral.
- `forloop.counter` indica quantas vezes a tag `for` passou por seu loop
- Como estamos criando um formulário POST (que pode ter o efeito de modificar dados), precisamos nos preocupar com Cross Site Request Forgeries. Felizmente, você não precisa se preocupar muito, porque o Django vem com um sistema útil para se proteger contra isso. Em resumo, todos os formulários POST que são direcionados a URLs internas devem usar a tag de template `{% csrf_token %}<csrf_token>`.

Agora, vamos criar uma view do Django que lida com os dados enviados e faz algo com eles. Lembre-se, em `**Criando as Visões da Interface Pública**`, criamos um URLconf para a aplicação de enquetes que inclui esta linha:

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

Também criamos uma implementação dummy da função `vote()`. Vamos criar uma versão real. Adicione o seguinte a `polls/views.py`:

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

Este código inclui algumas coisas que ainda não cobrimos neste tutorial:

- `request.POST <django.http.HttpRequest.POST>` é um objeto semelhante a um dicionário que permite acessar dados enviados por nome de chave. Neste caso, `request.POST['choice']` retorna o ID da opção selecionada, como uma string. Os valores de `request.POST <django.http.HttpRequest.POST>` são sempre strings.

  Observe que o Django também fornece `request.GET
<django.http.HttpRequest.GET>` para acessar dados GET da mesma forma - mas estamos usando explicitamente `request.POST
<django.http.HttpRequest.POST>` em nosso código, para garantir que os dados sejam alterados apenas por meio de uma chamada POST.

- `request.POST['choice']` levantará `KeyError` se `choice` não foi fornecido nos dados POST. O código acima verifica `KeyError` e exibe novamente o formulário da pergunta com uma mensagem de erro se `choice` não for fornecido.

- Após incrementar a contagem de opções, o código retorna um `~django.http.HttpResponseRedirect` em vez de um `~django.http.HttpResponse` normal. `~django.http.HttpResponseRedirect` recebe um único argumento: a URL para a qual o usuário será redirecionado (veja o ponto seguinte para saber como construímos a URL neste caso).

  Como o comentário em Python acima aponta, você sempre deve retornar um `~django.http.HttpResponseRedirect` após lidar com sucesso com os dados POST. Esta dica não é específica do Django; é uma boa prática de desenvolvimento web em geral.

- Estamos usando a função `~django.urls.reverse` no construtor `~django.http.HttpResponseRedirect` neste exemplo. Esta função ajuda a evitar ter que codificar uma URL no código da view. Ela recebe o nome da view para a qual queremos passar o controle e a parte variável do padrão de URL que aponta para essa view. Neste caso, usando o URLconf que configuramos em `**Criando as Visões da Interface Pública**`, esta chamada `~django.urls.reverse` retornará uma string como:

      "/polls/3/results/"

  onde o `3` é o valor de `question.id`. Esta URL redirecionada então chamará a view `'results'` para exibir a página final.

Como mencionado em `**Criando as Visões da Interface Pública**`, `request` é um objeto `~django.http.HttpRequest`. Para mais informações sobre objetos `~django.http.HttpRequest`, consulte a `documentação de request and
response </ref/request-response>`.

Depois que alguém vota em uma pergunta, a view `vote()` redireciona para a página de resultados da pergunta. Vamos escrever essa view:

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

Esta é quase exatamente a mesma da view `detail()` de **Criando as Visões da Interface Pública**. A única diferença é o nome do template. Vamos corrigir essa redundância mais tarde.

Agora, crie um template `polls/results.html`:

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

Agora, vá para `/polls/1/` no seu navegador e vote na pergunta. Você deve ver uma página de resultados que é atualizada cada vez que você vota. Se você enviar o formulário sem ter escolhido uma opção, você deve ver a mensagem de erro.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![Poll voting form interface](../assets/20230908-10-37-07-p9ewKbe6.png)

**Observação:**

O código para nossa view `vote()` tem um pequeno problema. Ele primeiro obtém o objeto `selected_choice` do banco de dados, então calcula o novo valor de `votes` e, em seguida, o salva de volta no banco de dados. Se dois usuários do seu site tentarem votar _exatamente ao mesmo tempo_, isso pode dar errado: O mesmo valor, digamos 42, será recuperado para `votes`. Então, para ambos os usuários, o novo valor de 43 é calculado e salvo, mas 44 seria o valor esperado.

Isso é chamado de _condição de corrida_ (race condition). Se você estiver interessado, pode ler `avoiding-race-conditions-using-f` para aprender como você pode resolver esse problema.
