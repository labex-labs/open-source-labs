# Brincando com a API

Agora, vamos entrar no shell interativo do Python e brincar com a API gratuita que o Django oferece. Para invocar o shell do Python, use este comando:

```bash
python manage.py shell
```

Estamos usando isso em vez de simplesmente digitar "python", porque `manage.py` define a variável de ambiente `DJANGO_SETTINGS_MODULE`, que fornece ao Django o caminho de importação Python para o seu arquivo `mysite/settings.py`.

Depois de entrar no shell, explore a `API do banco de dados </topics/db/queries>`:

```python
>>> from polls.models import Choice, Question  # Importe as classes de modelo que acabamos de escrever.

# Nenhuma pergunta está no sistema ainda.
>>> Question.objects.all()
<QuerySet []>

# Crie uma nova Pergunta.
# O suporte para fusos horários está habilitado no arquivo de configurações padrão, então
# Django espera um datetime com tzinfo para pub_date. Use timezone.now()
# em vez de datetime.datetime.now() e ele fará a coisa certa.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Salve o objeto no banco de dados. Você deve chamar save() explicitamente.
>>> q.save()

# Agora ele tem um ID.
>>> q.id
1

# Acesse os valores dos campos do modelo via atributos Python.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# Altere os valores alterando os atributos e, em seguida, chamando save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() exibe todas as perguntas no banco de dados.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Espere um minuto. `<Question: Question object (1)>` não é uma representação útil deste objeto. Vamos corrigir isso editando o modelo `Question` (no arquivo `polls/models.py`) e adicionando um método `~django.db.models.Model.__str__` a `Question` e `Choice`:

```python
from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

É importante adicionar métodos `~django.db.models.Model.__str__` aos seus modelos, não apenas para sua própria conveniência ao lidar com o prompt interativo, mas também porque as representações dos objetos são usadas em toda a administração gerada automaticamente do Django.

Vamos também adicionar um método personalizado a este modelo:

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Observe a adição de `import datetime` e `from django.utils import timezone`, para referenciar o módulo `datetime` padrão do Python e os utilitários relacionados ao fuso horário do Django em `django.utils.timezone`, respectivamente. Se você não estiver familiarizado com o tratamento de fuso horário no Python, pode aprender mais nos `documentos de suporte ao fuso horário </topics/i18n/timezones>`.

Salve essas alterações e inicie um novo shell interativo do Python **executando `python manage.py shell` novamente**:

```python
>>> from polls.models import Choice, Question

# Certifique-se de que nossa adição __str__() funcionou.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django fornece uma rica API de pesquisa de banco de dados que é totalmente impulsionada por
# argumentos de palavra-chave.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Obtenha a pergunta que foi publicada este ano.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Solicite um ID que não existe, isso levantará uma exceção.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# A pesquisa por uma chave primária é o caso mais comum, então o Django fornece um
# atalho para pesquisas exatas de chave primária.
# O seguinte é idêntico a Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Certifique-se de que nosso método personalizado funcionou.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Dê à Pergunta algumas Escolhas. A chamada create constrói um novo
# Objeto Choice, faz a instrução INSERT, adiciona a escolha ao conjunto
# de escolhas disponíveis e retorna o novo objeto Choice. Django cria
# um conjunto para conter o "outro lado" de uma relação ForeignKey
# (por exemplo, a escolha de uma pergunta) que pode ser acessada via API.
>>> q = Question.objects.get(pk=1)

# Exiba quaisquer escolhas do conjunto de objetos relacionados -- nenhum até agora.
>>> q.choice_set.all()
<QuerySet []>

# Crie três escolhas.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Os objetos Choice têm acesso à API aos seus objetos Question relacionados.
>>> c.question
<Question: What's up?>

# E vice-versa: os objetos Question obtêm acesso aos objetos Choice.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# A API segue automaticamente as relações até onde você precisa.
# Use sublinhados duplos para separar relacionamentos.
# Isso funciona em quantos níveis você quiser; não há limite.
# Encontre todas as Escolhas para qualquer pergunta cuja pub_date esteja neste ano
# (reutilizando a variável 'current_year' que criamos acima).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Vamos excluir uma das escolhas. Use delete() para isso.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

Para obter mais informações sobre as relações de modelo, consulte `Acessando objetos relacionados
</ref/models/relations>`. Para obter mais informações sobre como usar sublinhados duplos para realizar pesquisas de campo via API, consulte `Pesquisas de campo <field-lookups-intro>`. Para obter detalhes completos sobre a API do banco de dados, consulte nossa `referência da API do banco de dados
</topics/db/queries>`.
