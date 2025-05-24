# Personalizar o formulário de administração

Ao registrar o modelo `Question` com `admin.site.register(Question)`, o Django foi capaz de construir uma representação de formulário padrão. Frequentemente, você desejará personalizar a aparência e o funcionamento do formulário de administração. Você fará isso informando ao Django as opções desejadas ao registrar o objeto.

Vamos ver como isso funciona reordenando os campos no formulário de edição. Substitua a linha `admin.site.register(Question)` por:

Edite o arquivo `~/project/mysite/polls/admin.py` para que fique assim:

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

Você seguirá este padrão -- crie uma classe de administração de modelo (model admin class), depois passe-a como o segundo argumento para `admin.site.register()` -- sempre que precisar alterar as opções de administração para um modelo.

Execute o servidor de desenvolvimento Django:

```bash
cd ~/project/mysite
python manage.py runserver
```

Abra `http://127.0.0.1:8000/admin/` no Firefox ou no Ambiente de Trabalho (Desktop Environment) e clique no link "Questions". Você deve ver um formulário que se parece com este.

Esta alteração específica acima faz com que a "Data de publicação" (Publication date) venha antes do campo "Pergunta" (Question):

![Admin form field reorder](../assets/20230908-16-06-41-wiBfnHS8.png)

Isso não é impressionante com apenas dois campos, mas para formulários de administração com dezenas de campos, escolher uma ordem intuitiva é um detalhe importante de usabilidade.

E falando em formulários com dezenas de campos, você pode querer dividir o formulário em fieldsets:

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

O primeiro elemento de cada tupla em `~django.contrib.admin.ModelAdmin.fieldsets` é o título do fieldset. Veja como nosso formulário se parece agora:

![Admin form with fieldsets](../assets/20230908-16-08-19-HOzMJWFG.png)
