# Adicionando objetos relacionados

OK, temos nossa página de administração de `Question`, mas uma `Question` tem múltiplas `Choice`s, e a página de administração não exibe as escolhas.

Ainda não.

Existem duas maneiras de resolver este problema. A primeira é registrar `Choice` com o admin, assim como fizemos com `Question`:

```python
from django.contrib import admin

from .models import Choice, Question

# ...
admin.site.register(Choice)
```

Agora "Choices" é uma opção disponível no admin do Django. O formulário "Adicionar escolha" (Add choice) se parece com isto:

![Add Choice form interface](../assets/20230908-16-09-57-eCXIdjZu.png)

Nesse formulário, o campo "Question" é uma caixa de seleção contendo todas as perguntas no banco de dados. O Django sabe que um `~django.db.models.ForeignKey` deve ser representado no admin como uma caixa `<select>`. Em nosso caso, apenas uma pergunta existe neste ponto.

Observe também o link "Adicionar outra pergunta" (Add another question) ao lado de "Question". Cada objeto com um relacionamento `ForeignKey` com outro recebe isso gratuitamente. Quando você clica em "Adicionar outra pergunta", você obterá uma janela pop-up com o formulário "Adicionar pergunta". Se você adicionar uma pergunta nessa janela e clicar em "Salvar", o Django salvará a pergunta no banco de dados e a adicionará dinamicamente como a escolha selecionada no formulário "Adicionar escolha" que você está vendo.

Mas, na verdade, esta é uma maneira ineficiente de adicionar objetos `Choice` ao sistema. Seria melhor se você pudesse adicionar um monte de Choices diretamente quando criar o objeto `Question`. Vamos fazer isso acontecer.

Remova a chamada `register()` para o modelo `Choice`. Em seguida, edite o código de registro `Question` para ler:

```python
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

Isso diz ao Django: "Objetos `Choice` são editados na página de administração de `Question`. Por padrão, forneça campos suficientes para 3 escolhas."

Carregue a página "Adicionar pergunta" para ver como isso fica:

![Question admin with choices](../assets/20230908-16-11-09-tVqaXrGB.png)

Funciona assim: Existem três slots para Choices relacionadas -- conforme especificado por `extra` -- e cada vez que você volta para a página "Alterar" (Change) para um objeto já criado, você recebe mais três slots extras.

No final dos três slots atuais, você encontrará um link "Adicionar outra Choice" (Add another Choice). Se você clicar nele, um novo slot será adicionado. Se você quiser remover o slot adicionado, você pode clicar no X no canto superior direito do slot adicionado. Esta imagem mostra um slot adicionado:

![Additional slot added dynamically](../assets/admin14t.png)

Um pequeno problema, no entanto. Leva muito espaço na tela para exibir todos os campos para inserir objetos `Choice` relacionados. Por essa razão, o Django oferece uma maneira tabular de exibir objetos relacionados inline. Para usá-lo, altere a declaração `ChoiceInline` para ler:

```python
class ChoiceInline(admin.TabularInline):
    ...
```

Com esse `TabularInline` (em vez de `StackedInline`), os objetos relacionados são exibidos em um formato mais compacto, baseado em tabela:

![Tabular inline choices display](../assets/20230908-16-12-24-1nqRkbAI.png)

Observe que há uma coluna extra "Excluir?" (Delete?) que permite remover linhas adicionadas usando o botão "Adicionar outra Choice" e linhas que já foram salvas.
