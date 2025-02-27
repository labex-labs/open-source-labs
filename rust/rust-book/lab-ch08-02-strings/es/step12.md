# Las cadenas no son tan simples

Para resumir, las cadenas son complicadas. Diferentes lenguajes de programación toman diferentes decisiones sobre cómo presentar esta complejidad al programador. Rust ha elegido hacer que el manejo correcto de los datos de `String` sea el comportamiento predeterminado para todos los programas de Rust, lo que significa que los programadores deben poner más atención en manejar los datos UTF-8 desde el principio. Esta compensación expone más de la complejidad de las cadenas que lo que es aparente en otros lenguajes de programación, pero te evita tener que manejar errores que involucren caracteres no ASCII más adelante en el ciclo de vida de tu desarrollo.

La buena noticia es que la biblioteca estándar ofrece mucha funcionalidad construida sobre los tipos `String` y `&str` para ayudar a manejar correctamente estas situaciones complejas. Asegúrate de revisar la documentación para métodos útiles como `contains` para buscar en una cadena y `replace` para sustituir partes de una cadena con otra cadena.

Pasemos a algo un poco menos complejo: los mapas hash.
