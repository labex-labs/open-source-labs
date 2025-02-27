# Memoria y asignación

En el caso de un literal de cadena, conocemos el contenido en tiempo de compilación, por lo que el texto se codifica directamente en el ejecutable final. Es por esto que los literales de cadena son rápidos y eficientes. Pero estas propiedades solo se derivan de la inmutabilidad del literal de cadena. Lamentablemente, no podemos poner un bloque de memoria en el binario para cada fragmento de texto cuyo tamaño es desconocido en tiempo de compilación y que puede cambiar mientras se ejecuta el programa.

Con el tipo `String`, para admitir un fragmento de texto mutable y creciente, necesitamos asignar una cantidad de memoria en el montón, desconocida en tiempo de compilación, para almacenar el contenido. Esto significa:

- La memoria debe solicitarse al asignador de memoria en tiempo de ejecución.
- Necesitamos una forma de devolver esta memoria al asignador cuando hayamos terminado con nuestro `String`.

La primera parte la hacemos nosotros: cuando llamamos a `String::from`, su implementación solicita la memoria que necesita. Esto es bastante común en los lenguajes de programación.

Sin embargo, la segunda parte es diferente. En los lenguajes con un _recolector de basura (GC)_, el GC lleva un seguimiento y limpia la memoria que ya no se está utilizando, y no tenemos que preocuparnos por ello. En la mayoría de los lenguajes sin GC, es nuestra responsabilidad identificar cuándo la memoria ya no se está utilizando y llamar a código para liberarla explícitamente, al igual que lo hicimos para solicitarla. Hacer esto correctamente históricamente ha sido un problema de programación difícil. Si olvidamos, desperdiciamos memoria. Si lo hacemos demasiado temprano, tendremos una variable inválida. Si lo hacemos dos veces, eso también es un error. Necesitamos emparejar exactamente una `asignación` con exactamente una `liberación`.

Rust sigue un camino diferente: la memoria se devuelve automáticamente una vez que la variable que la posee sale del ámbito. Aquí hay una versión de nuestro ejemplo de ámbito de la Lista 4-1 que utiliza un `String` en lugar de un literal de cadena:

    {
        let s = String::from("hello"); // s es válida a partir de este momento en adelante

        // haz cosas con s
    }                                  // este ámbito ha terminado, y s ya no es
                                       // válida

Hay un punto natural en el que podemos devolver la memoria que necesita nuestro `String` al asignador: cuando `s` sale del ámbito. Cuando una variable sale del ámbito, Rust llama a una función especial para nosotros. Esta función se llama `drop`, y es donde el autor de `String` puede poner el código para devolver la memoria. Rust llama a `drop` automáticamente en el corchete cerrado.

> Nota: En C++, este patrón de desasignar recursos al final de la vida útil de un elemento a veces se llama _Resource Acquisition Is Initialization_ _(RAII)_. La función `drop` en Rust te resultará familiar si has utilizado patrones RAII.

Este patrón tiene un impacto profundo en la forma en que se escribe el código de Rust. Puede parecer simple ahora, pero el comportamiento del código puede ser inesperado en situaciones más complicadas cuando queremos que múltiples variables usen los datos que hemos asignado en el montón. Ahora exploremos algunas de esas situaciones.
