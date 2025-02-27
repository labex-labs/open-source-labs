# RefCell`<T>`{=html} y el Patrón de Mutabilidad Interior

La _mutabilidad interior_ es un patrón de diseño en Rust que te permite mutar datos incluso cuando hay referencias inmutables a esos datos; normalmente, esta acción está prohibida por las reglas de préstamo. Para mutar datos, el patrón utiliza código `unsafe` dentro de una estructura de datos para desviar las reglas habituales de Rust que gobiernan la mutación y el préstamo. El código `unsafe` indica al compilador que estamos comprobando las reglas manualmente en lugar de confiar en que el compilador las compruebe por nosotros; discutiremos el código `unsafe` más en el Capítulo 19.

Sólo podemos utilizar tipos que usan el patrón de mutabilidad interior cuando podemos garantizar que se seguirán las reglas de préstamo en tiempo de ejecución, aunque el compilador no puede garantizarlo. El código `unsafe` implicado se envuelve entonces en una API segura, y el tipo externo sigue siendo inmutable.

Exploremos este concepto mirando el tipo `RefCell<T>` que sigue el patrón de mutabilidad interior.
