# Ventajas y Desventajas del Patrón de Estado

Hemos demostrado que Rust es capaz de implementar el patrón de estado orientado a objetos para encapsular los diferentes tipos de comportamiento que una publicación debería tener en cada estado. Los métodos en `Post` no saben nada sobre los diversos comportamientos. Con la forma en que organizamos el código, solo tenemos que buscar en un solo lugar para conocer las diferentes maneras en que una publicación publicada puede comportarse: la implementación del trato `State` en la estructura `Published`.

Si tuviéramos que crear una implementación alternativa que no utilizara el patrón de estado, en lugar de eso podríamos usar expresiones `match` en los métodos de `Post` o incluso en el código de `main` que comprueba el estado de la publicación y cambia el comportamiento en esos lugares. Eso significaría que tendríamos que buscar en varios lugares para entender todas las implicaciones de una publicación estar en el estado publicado. Esto solo aumentaría a medida que agregáramos más estados: cada una de esas expresiones `match` necesitaría otro brazo.

Con el patrón de estado, los métodos de `Post` y los lugares donde usamos `Post` no necesitan expresiones `match`, y para agregar un nuevo estado, solo necesitaríamos agregar una nueva estructura y implementar los métodos del trato en esa sola estructura.

La implementación que utiliza el patrón de estado es fácil de extender para agregar más funcionalidad. Para ver la simplicidad de mantener el código que utiliza el patrón de estado, prueba algunas de estas sugerencias:

- Agrega un método `rechazar` que cambie el estado de la publicación de `PendingReview` de vuelta a `Draft`.
- Requiere dos llamadas a `aprobar` antes de que el estado pueda cambiar a `Publicado`.
- Permite a los usuarios agregar contenido de texto solo cuando una publicación está en el estado `Draft`. Consejo: haz que el objeto de estado sea responsable de lo que podría cambiar en el contenido pero no responsable de modificar `Post`.

Una desventaja del patrón de estado es que, debido a que los estados implementan las transiciones entre estados, algunos de los estados están acoplados entre sí. Si agregamos otro estado entre `PendingReview` y `Publicado`, como `Programado`, tendríamos que cambiar el código en `PendingReview` para que transite a `Programado` en lugar. Sería menos trabajo si `PendingReview` no tuviera que cambiar con la adición de un nuevo estado, pero eso significaría cambiar a otro patrón de diseño.

Otra desventaja es que hemos duplicado algo de lógica. Para eliminar algo de la duplicación, podríamos intentar hacer implementaciones predeterminadas para los métodos `request_review` y `approve` en el trato `State` que devuelvan `self`. Sin embargo, esto no funcionaría: cuando se utiliza `State` como un objeto de trato, el trato no sabe exactamente cuál será el `self` concrete, por lo que el tipo de retorno no es conocido en tiempo de compilación.

Otra duplicación incluye las implementaciones similares de los métodos `request_review` y `approve` en `Post`. Ambos métodos delegan en la implementación del mismo método en el valor del campo `state` de `Option` y establecen el nuevo valor del campo `state` en el resultado. Si tuviéramos muchos métodos en `Post` que siguieran este patrón, podríamos considerar definir una macro para eliminar la repetición (ver "Macros").

Al implementar exactamente el patrón de estado como está definido para los lenguajes orientados a objetos, no estamos aprovechando al máximo las fortalezas de Rust como podríamos. Echemos un vistazo a algunos cambios que podemos hacer en el crat `blog` que pueden convertir los estados e transiciones no válidas en errores de tiempo de compilación.
