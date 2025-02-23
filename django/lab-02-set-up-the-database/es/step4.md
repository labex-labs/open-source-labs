# Jugando con la API

Ahora, vamos a entrar en el shell interactivo de Python y jugar con la API gratuita que Django le ofrece. Para invocar el shell de Python, use este comando:

```bash
python manage.py shell
```

Estamos usando esto en lugar de simplemente escribir "python", porque `manage.py` establece la variable de entorno `DJANGO_SETTINGS_MODULE`, que le da a Django la ruta de importación de Python a su archivo `mysite/settings.py`.

Una vez que estás en el shell, explora la `API de base de datos </topics/db/queries>`:

```python
>>> from polls.models import Choice, Question  # Importa las clases de modelo que acabamos de escribir.

# No hay preguntas en el sistema todavía.
>>> Question.objects.all()
<QuerySet []>

# Crea una nueva Pregunta.
# El soporte para zonas horarias está habilitado en el archivo de configuración predeterminado, por lo que
# Django espera una fecha y hora con tzinfo para pub_date. Use timezone.now()
# en lugar de datetime.datetime.now() y hará lo correcto.
>>> from django.utils import timezone
>>> q = Question(question_text="¿Qué hay de nuevo?", pub_date=timezone.now())

# Guarda el objeto en la base de datos. Tienes que llamar a save() explícitamente.
>>> q.save()

# Ahora tiene un ID.
>>> q.id
1

# Accede a los valores de los campos del modelo a través de atributos de Python.
>>> q.question_text
"¿Qué hay de nuevo?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# Cambia los valores cambiando los atributos, luego llama a save().
>>> q.question_text = "¿Qué pasa?"
>>> q.save()

# objects.all() muestra todas las preguntas en la base de datos.
>>> Question.objects.all()
<QuerySet [<Question: Pregunta objeto (1)>]>
```

Espera un minuto. `<Question: Pregunta objeto (1)>` no es una representación útil de este objeto. Vamos a arreglar eso editando el modelo `Question` (en el archivo `polls/models.py`) y agregando un método `~django.db.models.Model.__str__` a tanto `Question` como `Choice`:

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

Es importante agregar métodos `~django.db.models.Model.__str__` a sus modelos, no solo por su propia conveniencia al trabajar con el prompt interactivo, sino también porque las representaciones de los objetos se usan en todo el administrador automáticamente generado de Django.

Vamos a agregar también un método personalizado a este modelo:

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Tenga en cuenta la adición de `import datetime` y `from django.utils import timezone`, para referenciar el módulo `datetime` estándar de Python y las utilidades relacionadas con las zonas horarias de Django en `django.utils.timezone`, respectivamente. Si no está familiarizado con el manejo de zonas horarias en Python, puede aprender más en la `documentación de soporte de zonas horarias </topics/i18n/timezones>`.

Guarda estos cambios y comienza un nuevo shell interactivo de Python **ejecutando `python manage.py shell` nuevamente**:

```python
>>> from polls.models import Choice, Question

# Asegúrate de que nuestra adición de __str__() funcione.
>>> Question.objects.all()
<QuerySet [<Question: ¿Qué pasa?>]>

# Django proporciona una rica API de búsqueda de base de datos que está completamente impulsada por
# argumentos de palabras clave.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: ¿Qué pasa?>]>
>>> Question.objects.filter(question_text__startswith="¿Qué")
<QuerySet [<Question: ¿Qué pasa?>]>

# Obtén la pregunta que se publicó este año.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: ¿Qué pasa?>

# Solicita un ID que no existe, esto generará una excepción.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Pregunta que coincide con la consulta no existe.

# La búsqueda por clave primaria es el caso más común, por lo que Django proporciona un
# atajo para búsquedas exactas por clave primaria.
# Lo siguiente es idéntico a Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: ¿Qué pasa?>

# Asegúrate de que nuestro método personalizado funcione.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Da a la Pregunta un par de Elecciones. La llamada a create construye un nuevo
# objeto Choice, hace la instrucción INSERT, agrega la elección al conjunto
# de elecciones disponibles y devuelve el nuevo objeto Choice. Django crea
# un conjunto para mantener el "lado opuesto" de una relación ForeignKey
# (por ejemplo, las elecciones de una pregunta) que se puede acceder a través de la API.
>>> q = Question.objects.get(pk=1)

# Muestra cualquier elección del conjunto de objetos relacionados, ninguna hasta ahora.
>>> q.choice_set.all()
<QuerySet []>

# Crea tres elecciones.
>>> q.choice_set.create(choice_text="No mucho", votes=0)
<Choice: No mucho>
>>> q.choice_set.create(choice_text="El cielo", votes=0)
<Choice: El cielo>
>>> c = q.choice_set.create(choice_text="Volviendo a hackear", votes=0)

# Los objetos Choice tienen acceso a través de la API a sus objetos Question relacionados.
>>> c.question
<Question: ¿Qué pasa?>

# Y viceversa: Los objetos Question tienen acceso a los objetos Choice.
>>> q.choice_set.all()
<QuerySet [<Choice: No mucho>, <Choice: El cielo>, <Choice: Volviendo a hackear>]>
>>> q.choice_set.count()
3

# La API sigue automáticamente las relaciones tan lejos como sea necesario.
# Utiliza dos guiones bajos para separar las relaciones.
# Esto funciona tantos niveles de profundidad como desees; no hay límite.
# Encuentra todas las Elecciones para cualquier pregunta cuya pub_date esté en este año
# (reutilizando la variable 'current_year' que creamos anteriormente).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: No mucho>, <Choice: El cielo>, <Choice: Volviendo a hackear>]>

# Vamos a eliminar una de las elecciones. Usa delete() para eso.
>>> c = q.choice_set.filter(choice_text__startswith="Volviendo a hackear")
>>> c.delete()
```

Para obtener más información sobre las relaciones de modelo, consulte `Accediendo a objetos relacionados </ref/models/relations>`. Para más sobre cómo usar dos guiones bajos para realizar búsquedas de campos a través de la API, consulte `Búsquedas de campos <field-lookups-intro>`. Para obtener detalles completos sobre la API de base de datos, consulte nuestra `Referencia de API de base de datos </topics/db/queries>`.
