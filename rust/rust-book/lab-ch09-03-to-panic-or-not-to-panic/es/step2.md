# Ejemplos, código de prototipo y pruebas

Cuando estás escribiendo un ejemplo para ilustrar algún concepto, incluir también código de manejo de errores robusto puede hacer que el ejemplo sea menos claro. En los ejemplos, se entiende que una llamada a un método como `unwrap` que podría causar un bloqueo es un marcador temporal para la forma en que quieres que tu aplicación maneje los errores, lo cual puede variar según lo que haga el resto de tu código.

Del mismo modo, los métodos `unwrap` y `expect` son muy útiles durante el prototipado, antes de que estés listo para decidir cómo manejar los errores. Dejan marcas claras en tu código para cuando estés listo para hacer que tu programa sea más robusto.

Si una llamada a un método falla en una prueba, querrás que toda la prueba falle, incluso si ese método no es la funcionalidad que se está probando. Debido a que `panic!` es la forma en que una prueba se marca como fallida, llamar a `unwrap` o `expect` es exactamente lo que debería suceder.
