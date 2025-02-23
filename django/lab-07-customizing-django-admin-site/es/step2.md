# Agregar objetos relacionados

Está bien, tenemos nuestra página de administración de `Question`, pero una `Question` tiene múltiples `Choice`, y la página de administración no muestra las opciones.

Todavía no.

Hay dos maneras de resolver este problema. La primera es registrar `Choice` con el administrador de la misma manera que hicimos con `Question`:

```python
from django.contrib import admin

from.models import Choice, Question

#...
admin.site.register(Choice)
```

Ahora, "Opciones" es una opción disponible en el administrador de Django. El formulario "Agregar opción" se ve así:

![Add Choice form interface](../assets/20230908-16-09-57-eCXIdjZu.png)

En ese formulario, el campo "Pregunta" es un cuadro de selección que contiene cada pregunta en la base de datos. Django sabe que un `~django.db.models.ForeignKey` debe representarse en el administrador como un `<select>`. En nuestro caso, solo existe una pregunta en este momento.

También observe el enlace "Agregar otra pregunta" junto a "Pregunta". Todo objeto con una relación `ForeignKey` con otro obtiene esto gratuitamente. Cuando haga clic en "Agregar otra pregunta", obtendrá una ventana emergente con el formulario "Agregar pregunta". Si agrega una pregunta en esa ventana y hace clic en "Guardar", Django guardará la pregunta en la base de datos y la agregará dinámicamente como la opción seleccionada en el formulario "Agregar opción" que está viendo.

Pero, en realidad, esta es una manera ineficiente de agregar objetos `Choice` al sistema. Sería mejor si pudiera agregar un montón de Opciones directamente cuando crea el objeto `Question`. Hagamos que eso suceda.

Quite la llamada `register()` para el modelo `Choice`. Luego, edite el código de registro de `Question` para que se lea:

```python
from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Información de fecha", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

Esto le dice a Django: "Los objetos `Choice` se editan en la página de administración de `Question`. Por defecto, proporcione suficientes campos para 3 opciones".

Cargue la página "Agregar pregunta" para ver cómo se ve:

![Question admin with choices](../assets/20230908-16-11-09-tVqaXrGB.png)

Funciona así: Hay tres espacios para Opciones relacionadas, como se especifica por `extra`, y cada vez que regrese a la página "Cambiar" para un objeto ya creado, obtendrá otros tres espacios adicionales.

Al final de los tres espacios actuales encontrará un enlace "Agregar otra Opción". Si hace clic en él, se agregará un nuevo espacio. Si desea eliminar el espacio agregado, puede hacer clic en la X en la esquina superior derecha del espacio agregado. Esta imagen muestra un espacio agregado:

![Additional slot added dynamically](../assets/admin14t.png)

Sin embargo, un pequeño problema. Se necesita mucho espacio en pantalla para mostrar todos los campos para ingresar objetos `Choice` relacionados. Por esa razón, Django ofrece una manera tabular de mostrar objetos relacionados en línea. Para usarlo, cambie la declaración `ChoiceInline` para que se lea:

```python
class ChoiceInline(admin.TabularInline):
 ...
```

Con ese `TabularInline` (en lugar de `StackedInline`), los objetos relacionados se muestran en un formato más compacto, basado en tablas:

![Tabular inline choices display](../assets/20230908-16-12-24-1nqRkbAI.png)

Tenga en cuenta que hay una columna adicional "¿Eliminar?" que permite eliminar las filas agregadas usando el botón "Agregar otra Opción" y las filas que ya se han guardado.
