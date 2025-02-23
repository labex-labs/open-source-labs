# Creando modelos

Ahora definiremos nuestros modelos, esencialmente, la estructura de nuestra base de datos, con metadatos adicionales.

Un modelo es la única fuente definitiva de información sobre nuestros datos. Contiene los campos y comportamientos esenciales de los datos que estamos almacenando. Django sigue el `Principio DRY <dry>`. El objetivo es definir nuestro modelo de datos en un solo lugar y derivar automáticamente cosas a partir de él.

Esto incluye las migraciones: a diferencia de Ruby On Rails, por ejemplo, las migraciones se derivan enteramente de su archivo de modelos y son esencialmente una historia que Django puede revisar para actualizar su esquema de base de datos para que coincida con sus modelos actuales.

En nuestra aplicación de sondeo, crearemos dos modelos: `Question` (Pregunta) y `Choice` (Elección). Una `Pregunta` tiene una pregunta y una fecha de publicación. Una `Elección` tiene dos campos: el texto de la elección y un recuento de votos. Cada `Elección` está asociada a una `Pregunta`.

Estos conceptos se representan por clases de Python. Edite el archivo `polls/models.py` para que se vea así:

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

Aquí, cada modelo se representa por una clase que hereda de `django.db.models.Model`. Cada modelo tiene un número de variables de clase, cada una de las cuales representa un campo de base de datos en el modelo.

Cada campo se representa por una instancia de una clase `~django.db.models.Field`; por ejemplo, `~django.db.models.CharField` para campos de texto y `~django.db.models.DateTimeField` para fechas y horas. Esto le dice a Django qué tipo de datos almacena cada campo.

El nombre de cada instancia de `~django.db.models.Field` (por ejemplo, `question_text` o `pub_date`) es el nombre del campo, en un formato amigable para la máquina. Usará este valor en su código de Python y su base de datos lo usará como el nombre de la columna.

Puede usar un primer argumento posicional opcional para una `~django.db.models.Field` para designar un nombre legible para humanos. Eso se utiliza en un par de partes introspectivas de Django y también sirve como documentación. Si este campo no se proporciona, Django usará el nombre legible para la máquina. En este ejemplo, solo hemos definido un nombre legible para humanos para `Question.pub_date`. Para todos los demás campos de este modelo, el nombre legible para la máquina del campo será suficiente como nombre legible para humanos.

Algunas clases `~django.db.models.Field` tienen argumentos requeridos. `~django.db.models.CharField`, por ejemplo, requiere que le dé un `~django.db.models.CharField.max_length`. Eso se utiliza no solo en el esquema de base de datos, sino también en la validación, como veremos pronto.

Un `~django.db.models.Field` también puede tener varios argumentos opcionales; en este caso, hemos establecido el valor predeterminado `~django.db.models.Field.default` de `votes` en 0.

Finalmente, observe que se define una relación, usando `~django.db.models.ForeignKey`. Eso le dice a Django que cada `Elección` está relacionada con una sola `Pregunta`. Django admite todas las relaciones de base de datos comunes: muchos a uno, muchos a muchos y uno a uno.
