# Use o sistema de templates

Voltando à view `detail()` para nossa aplicação de enquetes. Dada a variável de contexto `question`, aqui está como o template `polls/detail.html` pode ser:

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

O sistema de templates usa a sintaxe de busca por ponto para acessar atributos de variáveis. No exemplo de `{{ question.question_text }}`, primeiro o Django faz uma busca no dicionário no objeto `question`. Falhando nisso, ele tenta uma busca de atributo -- que funciona, neste caso. Se a busca de atributo tivesse falhado, ele teria tentado uma busca de índice de lista.

A chamada de método acontece no loop `{% for %}<for>`: `question.choice_set.all` é interpretado como o código Python `question.choice_set.all()`, que retorna um iterável de objetos `Choice` e é adequado para uso na tag `{% for %}<for>`.
