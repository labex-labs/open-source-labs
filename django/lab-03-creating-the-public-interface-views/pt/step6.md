# Removendo URLs hardcoded em templates

Lembre-se que, quando escrevemos o link para uma pergunta no template `polls/index.html`, o link foi parcialmente hardcoded (codificado diretamente) assim:

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

O problema com essa abordagem hardcoded, fortemente acoplada, é que se torna desafiador alterar URLs em projetos com muitos templates. No entanto, como você definiu o argumento `name` nas funções `~django.urls.path` no módulo `polls.urls`, você pode remover a dependência de caminhos de URL específicos definidos em suas configurações de URL usando a tag de template `{% url %}`:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

A forma como isso funciona é procurando a definição da URL conforme especificado no módulo `polls.urls`. Você pode ver exatamente onde o nome da URL 'detail' é definido abaixo:

```python
# o valor 'name' como chamado pela tag de template {% url %}
path("<int:question_id>/", views.detail, name="detail"),
```

Se você quiser alterar a URL da view de detalhes das enquetes para outra coisa, talvez para algo como `polls/specifics/12/`, em vez de fazê-lo no template (ou templates), você a alteraria em `polls/urls.py`:

> Você não precisa alterar o template em absoluto.

```python
# adicionou a palavra 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
