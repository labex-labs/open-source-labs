# Personalizar a lista de alterações do admin

Agora que a página de administração de Question está com boa aparência, vamos fazer alguns ajustes na página de "lista de alterações" (change list) -- aquela que exibe todas as perguntas no sistema.

Veja como ela se parece neste ponto:

![Polls change list page](../assets/admin04t.png)

Por padrão, o Django exibe o `str()` de cada objeto. Mas, às vezes, seria mais útil se pudéssemos exibir campos individuais. Para fazer isso, use a opção de administração `~django.contrib.admin.ModelAdmin.list_display`, que é uma tupla de nomes de campos a serem exibidos, como colunas, na página de lista de alterações do objeto:

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date"]
```

Para garantir, vamos também incluir o método `was_published_recently()` de `**Configurar o Banco de Dados**`:

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

Agora, a página de lista de alterações da pergunta se parece com isto:

![Question change list view](../assets/20230908-16-14-08-GNY2lggF.png)

Você pode clicar nos cabeçalhos das colunas para classificar por esses valores -- exceto no caso do cabeçalho `was_published_recently`, porque a classificação pela saída de um método arbitrário não é suportada. Observe também que o cabeçalho da coluna para `was_published_recently` é, por padrão, o nome do método (com sublinhados substituídos por espaços), e que cada linha contém a representação de string da saída.

Você pode melhorar isso usando o decorador `~django.contrib.admin.display` nesse método (em `polls/models.py`), da seguinte forma:

```python
from django.contrib import admin


class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Para obter mais informações sobre as propriedades configuráveis por meio do decorador, consulte `~django.contrib.admin.ModelAdmin.list_display`.

Edite seu arquivo `polls/admin.py` novamente e adicione uma melhoria à página de lista de alterações de `Question`: filtros usando `~django.contrib.admin.ModelAdmin.list_filter`. Adicione a seguinte linha a `QuestionAdmin`:

```python
list_filter = ["pub_date"]
```

Isso adiciona uma barra lateral "Filtro" (Filter) que permite que as pessoas filtrem a lista de alterações pelo campo `pub_date`:

![Admin list filter sidebar](../assets/20230908-16-16-39-otfMNyYo.png)

O tipo de filtro exibido depende do tipo de campo que você está filtrando. Como `pub_date` é um `~django.db.models.DateTimeField`, o Django sabe dar opções de filtro apropriadas: "Qualquer data", "Hoje", "Últimos 7 dias", "Este mês", "Este ano".

Isso está tomando forma. Vamos adicionar alguma capacidade de pesquisa:

```python
search_fields = ["question_text"]
```

Isso adiciona uma caixa de pesquisa na parte superior da lista de alterações. Quando alguém insere termos de pesquisa, o Django pesquisará o campo `question_text`. Você pode usar quantos campos quiser -- embora, como ele usa uma consulta `LIKE` nos bastidores, limitar o número de campos de pesquisa a um número razoável tornará mais fácil para seu banco de dados fazer a pesquisa.

Agora também é um bom momento para observar que as listas de alterações fornecem paginação gratuita. O padrão é exibir 100 itens por página. `Paginação da lista de alterações
<django.contrib.admin.ModelAdmin.list_per_page>`, `caixas de pesquisa
<django.contrib.admin.ModelAdmin.search_fields>`, `filtros
<django.contrib.admin.ModelAdmin.list_filter>`, `hierarquias de data
<django.contrib.admin.ModelAdmin.date_hierarchy>` e `ordenação de cabeçalho de coluna <django.contrib.admin.ModelAdmin.list_display>` funcionam juntos como você pensa que deveriam.
