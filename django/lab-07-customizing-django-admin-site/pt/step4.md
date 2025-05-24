# Personalizar a aparência e a sensação do admin

Claramente, ter "Administração do Django" no topo de cada página de administração é ridículo. É apenas texto de espaço reservado.

Você pode alterá-lo, no entanto, usando o sistema de templates do Django. O admin do Django é alimentado pelo próprio Django, e suas interfaces usam o sistema de templates do Django.

## Personalizando os templates do seu _projeto_

Crie um diretório `templates` no diretório do seu projeto (aquele que contém `manage.py`). Os templates podem residir em qualquer lugar no seu sistema de arquivos que o Django possa acessar. (O Django é executado como qualquer usuário que seu servidor execute.) No entanto, manter seus templates dentro do projeto é uma boa convenção a seguir.

Abra seu arquivo de configurações (`mysite/settings.py`, lembre-se) e adicione uma opção `DIRS <TEMPLATES-DIRS>` na configuração `TEMPLATES`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` é uma lista de diretórios do sistema de arquivos a serem verificados ao carregar templates do Django; é um caminho de pesquisa.

## Organizando templates

Assim como os arquivos estáticos, _poderíamos_ ter todos os nossos templates juntos, em um grande diretório de templates, e funcionaria perfeitamente bem. No entanto, os templates que pertencem a uma aplicação específica devem ser colocados no diretório de templates dessa aplicação (por exemplo, `polls/templates`) em vez do projeto (`templates`). Discutiremos em mais detalhes no `tutorial de aplicativos reutilizáveis </intro/reusable-apps>` _por que_ fazemos isso.

Agora, crie um diretório chamado `admin` dentro de `templates` e copie o template `admin/base_site.html` de dentro do diretório de templates padrão do admin do Django no código-fonte do próprio Django (`django/contrib/admin/templates`) para esse diretório.

## Onde estão os arquivos-fonte do Django?

Se você tiver dificuldade em encontrar onde os arquivos-fonte do Django estão localizados em seu sistema, execute o seguinte comando:

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

Em seguida, edite o arquivo e substitua `{{ site_header|default:_('Django administration') }}` (incluindo as chaves) pelo nome do seu próprio site, conforme achar adequado. Você deve acabar com uma seção de código como:

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

Usamos essa abordagem para ensinar como substituir templates. Em um projeto real, você provavelmente usaria o atributo `django.contrib.admin.AdminSite.site_header` para fazer essa personalização específica com mais facilidade.

Este arquivo de template contém muito texto como `{% block branding %}` e `{{ title }}`. As tags `{%` e `{{` fazem parte da linguagem de templates do Django. Quando o Django renderiza `admin/base_site.html`, essa linguagem de templates será avaliada para produzir a página HTML final, assim como vimos em `**Criando as Visualizações da Interface Pública**`.

Observe que qualquer um dos templates de administração padrão do Django pode ser substituído. Para substituir um template, faça a mesma coisa que você fez com `base_site.html` -- copie-o do diretório padrão para seu diretório personalizado e faça alterações.

## Personalizando os templates da sua _aplicação_

Leitores astutos perguntarão: Mas se `DIRS <TEMPLATES-DIRS>` estivesse vazio por padrão, como o Django estava encontrando os templates de administração padrão? A resposta é que, como `APP_DIRS <TEMPLATES-APP_DIRS>` está definido como `True`, o Django procura automaticamente um subdiretório `templates/` dentro de cada pacote de aplicação, para uso como fallback (não se esqueça que `django.contrib.admin` é uma aplicação).

Nossa aplicação de enquetes não é muito complexa e não precisa de templates de administração personalizados. Mas se ela se tornasse mais sofisticada e exigisse a modificação dos templates de administração padrão do Django para alguma de suas funcionalidades, seria mais sensato modificar os templates da _aplicação_, em vez daqueles do _projeto_. Dessa forma, você poderia incluir a aplicação de enquetes em qualquer novo projeto e ter a certeza de que ela encontraria os templates personalizados de que precisa.

Consulte a `documentação de carregamento de templates <template-loading>` para obter mais informações sobre como o Django encontra seus templates.
