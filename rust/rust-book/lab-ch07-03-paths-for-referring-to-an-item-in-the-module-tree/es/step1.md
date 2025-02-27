# Rutas para Referirse a un Elemento en el Árbol de Módulos

Para indicar a Rust dónde encontrar un elemento en el árbol de módulos, usamos una ruta de la misma manera en que usamos una ruta al navegar por un sistema de archivos. Para llamar a una función, necesitamos conocer su ruta.

Una ruta puede tomar dos formas:

- Una _ruta absoluta_ es la ruta completa que comienza en la raíz del crat; para el código de un crat externo, la ruta absoluta comienza con el nombre del crat, y para el código del crat actual, comienza con el literal `crate`.
- Una _ruta relativa_ comienza desde el módulo actual y utiliza `self`, `super` o un identificador en el módulo actual.

Tanto las rutas absolutas como las relativas se siguen con uno o más identificadores separados por dos puntos dobles (`::`).

Volviendo a la Lista 7-1, digamos que queremos llamar a la función `add_to_waitlist`. Esto es lo mismo que preguntar: ¿cuál es la ruta de la función `add_to_waitlist`? La Lista 7-3 contiene la Lista 7-1 con algunos de los módulos y funciones eliminados.

Mostraremos dos maneras de llamar a la función `add_to_waitlist` desde una nueva función, `eat_at_restaurant`, definida en la raíz del crat. Estas rutas son correctas, pero queda otro problema que evitará que este ejemplo se compile tal como está. Lo explicaré un poco más adelante.

La función `eat_at_restaurant` es parte de la API pública de nuestro crat de biblioteca, por lo que la marcamos con la palabra clave `pub`. En "Exponiendo Rutas con la Palabra Clave pub", entraremos en más detalle sobre `pub`.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Ruta absoluta
    crate::front_of_house::hosting::add_to_waitlist();

    // Ruta relativa
    front_of_house::hosting::add_to_waitlist();
}
```

Lista 7-3: Llamando a la función `add_to_waitlist` usando rutas absolutas y relativas

La primera vez que llamamos a la función `add_to_waitlist` en `eat_at_restaurant`, usamos una ruta absoluta. La función `add_to_waitlist` está definida en el mismo crat que `eat_at_restaurant`, lo que significa que podemos usar la palabra clave `crate` para comenzar una ruta absoluta. Luego incluimos cada uno de los módulos sucesivos hasta llegar a `add_to_waitlist`. Puedes imaginar un sistema de archivos con la misma estructura: especificaríamos la ruta `/front_of_house/hosting/add_to_waitlist` para ejecutar el programa `add_to_waitlist`; usar el nombre del `crate` para comenzar desde la raíz del crat es como usar `/` para comenzar desde la raíz del sistema de archivos en tu shell.

La segunda vez que llamamos a `add_to_waitlist` en `eat_at_restaurant`, usamos una ruta relativa. La ruta comienza con `front_of_house`, el nombre del módulo definido en el mismo nivel del árbol de módulos que `eat_at_restaurant`. Aquí, el equivalente en el sistema de archivos sería usar la ruta `front_of_house/hosting/add_to_waitlist`. Comenzar con el nombre de un módulo significa que la ruta es relativa.

Decidir si usar una ruta relativa o absoluta es una decisión que tomarás en función de tu proyecto y depende de si es más probable que muevas el código de definición de elementos por separado o junto con el código que usa el elemento. Por ejemplo, si movemos el módulo `front_of_house` y la función `eat_at_restaurant` a un módulo llamado `customer_experience`, tendremos que actualizar la ruta absoluta a `add_to_waitlist`, pero la ruta relativa todavía sería válida. Sin embargo, si movemos la función `eat_at_restaurant` por separado a un módulo llamado `dining`, la ruta absoluta a la llamada `add_to_waitlist` permanecería igual, pero la ruta relativa tendría que actualizarse. En general, nuestra preferencia es especificar rutas absolutas porque es más probable que queramos mover las definiciones de código y las llamadas a elementos independientemente entre sí.

Intentemos compilar la Lista 7-3 y averigüemos por qué todavía no se compilará. Los errores que obtenemos se muestran en la Lista 7-4.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: module `hosting` is private
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ private module
  |
note: the module `hosting` is defined here
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: module `hosting` is private
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ private module
   |
note: the module `hosting` is defined here
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

Lista 7-4: Errores del compilador al compilar el código de la Lista 7-3

Los mensajes de error dicen que el módulo `hosting` es privado. En otras palabras, tenemos las rutas correctas para el módulo `hosting` y la función `add_to_waitlist`, pero Rust no nos permite usarlas porque no tiene acceso a las secciones privadas. En Rust, todos los elementos (funciones, métodos, structs, enums, módulos y constantes) son privados para los módulos padre por defecto. Si quieres hacer que un elemento como una función o un struct sea privado, lo pones en un módulo.

Los elementos en un módulo padre no pueden usar los elementos privados dentro de los módulos hijos, pero los elementos en los módulos hijos pueden usar los elementos en sus módulos ancestros. Esto se debe a que los módulos hijos envuelven y ocultan sus detalles de implementación, pero los módulos hijos pueden ver el contexto en el que están definidos. Para continuar con nuestra metáfora, piensa en las reglas de privacidad como si fueran la oficina trasera de un restaurante: lo que pasa allí es privado para los clientes del restaurante, pero los gerentes de oficina pueden ver y hacer todo en el restaurante que administran.

Rust decidió que el sistema de módulos funcione de esta manera para que ocultar los detalles de implementación internos sea el comportamiento predeterminado. De esta manera, sabes qué partes del código interno puedes cambiar sin romper el código externo. Sin embargo, Rust te da la opción de exponer las partes internas del código de los módulos hijos a los módulos ancestros externos usando la palabra clave `pub` para hacer un elemento público.
