# Pruebas adicionales

Este tutorial solo introduce algunos de los conceptos básicos de las pruebas. Hay mucho más que se puede hacer, y hay una serie de herramientas muy útiles a su disposición para lograr algunas cosas muy inteligentes.

Por ejemplo, mientras nuestras pruebas aquí han cubierto algo de la lógica interna de un modelo y la forma en que nuestras vistas publican información, puede usar un marco "en el navegador" como [Selenium](https://www.selenium.dev/) para probar la forma en que su HTML se renderiza realmente en un navegador. Estas herramientas le permiten comprobar no solo el comportamiento de su código de Django, sino también, por ejemplo, de su JavaScript. Es bastante impresionante ver cómo las pruebas inician un navegador y comienzan a interactuar con su sitio, como si una persona lo estuviera manejando. Django incluye `~django.test.LiveServerTestCase` para facilitar la integración con herramientas como Selenium.

Si tiene una aplicación compleja, es posible que desee ejecutar las pruebas automáticamente con cada confirmación con fines de [integración continua](https://en.wikipedia.org/wiki/Continuous_integration), de modo que el control de calidad sea, al menos en parte, automatizado.

Una buena manera de detectar las partes no probadas de su aplicación es comprobar la cobertura del código. Esto también ayuda a identificar código frágil o incluso código muerto. Si no puede probar un fragmento de código, generalmente significa que ese código debe refactorizarse o eliminarse. La cobertura ayudará a identificar el código muerto. Consulte `temas-pruebas-cobertura-del-código` para obtener detalles.

`Pruebas en Django </temas/pruebas/index>` tiene información detallada sobre las pruebas.
