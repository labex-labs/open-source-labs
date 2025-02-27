# Dereferenciar un puntero crudo

En "Referencias colgantes", mencionamos que el compilador asegura que las referencias siempre son válidas. Rust inseguro tiene dos nuevos tipos llamados _punteros crudos_ que son similares a las referencias. Al igual que con las referencias, los punteros crudos pueden ser inmutables o mutables y se escriben como `*const T` y `*mut T`, respectivamente. El asterisco no es el operador de dereferencia; es parte del nombre del tipo. En el contexto de los punteros crudos, _inmutable_ significa que el puntero no se puede asignar directamente después de ser dereferenciado.

A diferencia de las referencias y los punteros inteligentes, los punteros crudos:

- Se permiten ignorar las reglas de préstamo al tener punteros inmutables y mutables o múltiples punteros mutables a la misma ubicación
- No está garantizado que apunten a memoria válida
- Se permite que sean nulos
- No implementan ninguna limpieza automática

Al optar por no tener que Rust enforce estas garantías, puedes renunciar a la seguridad garantizada a cambio de una mayor rendimiento o la capacidad de interactuar con otro lenguaje o hardware donde las garantías de Rust no se aplican.

La Lista 19-1 muestra cómo crear un puntero crudo inmutable y un puntero crudo mutable a partir de referencias.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;
```

Lista 19-1: Crear punteros crudos a partir de referencias

Observa que no incluimos la palabra clave `unsafe` en este código. Podemos crear punteros crudos en código seguro; solo no podemos dereferenciar punteros crudos fuera de un bloque `unsafe`, como verás enseguida.

Hemos creado punteros crudos usando `as` para convertir una referencia inmutable y una referencia mutable en sus tipos de puntero crudo correspondientes. Debido a que los creamos directamente a partir de referencias garantizadas como válidas, sabemos que estos punteros crudos particulares son válidos, pero no podemos hacer esa suposición sobre cualquier puntero crudo.

Para demostrar esto, a continuación crearemos un puntero crudo cuya validez no podemos estar tan seguros. La Lista 19-2 muestra cómo crear un puntero crudo a una ubicación arbitraria en la memoria. Intentar usar memoria arbitraria es indefinido: puede haber datos en esa dirección o puede que no, el compilador puede optimizar el código de modo que no haya acceso a memoria, o el programa puede terminar con un error de segmentación. Por lo general, no hay buena razón para escribir código así, pero es posible.

```rust
let address = 0x012345usize;
let r = address as *const i32;
```

Lista 19-2: Crear un puntero crudo a una dirección de memoria arbitraria

Recuerda que podemos crear punteros crudos en código seguro, pero no podemos _dereferenciar_ punteros crudos y leer los datos a los que apuntan. En la Lista 19-3, usamos el operador de dereferencia `*` en un puntero crudo que requiere un bloque `unsafe`.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

Lista 19-3: Dereferenciar punteros crudos dentro de un bloque `unsafe`

Crear un puntero no hace daño; solo cuando intentamos acceder al valor al que apunta es cuando es posible que terminemos tratando con un valor no válido.

Tenga en cuenta también que en las Listas 19-1 y 19-3, creamos punteros crudos `*const i32` y `*mut i32` que ambos apuntan a la misma ubicación de memoria, donde se almacena `num`. Si en cambio intentáramos crear una referencia inmutable y una referencia mutable a `num`, el código no se habría compilado porque las reglas de propiedad de Rust no permiten una referencia mutable al mismo tiempo que cualquier referencia inmutable. Con punteros crudos, podemos crear un puntero mutable y un puntero inmutable a la misma ubicación y cambiar los datos a través del puntero mutable, lo que puede crear una carrera de datos. ¡Ten cuidado!

Con todos estos peligros, ¿por qué usaría punteros crudos alguna vez? Un caso de uso principal es cuando se interactúa con código C, como verás en "Llamar a una función o método inseguro". Otro caso es cuando se construyen abstracciones seguras que el verificador de préstamos no entiende. Introduciremos funciones inseguras y luego veremos un ejemplo de una abstracción segura que utiliza código inseguro.
