# Escrevendo nosso primeiro teste

## Identificamos um bug

Felizmente, há um pequeno bug na aplicação `polls` para corrigirmos imediatamente: o método `Question.was_published_recently()` retorna `True` se a `Question` foi publicada no último dia (o que está correto), mas também se o campo `pub_date` da `Question` está no futuro (o que certamente não está).

Confirme o bug usando o `shell` para verificar o método em uma pergunta cuja data está no futuro:

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```

Como as coisas no futuro não são 'recentes', isso está claramente errado.

## Crie um teste para expor o bug

O que acabamos de fazer no `shell` para testar o problema é exatamente o que podemos fazer em um teste automatizado, então vamos transformá-lo em um teste automatizado.

Um local convencional para os testes de uma aplicação é no arquivo `tests.py` da aplicação; o sistema de teste encontrará automaticamente testes em qualquer arquivo cujo nome comece com `test`.

Coloque o seguinte no arquivo `tests.py` na aplicação `polls`:

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Aqui, criamos uma subclasse `django.test.TestCase` com um método que cria uma instância `Question` com um `pub_date` no futuro. Em seguida, verificamos a saída de `was_published_recently()` - que _deveria_ ser False.

## Executando testes

No terminal, podemos executar nosso teste:

```bash
python manage.py test polls
```

e você verá algo como:

```shell
[object Object]
```

> Erro diferente?

Se, em vez disso, você estiver recebendo um `NameError` aqui, pode ter perdido uma etapa em `Parte 2 <tutorial02-import-timezone>` onde adicionamos importações de `datetime` e `timezone` para `polls/models.py`. Copie as importações dessa seção e tente executar seus testes novamente.

O que aconteceu foi o seguinte:

- `manage.py test polls` procurou testes na aplicação `polls`
- encontrou uma subclasse da classe `django.test.TestCase`
- criou um banco de dados especial para fins de teste
- procurou métodos de teste - aqueles cujos nomes começam com `test`
- em `test_was_published_recently_with_future_question`, criou uma instância `Question` cujo campo `pub_date` está 30 dias no futuro
- ... e usando o método `assertIs()`, descobriu que seu `was_published_recently()` retorna `True`, embora quiséssemos que retornasse `False`

O teste nos informa qual teste falhou e até mesmo a linha em que a falha ocorreu.

## Corrigindo o bug

Já sabemos qual é o problema: `Question.was_published_recently()` deve retornar `False` se seu `pub_date` estiver no futuro. Modifique o método em `models.py` para que ele retorne `True` somente se a data também estiver no passado:

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

e execute o teste novamente:

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

Depois de identificar um bug, escrevemos um teste que o expõe e corrigimos o bug no código para que nosso teste passe.

Muitas outras coisas podem dar errado com nossa aplicação no futuro, mas podemos ter certeza de que não reintroduziremos inadvertidamente esse bug, porque a execução do teste nos avisará imediatamente. Podemos considerar esta pequena parte da aplicação fixada com segurança para sempre.

## Testes mais abrangentes

Enquanto estamos aqui, podemos fixar ainda mais o método `was_published_recently()`; na verdade, seria positivamente embaraçoso se, ao corrigir um bug, tivéssemos introduzido outro.

Adicione mais dois métodos de teste à mesma classe, para testar o comportamento do método de forma mais abrangente:

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

E agora temos três testes que confirmam que `Question.was_published_recently()` retorna valores sensatos para perguntas passadas, recentes e futuras.

Novamente, `polls` é uma aplicação mínima, mas por mais complexa que ela se torne no futuro e com qualquer outro código com o qual ela interaja, agora temos alguma garantia de que o método para o qual escrevemos testes se comportará da maneira esperada.
