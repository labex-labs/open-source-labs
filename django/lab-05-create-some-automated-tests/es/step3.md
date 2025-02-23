# Escribiendo nuestra primera prueba

## Identificamos un error

Afortunadamente, hay un pequeño error en la aplicación `polls` que podemos corregir inmediatamente: el método `Question.was_published_recently()` devuelve `True` si la `Question` se publicó dentro del último día (lo cual es correcto), pero también si el campo `pub_date` de la `Question` está en el futuro (lo cual ciertamente no es).

Confirme el error usando la `shell` para comprobar el método en una pregunta cuya fecha está en el futuro:

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # crea una instancia de Question con pub_date 30 días en el futuro
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # ¿se publicó recientemente?
>>> future_question.was_published_recently()
True
```

Como las cosas en el futuro no son'recientes', esto está claramente mal.

## Creamos una prueba para detectar el error

Lo que acabamos de hacer en la `shell` para probar el problema es exactamente lo que podemos hacer en una prueba automatizada, así que convertámoslo en una prueba automatizada.

Un lugar convencional para las pruebas de una aplicación es en el archivo `tests.py` de la aplicación; el sistema de prueba buscará automáticamente las pruebas en cualquier archivo cuyo nombre comience con `test`.

Coloque lo siguiente en el archivo `tests.py` de la aplicación `polls`:

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() devuelve False para preguntas cuya pub_date
        está en el futuro.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Aquí hemos creado una subclase de `django.test.TestCase` con un método que crea una instancia de `Question` con un `pub_date` en el futuro. Luego comprobamos la salida de `was_published_recently()` - que _debería_ ser False.

## Ejecutando las pruebas

En la terminal, podemos ejecutar nuestra prueba:

```bash
python manage.py test polls
```

y verá algo como:

```shell
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

> ¿Error diferente?

Si en su lugar está recibiendo un `NameError` aquí, es posible que haya omitido un paso en la `Parte 2 <tutorial02-import-timezone>` donde agregamos las importaciones de `datetime` y `timezone` a `polls/models.py`. Copie las importaciones de esa sección y vuelva a intentar ejecutar sus pruebas.

Lo que pasó es lo siguiente:

- `manage.py test polls` buscó pruebas en la aplicación `polls`
- encontró una subclase de la clase `django.test.TestCase`
- creó una base de datos especial con el propósito de probar
- buscó métodos de prueba, aquellos cuyo nombre comienza con `test`
- en `test_was_published_recently_with_future_question` creó una instancia de `Question` cuyo campo `pub_date` está 30 días en el futuro
  -... y usando el método `assertIs()`, descubrió que su `was_published_recently()` devuelve `True`, aunque queríamos que devolviera `False`

La prueba nos informa cuál prueba falló e incluso la línea en la que ocurrió el error.

## Corrigiendo el error

Ya sabemos cuál es el problema: `Question.was_published_recently()` debería devolver `False` si su `pub_date` está en el futuro. Amende el método en `models.py` para que solo devuelva `True` si la fecha también está en el pasado:

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

y ejecute la prueba nuevamente:

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

Después de identificar un error, escribimos una prueba que lo expone y corregimos el error en el código para que nuestra prueba pase.

Muchas otras cosas pueden salir mal con nuestra aplicación en el futuro, pero podemos estar seguros de que no volveremos a introducir inadvertidamente este error, porque ejecutar la prueba nos advertirá inmediatamente. Podemos considerar esta pequeña parte de la aplicación fijada de manera segura para siempre.

## Pruebas más exhaustivas

Mientras estamos aquí, podemos fijar aún más el método `was_published_recently()`; de hecho, sería vergonzoso si al corregir un error hubiéramos introducido otro.

Agregue dos métodos de prueba más a la misma clase para probar el comportamiento del método de manera más exhaustiva:

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() devuelve False para preguntas cuya pub_date
    es anterior a 1 día.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() devuelve True para preguntas cuya pub_date
    está dentro del último día.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

Y ahora tenemos tres pruebas que confirman que `Question.was_published_recently()` devuelve valores sensatos para preguntas pasadas, recientes y futuras.

Nuevamente, `polls` es una aplicación mínima, pero sin importar cuán compleja crezca en el futuro y con cualquier otro código con el que interactúe, ahora tenemos alguna garantía de que el método para el que escribimos pruebas se comportará de manera esperada.
