# Tipos Enteros

Un _entero_ es un número sin componente fraccionaria. Usamos un tipo entero en el Capítulo 2, el tipo `u32`. Esta declaración de tipo indica que el valor con el que está asociado debe ser un entero sin signo (los tipos de enteros con signo empiezan con `i` en lugar de `u`) que ocupa 32 bits de espacio. La Tabla 3-1 muestra los tipos enteros integrados en Rust. Podemos usar cualquiera de estas variantes para declarar el tipo de un valor entero.

Tabla 3-1: Tipos Enteros en Rust

## Longitud Con signo Sin signo

8 bits `i8` `u8`
16 bits `i16` `u16`
32 bits `i32` `u32`
64 bits `i64` `u64`
128 bits `i128` `u128`
arquitectura `isize` `usize`

Cada variante puede ser con signo o sin signo y tiene un tamaño explícito. _Con signo_ y _sin signo_ se refieren a si es posible que el número sea negativo, es decir, si el número necesita tener un signo (con signo) o si solo será positivo y por lo tanto puede representarse sin signo (sin signo). Es como escribir números en papel: cuando el signo importa, un número se muestra con un signo más o un signo menos; sin embargo, cuando es seguro asumir que el número es positivo, se muestra sin signo. Los números con signo se almacenan usando representación de complemento a dos.

Cada variante con signo puede almacenar números desde -(2`<sup>`{=html}n - 1`</sup>`{=html}) hasta 2`<sup>`{=html}n - 1`</sup>`{=html} - 1 inclusive, donde _n_ es el número de bits que utiliza esa variante. Entonces, un `i8` puede almacenar números desde -(2`<sup>`{=html}7`</sup>`{=html}) hasta 2`<sup>`{=html}7`</sup>`{=html} - 1, lo que equivale a -128 a 127. Las variantes sin signo pueden almacenar números desde 0 hasta 2`<sup>`{=html}n`</sup>`{=html} - 1, por lo que un `u8` puede almacenar números desde 0 hasta 2`<sup>`{=html}8`</sup>`{=html} - 1, lo que equivale a 0 a 255.

Además, los tipos `isize` y `usize` dependen de la arquitectura de la computadora en la que se está ejecutando su programa, lo que se denota en la tabla como "arquitectura": 64 bits si está en una arquitectura de 64 bits y 32 bits si está en una arquitectura de 32 bits.

Puedes escribir literales enteros en cualquiera de las formas mostradas en la Tabla 3-2. Tenga en cuenta que los literales numéricos que pueden ser de múltiples tipos numéricos permiten un sufijo de tipo, como `57u8`, para designar el tipo. Los literales numéricos también pueden usar `_` como separador visual para que el número sea más fácil de leer, como `1_000`, que tendrá el mismo valor que si hubieras especificado `1000`.

Tabla 3-2: Literales Enteros en Rust

## Literales numéricos Ejemplo

Decimal `98_222`
Hexadecimal `0xff`
Octal `0o77`
Binario `0b1111_0000`
Byte (`u8` solo) `b'A'`

Entonces, ¿cómo sabes qué tipo de entero usar? Si no estás seguro, generalmente es buena idea empezar con los valores predeterminados de Rust: los tipos enteros por defecto son `i32`. La principal situación en la que usarías `isize` o `usize` es cuando estás indexando algún tipo de colección.

> **Desbordamiento de Enteros**
>
> Digamos que tienes una variable de tipo `u8` que puede contener valores entre 0 y 255. Si intentas cambiar la variable a un valor fuera de ese rango, como 256, se producirá un _desbordamiento de enteros_, lo que puede dar lugar a uno de dos comportamientos. Cuando se compila en modo depuración, Rust incluye comprobaciones para el desbordamiento de enteros que hacen que tu programa _se detenga abruptamente_ en tiempo de ejecución si este comportamiento ocurre. Rust utiliza el término _abrupta detención_ cuando un programa sale con un error; discutiremos las abruptas detención con más detalle en "Errores irreparables con panic!".
>
> Cuando se compila en modo lanzamiento con la bandera `--release`, Rust _no_ incluye comprobaciones para el desbordamiento de enteros que causan abruptas detención. En cambio, si ocurre un desbordamiento, Rust realiza un _envuelve con complemento a dos_. En resumen, los valores mayores que el valor máximo que el tipo puede contener "se vuelven" al mínimo de los valores que el tipo puede contener. En el caso de un `u8`, el valor 256 se convierte en 0, el valor 257 se convierte en 1, y así sucesivamente. El programa no se detendrá abruptamente, pero la variable tendrá un valor que probablemente no sea el que esperabas que tuviera. Confiar en el comportamiento de envuelve del desbordamiento de enteros se considera un error.
>
> Para manejar explícitamente la posibilidad de desbordamiento, puedes usar estas familias de métodos proporcionados por la biblioteca estándar para los tipos numéricos primitivos:
>
> - Envuelve en todos los modos con los métodos `wrapping_*`, como `wrapping_add`.
> - Devuelve el valor `None` si hay desbordamiento con los métodos `checked_*`.
> - Devuelve el valor y un booleano que indica si hubo desbordamiento con los métodos `overflowing_*`.
> - Satura en los valores mínimo o máximo del valor con los métodos `saturating_*`.
