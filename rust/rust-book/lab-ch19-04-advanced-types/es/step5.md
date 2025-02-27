# Tipos de tamaño dinámico y el trato Sized

Rust necesita conocer ciertos detalles sobre sus tipos, como cuánto espacio asignar para un valor de un tipo particular. Esto deja un rincón de su sistema de tipos un poco confuso al principio: el concepto de _tipos de tamaño dinámico_. A veces se les llama _DST_ o _tipos sin tamaño_, estos tipos nos permiten escribir código usando valores cuyo tamaño solo podemos conocer en tiempo de ejecución.

Vamos a profundizar en los detalles de un tipo de tamaño dinámico llamado `str`, que hemos estado usando en todo el libro. Eso's correcto, no `&str`, sino `str` por sí mismo, es un DST. No podemos saber cuánto largo es la cadena hasta el tiempo de ejecución, lo que significa que no podemos crear una variable de tipo `str`, ni podemos tomar un argumento de tipo `str`. Considere el siguiente código, que no funciona:

```rust
let s1: str = "Hello there!";
let s2: str = "How's it going?";
```

Rust necesita saber cuánta memoria asignar para cualquier valor de un tipo particular, y todos los valores de un tipo deben usar la misma cantidad de memoria. Si Rust nos permitiera escribir este código, estos dos valores de `str` necesitarían ocupar la misma cantidad de espacio. Pero tienen longitudes diferentes: `s1` necesita 12 bytes de almacenamiento y `s2` necesita 15. Por eso no es posible crear una variable que contenga un tipo de tamaño dinámico.

Entonces, ¿qué hacemos? En este caso, ya sabes la respuesta: hacemos que los tipos de `s1` y `s2` sean un `&str` en lugar de un `str`. Recuerda de "Fragmentos de cadena" que la estructura de datos de fragmento solo almacena la posición de inicio y la longitud del fragmento. Entonces, aunque un `&T` es un solo valor que almacena la dirección de memoria donde se encuentra el `T`, un `&str` es _dos_ valores: la dirección del `str` y su longitud. Como tal, podemos conocer el tamaño de un valor de `&str` en tiempo de compilación: es el doble de la longitud de un `usize`. Es decir, siempre conocemos el tamaño de un `&str`, sin importar cuánto largo sea la cadena a la que se refiere. En general, esta es la forma en que se usan los tipos de tamaño dinámico en Rust: tienen un poco adicional de metadatos que almacenan el tamaño de la información dinámica. La regla aureola de los tipos de tamaño dinámico es que siempre debemos poner valores de tipos de tamaño dinámico detrás de un puntero de algún tipo.

Podemos combinar `str` con todo tipo de punteros: por ejemplo, `Box<str>` o `Rc<str>`. De hecho, ya has visto esto antes pero con un tipo de tamaño dinámico diferente: los rasgos. Cada rasgo es un tipo de tamaño dinámico al que podemos referirnos usando el nombre del rasgo. En "Usando objetos de rasgo que permiten valores de diferentes tipos", mencionamos que para usar los rasgos como objetos de rasgo, debemos ponerlos detrás de un puntero, como `&dyn Trait` o `Box<dyn Trait>` (`Rc<dyn Trait>` también funcionaría).

Para trabajar con DSTs, Rust proporciona el trato `Sized` para determinar si el tamaño de un tipo es conocido en tiempo de compilación. Este trato se implementa automáticamente para todo aquello cuyo tamaño es conocido en tiempo de compilación. Además, Rust agrega implícitamente un límite en `Sized` a cada función genérica. Es decir, una definición de función genérica como esta:

```rust
fn genérico<T>(t: T) {
    --snip--
}
```

en realidad se trata como si hubiéramos escrito esto:

```rust
fn genérico<T: Sized>(t: T) {
    --snip--
}
```

Por defecto, las funciones genéricas solo funcionarán con tipos que tienen un tamaño conocido en tiempo de compilación. Sin embargo, puedes usar la siguiente sintaxis especial para relajar esta restricción:

```rust
fn genérico<T:?Sized>(t: &T) {
    --snip--
}
```

Un límite de rasgo en `?Sized` significa "`T` puede o no ser `Sized`" y esta notación anula el predeterminado de que los tipos genéricos deben tener un tamaño conocido en tiempo de compilación. La sintaxis `?Rasgo` con este significado solo está disponible para `Sized`, no para ningún otro rasgo.

También ten en cuenta que cambiamos el tipo del parámetro `t` de `T` a `&T`. Debido a que el tipo puede no ser `Sized`, necesitamos usarlo detrás de algún tipo de puntero. En este caso, hemos elegido una referencia.

A continuación, hablaremos sobre funciones y closures!
