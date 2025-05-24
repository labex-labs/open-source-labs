# Criando modelos

Agora, vamos definir seus modelos -- essencialmente, seu layout de banco de dados, com metadados adicionais.

Um modelo é a única fonte definitiva de informações sobre seus dados. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. Django segue o `Princípio DRY <dry>`. O objetivo é definir seu modelo de dados em um só lugar e derivar automaticamente as coisas dele.

Isso inclui as migrações - ao contrário do Ruby On Rails, por exemplo, as migrações são inteiramente derivadas do seu arquivo de modelos e são essencialmente um histórico que o Django pode percorrer para atualizar o esquema do seu banco de dados para corresponder aos seus modelos atuais.

Em nosso aplicativo de enquete, criaremos dois modelos: `Question` (Pergunta) e `Choice` (Escolha). Uma `Question` tem uma pergunta e uma data de publicação. Uma `Choice` tem dois campos: o texto da escolha e uma contagem de votos. Cada `Choice` está associada a uma `Question`.

Esses conceitos são representados por classes Python. Edite o arquivo `polls/models.py` para que ele se pareça com isto:

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Aqui, cada modelo é representado por uma classe que subclasse `django.db.models.Model`. Cada modelo tem um número de variáveis de classe, cada uma das quais representa um campo de banco de dados no modelo.

Cada campo é representado por uma instância de uma classe `~django.db.models.Field` -- por exemplo, `~django.db.models.CharField` para campos de caracteres e `~django.db.models.DateTimeField` para datas e horários. Isso informa ao Django que tipo de dados cada campo contém.

O nome de cada instância `~django.db.models.Field` (por exemplo, `question_text` ou `pub_date`) é o nome do campo, em formato amigável para a máquina. Você usará esse valor em seu código Python, e seu banco de dados o usará como o nome da coluna.

Você pode usar um primeiro argumento posicional opcional para um `~django.db.models.Field` para designar um nome legível por humanos. Isso é usado em algumas partes introspectivas do Django, e funciona como documentação. Se este campo não for fornecido, o Django usará o nome legível por máquina. Neste exemplo, definimos apenas um nome legível por humanos para `Question.pub_date`. Para todos os outros campos neste modelo, o nome legível por máquina do campo será suficiente como seu nome legível por humanos.

Algumas classes `~django.db.models.Field` têm argumentos obrigatórios. `~django.db.models.CharField`, por exemplo, exige que você forneça um `~django.db.models.CharField.max_length`. Isso é usado não apenas no esquema do banco de dados, mas na validação, como veremos em breve.

Um `~django.db.models.Field` também pode ter vários argumentos opcionais; neste caso, definimos o valor `~django.db.models.Field.default` de `votes` como 0.

Finalmente, observe que uma relação é definida, usando `~django.db.models.ForeignKey`. Isso informa ao Django que cada `Choice` está relacionada a uma única `Question`. Django suporta todos os relacionamentos comuns de banco de dados: muitos-para-um, muitos-para-muitos e um-para-um.
