# Personalizar la lista de cambios del administrador

Ahora que la página de administración de Preguntas se ve bien, hagamos algunos ajustes en la página de "lista de cambios", la que muestra todas las preguntas en el sistema.

Así se ve en este momento:

![Polls change list page](../assets/admin04t.png)

Por defecto, Django muestra la `str()` de cada objeto. Pero a veces sería más útil si pudiéramos mostrar campos individuales. Para hacer eso, use la opción de administración `~django.contrib.admin.ModelAdmin.list_display`, que es una tupla de nombres de campos a mostrar, como columnas, en la página de lista de cambios del objeto:

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date"]
```

Para estar seguros, también incluyamos el método `was_published_recently()` de `**Configurar la base de datos**`:

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

Ahora la página de lista de cambios de preguntas se ve así:

![Question change list view](../assets/20230908-16-14-08-GNY2lggF.png)

Puede hacer clic en los encabezados de columna para ordenar por esos valores, excepto en el caso del encabezado `was_published_recently`, porque no se admite ordenar por la salida de un método arbitrario. También observe que el encabezado de columna de `was_published_recently` es, por defecto, el nombre del método (con los guiones bajos reemplazados por espacios), y que cada línea contiene la representación de cadena de la salida.

Puede mejorarlo usando el decorador `~django.contrib.admin.display` en ese método (en `polls/models.py`), como sigue:

```python
from django.contrib import admin


class Question(models.Model):
    #...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="¿Publicado recientemente?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Para obtener más información sobre las propiedades configurables a través del decorador, consulte `~django.contrib.admin.ModelAdmin.list_display`.

Edite nuevamente su archivo `polls/admin.py` y agregue una mejora a la página de lista de cambios de `Question`: filtros usando `~django.contrib.admin.ModelAdmin.list_filter`. Agregue la siguiente línea a `QuestionAdmin`:

```python
list_filter = ["pub_date"]
```

Eso agrega una barra lateral de "Filtros" que permite a las personas filtrar la lista de cambios por el campo `pub_date`:

![Admin list filter sidebar](../assets/20230908-16-16-39-otfMNyYo.png)

El tipo de filtro que se muestra depende del tipo de campo en el que se está filtrando. Debido a que `pub_date` es un `~django.db.models.DateTimeField`, Django sabe dar opciones de filtro adecuadas: "Cualquier fecha", "Hoy", "Últimos 7 días", "Este mes", "Este año".

Esto está quedando muy bien. Agreguemos alguna capacidad de búsqueda:

```python
search_fields = ["question_text"]
```

Eso agrega una caja de búsqueda en la parte superior de la lista de cambios. Cuando alguien ingresa términos de búsqueda, Django buscará en el campo `question_text`. Puede usar tantos campos como desee, aunque como utiliza una consulta `LIKE` en segundo plano, limitar el número de campos de búsqueda a un número razonable hará que sea más fácil para su base de datos realizar la búsqueda.

Ahora también es un buen momento para señalar que las listas de cambios le dan paginación gratuita. El predeterminado es mostrar 100 elementos por página. `Paginación de la lista de cambios
<django.contrib.admin.ModelAdmin.list_per_page>`, `cajas de búsqueda
<django.contrib.admin.ModelAdmin.search_fields>`, `filtros
<django.contrib.admin.ModelAdmin.list_filter>`, `jerarquías de fechas
<django.contrib.admin.ModelAdmin.date_hierarchy>` y `ordenamiento de encabezados de columna <django.contrib.admin.ModelAdmin.list_display>` todos funcionan juntos como usted esperaría que lo hicieran.
