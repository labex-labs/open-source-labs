# Tipos Enteros

Un _entero_ (integer) es un número sin componente fraccionario. Usamos un tipo entero en el Capítulo 2, el tipo `u32`. Esta declaración de tipo indica que el valor asociado debe ser un entero sin signo (los tipos de enteros con signo comienzan con `i` en lugar de `u`) que ocupa 32 bits de espacio. La Tabla 3-1 muestra los tipos enteros integrados en Rust. Podemos usar cualquiera de estas variantes para declarar el tipo de un valor entero.

Tabla 3-1: Tipos Enteros en Rust

Longitud Con signo Sin signo

---

8 bits `i8` `u8`
16 bits `i16` `u16`
32 bits `i32` `u32`
64 bits `i64` `u64`
128 bits `i128` `u128`
arch `isize` `usize`

Cada variante puede ser con o sin signo y tiene un tamaño explícito. _Con signo_ (signed) y _sin signo_ (unsigned) se refieren a si es posible que el número sea negativo; en otras palabras, si el número necesita tener un signo (con signo) o si solo será positivo y, por lo tanto, puede representarse sin un signo (sin signo). Es como escribir números en papel: cuando el signo importa, un número se muestra con un signo más o un signo menos; sin embargo, cuando es seguro asumir que el número es positivo, se muestra sin signo. Los números con signo se almacenan utilizando la representación de complemento a dos (two's complement).

Cada variante con signo puede almacenar números desde -(2^(n-1)) hasta 2^(n-1) - 1 inclusive, donde _n_ es el número de bits que usa esa variante. Así, un `i8` puede almacenar números desde -(2^7) hasta 2^7 - 1, que es igual a -128 a 127. Las variantes sin signo pueden almacenar números desde 0 hasta 2^n - 1, por lo que un `u8` puede almacenar números desde 0 hasta 2^8 - 1, que es igual a 0 a 255.

Además, los tipos `isize` y `usize` dependen de la arquitectura de la computadora en la que se ejecuta su programa, lo que se denota en la tabla como "arch": 64 bits si está en una arquitectura de 64 bits y 32 bits si está en una arquitectura de 32 bits.

Puede escribir literales enteros en cualquiera de las formas que se muestran en la Tabla 3-2. Tenga en cuenta que los literales numéricos que pueden ser de múltiples tipos numéricos permiten un sufijo de tipo, como `57u8`, para designar el tipo. Los literales numéricos también pueden usar `_` como separador visual para que el número sea más fácil de leer, como `1_000`, que tendrá el mismo valor que si hubiera especificado `1000`.

Tabla 3-2: Literales Enteros en Rust

Literales numéricos Ejemplo

---

Decimal `98_222`
Hexadecimal `0xff`
Octal `0o77`
Binario `0b1111_0000`
Byte (solo `u8`) `b'A'`

Entonces, ¿cómo saber qué tipo de entero usar? Si no está seguro, los valores predeterminados de Rust son generalmente buenos lugares para comenzar: los tipos enteros por defecto son `i32`. La principal situación en la que usaría `isize` o `usize` es al indexar algún tipo de colección.

> **Desbordamiento de Entero (Integer Overflow)**
>
> Digamos que tiene una variable de tipo `u8` que puede contener valores entre 0 y 255. Si intenta cambiar la variable a un valor fuera de ese rango, como 256, ocurrirá un _desbordamiento de entero_ (integer overflow), lo que puede resultar en uno de dos comportamientos. Cuando está compilando en modo de depuración (debug), Rust incluye comprobaciones de desbordamiento de enteros que hacen que su programa entre en _pánico_ (panic) en tiempo de ejecución si ocurre este comportamiento. Rust usa el término _pánico_ (panicking) cuando un programa sale con un error; discutiremos los pánicos con más detalle en "Errores Irrecuperables con panic!".
>
> Cuando está compilando en modo de lanzamiento (release) con la bandera `--release`, Rust _no_ incluye comprobaciones de desbordamiento de enteros que causan pánicos. En cambio, si ocurre un desbordamiento, Rust realiza un _envoltorio de complemento a dos_ (two's complement wrapping). En resumen, los valores mayores que el valor máximo que el tipo puede contener "se envuelven" al mínimo de los valores que el tipo puede contener. En el caso de un `u8`, el valor 256 se convierte en 0, el valor 257 se convierte en 1, y así sucesivamente. El programa no entrará en pánico, pero la variable tendrá un valor que probablemente no sea el que esperaba que tuviera. Confiar en el comportamiento de envoltorio del desbordamiento de enteros se considera un error.
>
> Para manejar explícitamente la posibilidad de desbordamiento, puede usar estas familias de métodos proporcionadas por la biblioteca estándar para tipos numéricos primitivos:
>
> - Envolver en todos los modos con los métodos `wrapping_*`, como `wrapping_add`.
> - Devolver el valor `None` si hay desbordamiento con los métodos `checked_*`.
> - Devolver el valor y un booleano que indica si hubo desbordamiento con los métodos `overflowing_*`.
> - Saturar en los valores mínimo o máximo del valor con los métodos `saturating_*`.
