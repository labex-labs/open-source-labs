# Concurrencia de Estado Compartido

El paso de mensajes es una forma adecuada de manejar la concurrencia, pero no es la única. Otro método sería que múltiples subprocesos accedan a los mismos datos compartidos. Consideremos nuevamente esta parte del eslogan de la documentación del lenguaje Go: "No comunique mediante la compartición de memoria".

¿Cómo sería comunicarse mediante la compartición de memoria? Además, ¿por qué los entusiastas del paso de mensajes recomiendan no utilizar la compartición de memoria?

De cierto modo, los canales en cualquier lenguaje de programación son similares a la propiedad única, ya que una vez que se transfiere un valor a través de un canal, ya no se debe utilizar ese valor. La concurrencia de memoria compartida es como la propiedad múltiple: múltiples subprocesos pueden acceder a la misma ubicación de memoria al mismo tiempo. Como viste en el Capítulo 15, donde los punteros inteligentes hicieron posible la propiedad múltiple, la propiedad múltiple puede agregar complejidad porque estos diferentes propietarios necesitan ser administrados. El sistema de tipos y las reglas de propiedad de Rust ayudan en gran medida a que esta administración sea correcta. Para un ejemplo, veamos los mutex, uno de los primitivos de concurrencia más comunes para la memoria compartida.
