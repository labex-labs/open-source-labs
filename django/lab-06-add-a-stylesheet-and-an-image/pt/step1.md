# Personalize a aparência do seu _app_

Primeiramente, crie um diretório chamado `static` no seu diretório `polls`. O Django procurará arquivos estáticos lá, de forma semelhante a como o Django encontra templates dentro de `polls/templates/`.

A configuração `STATICFILES_FINDERS` do Django contém uma lista de finders que sabem como descobrir arquivos estáticos de várias fontes. Um dos padrões é `AppDirectoriesFinder`, que procura um subdiretório "static" em cada um dos `INSTALLED_APPS`, como o que acabamos de criar em `polls`. O site de administração usa a mesma estrutura de diretórios para seus arquivos estáticos.

Dentro do diretório `static` que você acabou de criar, crie outro diretório chamado `polls` e, dentro dele, crie um arquivo chamado `style.css`. Em outras palavras, sua folha de estilo deve estar em `polls/static/polls/style.css`. Devido à forma como o finder de arquivos estáticos `AppDirectoriesFinder` funciona, você pode se referir a este arquivo estático no Django como `polls/style.css`, de forma semelhante a como você referencia o caminho para templates.

## Namespacing de arquivos estáticos

Assim como os templates, _poderíamos_ nos safar colocando nossos arquivos estáticos diretamente em `polls/static` (em vez de criar outro subdiretório `polls`), mas na verdade seria uma má ideia. O Django escolherá o primeiro arquivo estático que encontrar cujo nome corresponda, e se você tivesse um arquivo estático com o mesmo nome em uma aplicação _diferente_, o Django seria incapaz de distinguir entre eles. Precisamos ser capazes de apontar o Django para o correto, e a melhor maneira de garantir isso é _namespacing_ eles. Ou seja, colocando esses arquivos estáticos dentro de _outro_ diretório nomeado para a própria aplicação.

Coloque o seguinte código nessa folha de estilo (`polls/static/polls/style.css`):

```css
li a {
  color: green;
}
```

Em seguida, adicione o seguinte no topo de `polls/templates/polls/index.html`:

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

A tag de template `{% static %}` gera a URL absoluta de arquivos estáticos.

Isso é tudo o que você precisa fazer para desenvolvimento.

Inicie o servidor (ou reinicie-o se já estiver em execução):

```bash
python manage.py runserver 0.0.0.0:8080
```

Recarregue a aba **Web 8080** e você deverá ver que os links das perguntas estão verdes (estilo Django!), o que significa que sua folha de estilo foi carregada corretamente.

![green question links example](../assets/20230908-15-29-11-ztyI1umP.png)
