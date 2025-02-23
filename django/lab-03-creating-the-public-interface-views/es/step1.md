# Resumen

Una vista es un "tipo" de página web en su aplicación de Django que generalmente tiene una función específica y una plantilla específica. Por ejemplo, en una aplicación de blog, es posible que tenga las siguientes vistas:

- Página principal del blog: muestra las últimas entradas.
- Página de "detalles" de la entrada: página con enlace permanente para una sola entrada.
- Página de archivos basada en el año: muestra todos los meses con entradas en el año dado.
- Página de archivos basada en el mes: muestra todos los días con entradas en el mes dado.
- Página de archivos basada en el día: muestra todas las entradas del día dado.
- Acción de comentario: maneja la publicación de comentarios a una entrada determinada.

En nuestra aplicación de sondeo, tendremos las siguientes cuatro vistas:

- Página de "índice" de preguntas: muestra las últimas preguntas.
- Página de "detalles" de la pregunta: muestra el texto de una pregunta, sin resultados pero con un formulario para votar.
- Página de "resultados" de la pregunta: muestra los resultados de una pregunta en particular.
- Acción de voto: maneja el voto por una opción particular en una pregunta en particular.

En Django, las páginas web y otros contenidos se entregan por vistas. Cada vista está representada por una función de Python (o un método, en el caso de las vistas basadas en clases). Django elegirá una vista examinando la URL que se solicita (para ser precisos, la parte de la URL después del nombre de dominio).

Ahora, durante su tiempo en la web, es posible que haya encontrado hermosas URLs como `ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B`. Tendrá el agrado de saber que Django nos permite patrones de URL mucho más elegantes que eso.

Un patrón de URL es la forma general de una URL, por ejemplo: `/newsarchive/<year>/<month>/`.

Para pasar de una URL a una vista, Django utiliza lo que se conoce como 'URLconfs'. Un URLconf mapea patrones de URL a vistas.

Este tutorial proporciona instrucciones básicas sobre el uso de URLconfs, y puede consultar `/topics/http/urls` para obtener más información.
