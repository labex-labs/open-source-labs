# Probar una vista

La aplicación de sondeos es bastante permissiva: publicará cualquier pregunta, incluyendo aquellas cuyo campo `pub_date` está en el futuro. Debemos mejorar esto. Establecer un `pub_date` en el futuro debería significar que la Pregunta se publique en ese momento, pero sea invisible hasta entonces.

## Una prueba para una vista

Cuando corregimos el error anterior, escribimos la prueba primero y luego el código para corregirla. De hecho, eso fue un ejemplo de desarrollo dirigido por pruebas, pero en realidad no importa en qué orden hagamos el trabajo.

En nuestra primera prueba, nos centramos en el comportamiento interno del código. Para esta prueba, queremos comprobar su comportamiento tal como lo experimentaría un usuario a través de un navegador web.

Antes de intentar corregir algo, echemos un vistazo a las herramientas a nuestro alcance.

## El cliente de prueba de Django

Django proporciona un cliente de prueba `~django.test.Client` para simular la interacción de un usuario con el código en el nivel de vista. Lo podemos usar en `tests.py` o incluso en la `shell`.

Vamos a comenzar de nuevo con la `shell`, donde necesitamos hacer un par de cosas que no serán necesarias en `tests.py`. La primera es configurar el entorno de prueba en la `shell`:

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` instala un renderizador de plantillas que nos permitirá examinar algunos atributos adicionales en las respuestas, como `response.context`, que de lo contrario no estarían disponibles. Tenga en cuenta que este método _no_ configura una base de datos de prueba, por lo que lo siguiente se ejecutará contra la base de datos existente y la salida puede variar ligeramente dependiendo de las preguntas que ya haya creado. Es posible que obtenga resultados inesperados si su `TIME_ZONE` en `settings.py` no es correcta. Si no recuerda haberla configurado anteriormente, compruébela antes de continuar.

A continuación, necesitamos importar la clase del cliente de prueba (más adelante en `tests.py` usaremos la clase `django.test.TestCase`, que viene con su propio cliente, por lo que esto no será necesario):

```python
>>> from django.test import Client
>>> # crea una instancia del cliente para nuestro uso
>>> client = Client()
```

Con eso listo, podemos pedirle al cliente que haga algunos trabajos para nosotros:

```python
>>> # obtenga una respuesta de '/'
>>> response = client.get("/")
Not Found: /
>>> # deberíamos esperar un 404 de esa dirección; si en su lugar ve un
>>> # error "Invalid HTTP_HOST header" y una respuesta 400, es probable que
>>> # haya omitido la llamada a setup_test_environment() descrita anteriormente.
>>> response.status_code
404
>>> # por otro lado, deberíamos esperar encontrar algo en '/polls/'
>>> # usaremos'reverse()' en lugar de una URL codificada en duro
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## Mejora de nuestra vista

La lista de sondeos muestra sondeos que aún no se han publicado (es decir, aquellos que tienen un `pub_date` en el futuro). Vamos a corregir eso.

En `**Procesamiento de formularios y reducción de nuestro código**` introdujimos una vista basada en clases, basada en `~django.views.generic.list.ListView`:

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Devuelve las últimas cinco preguntas publicadas."""
        return Question.objects.order_by("-pub_date")[:5]
```

Debemos corregir el método `get_queryset()` y cambiarlo para que también verifique la fecha comparándola con `timezone.now()`. Primero debemos agregar una importación:

```python
from django.utils import timezone
```

y luego debemos corregir el método `get_queryset` de la siguiente manera:

```python
def get_queryset(self):
    """
    Devuelve las últimas cinco preguntas publicadas (sin incluir aquellas
    establecidas para ser publicadas en el futuro).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())` devuelve un conjunto de consultas que contiene `Question` cuya `pub_date` es menor o igual a, es decir, anterior o igual a, `timezone.now`.

## Prueba de nuestra nueva vista

Ahora puede comprobar que esto se comporta como se espera encendiendo `runserver`, cargando el sitio en su navegador, creando `Questions` con fechas en el pasado y el futuro y comprobando que solo se muestran aquellas que se han publicado. No quiere tener que hacer eso _cada vez que realice cualquier cambio que pueda afectar esto_, así que también creemos una prueba, basada en nuestra sesión de `shell` anterior.

Agregue lo siguiente a `polls/tests.py`:

```python
from django.urls import reverse
```

y crearemos una función atajo para crear preguntas así como una nueva clase de prueba:

```python
def create_question(question_text, days):
    """
    Crea una pregunta con el `question_text` dado y publicada el
    número dado de `días` desplazado hacia ahora (negativo para preguntas
    publicadas en el pasado, positivo para preguntas que aún no se han
    publicado).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Si no existen preguntas, se muestra un mensaje adecuado.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Las preguntas con un pub_date en el pasado se muestran en la
        página de índice.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Las preguntas con un pub_date en el futuro no se muestran en
        la página de índice.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Incluso si existen preguntas pasadas y futuras, solo se muestran
        las preguntas pasadas.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        La página de índice de preguntas puede mostrar múltiples preguntas.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

Echemos un vistazo más detenido a algunos de estos.

Primero está la función atajo de preguntas, `create_question`, para evitar repetir el proceso de creación de preguntas.

`test_no_questions` no crea ninguna pregunta, pero comprueba el mensaje: "No polls are available." y verifica que `latest_question_list` esté vacío. Tenga en cuenta que la clase `django.test.TestCase` proporciona algunos métodos de aserción adicionales. En estos ejemplos, usamos `~django.test.SimpleTestCase.assertContains()` y `~django.test.TransactionTestCase.assertQuerySetEqual()`.

En `test_past_question`, creamos una pregunta y verificamos que aparezca en la lista.

En `test_future_question`, creamos una pregunta con un `pub_date` en el futuro. La base de datos se reinicia para cada método de prueba, por lo que la primera pregunta ya no está allí, y por lo tanto el índice no debería tener ninguna pregunta en él.

Y así sucesivamente. En efecto, estamos usando las pruebas para contar una historia de la entrada del administrador y la experiencia del usuario en el sitio y comprobando que en cada estado y para cada nuevo cambio en el estado del sistema, se publiquen los resultados esperados.

## Prueba de la `DetailView`

Lo que tenemos funciona bien; sin embargo, aunque las preguntas futuras no aparecen en el _índice_, los usuarios aún pueden acceder a ellas si conocen o adivinan la URL correcta. Por lo tanto, necesitamos agregar una restricción similar a `DetailView`:

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        Excluye cualquier pregunta que aún no se haya publicado.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Luego deberíamos agregar algunas pruebas para comprobar que una `Question` cuya `pub_date` está en el pasado se puede mostrar y que una con un `pub_date` en el futuro no lo está:

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        La vista detallada de una pregunta con un pub_date en el futuro
        devuelve un 404 no encontrado.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        La vista detallada de una pregunta con un pub_date en el pasado
        muestra el texto de la pregunta.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## Ideas para más pruebas

Deberíamos agregar un método `get_queryset` similar a `ResultsView` y crear una nueva clase de prueba para esa vista. Será muy similar a lo que acabamos de crear; de hecho, habrá mucha repetición.

También podríamos mejorar nuestra aplicación de otras maneras, agregando pruebas en el camino. Por ejemplo, es tonto que se puedan publicar `Questions` en el sitio que no tienen `Choices`. Entonces, nuestras vistas podrían comprobar esto y excluir tales `Questions`. Nuestras pruebas crearían una `Question` sin `Choices` y luego probarían que no se publica, así como crear una `Question` similar _con_ `Choices` y probar que _sí_ se publica.

Tal vez los usuarios administradores autenticados deberían poder ver `Questions` no publicadas, pero no los visitantes ordinarios. Nuevamente: todo lo que se agregue al software para lograr esto debería ir acompañado de una prueba, ya sea que escriba la prueba primero y luego haga que el código pase la prueba, o que primero trabaje la lógica en su código y luego escriba una prueba para demostrarlo.

En cierto momento, seguro que mirará sus pruebas y se preguntará si su código está sufriendo de bloat de pruebas, lo que nos lleva a:
