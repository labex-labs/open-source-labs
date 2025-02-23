# Personalizar el formulario de administración

Al registrar el modelo `Question` con `admin.site.register(Question)`, Django fue capaz de construir una representación predeterminada del formulario. A menudo, querrás personalizar cómo se ve y funciona el formulario de administración. Lo harás indicando a Django las opciones que quieres cuando registras el objeto.

Veamos cómo funciona reordenando los campos en el formulario de edición. Reemplaza la línea `admin.site.register(Question)` con:

Edita el archivo `~/project/mysite/polls/admin.py` para que se vea así:

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

Seguirás este patrón: crear una clase de administración de modelo y luego pasarla como segundo argumento a `admin.site.register()` cada vez que necesites cambiar las opciones de administración de un modelo.

Ejecuta el servidor de desarrollo de Django:

```bash
cd ~/project/mysite
python manage.py runserver
```

Abre `http://127.0.0.1:8000/admin/` en Firefox del Entorno de Escritorio y haz clic en el enlace "Questions". Deberías ver un formulario que se ve así.

Este cambio en particular hace que la "Fecha de publicación" aparezca antes del campo "Question":

![Admin form field reorder](../assets/20230908-16-06-41-wiBfnHS8.png)

Esto no es impresionante con solo dos campos, pero para formularios de administración con docenas de campos, elegir un orden intuitivo es un detalle de usabilidad importante.

Y hablando de formularios con docenas de campos, es posible que desees dividir el formulario en conjuntos de campos:

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Información de fecha", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

El primer elemento de cada tupla en `~django.contrib.admin.ModelAdmin.fieldsets` es el título del conjunto de campos. Así se ve nuestro formulario ahora:

![Admin form with fieldsets](../assets/20230908-16-08-19-HOzMJWFG.png)
