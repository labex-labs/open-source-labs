# Macros Declarativas con macro_rules! para Metaprogramación General

La forma más utilizada de macros en Rust es la macro _declarativa_. A veces también se les conoce como "macros por ejemplo", "macros `macro_rules!`" o simplemente "macros". En esencia, las macros declarativas te permiten escribir algo similar a una expresión `match` de Rust. Como se discutió en el Capítulo 6, las expresiones `match` son estructuras de control que toman una expresión, comparan el valor resultante de la expresión con patrones y luego ejecutan el código asociado con el patrón coincidente. Las macros también comparan un valor con patrones que están asociados con código particular: en esta situación, el valor es el código fuente literal de Rust pasado a la macro; los patrones se comparan con la estructura de ese código fuente; y el código asociado con cada patrón, cuando coincide, reemplaza el código pasado a la macro. Todo esto sucede durante la compilación.

Para definir una macro, se utiliza la construcción `macro_rules!`. Vamos a explorar cómo usar `macro_rules!` viendo cómo se define la macro `vec!`. El Capítulo 8 cubrió cómo podemos usar la macro `vec!` para crear un nuevo vector con valores particulares. Por ejemplo, la siguiente macro crea un nuevo vector que contiene tres enteros:

```rust
let v: Vec<u32> = vec![1, 2, 3];
```

También podríamos usar la macro `vec!` para crear un vector de dos enteros o un vector de cinco rebanadas de cadena. No podríamos usar una función para hacer lo mismo porque no conoceríamos el número o el tipo de valores de antemano.

La Lista 19-28 muestra una definición ligeramente simplificada de la macro `vec!`.

Nombre del archivo: `src/lib.rs`

```rust
1 #[macro_export]
2 macro_rules! vec {
  3 ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
          4 $(
              5 temp_vec.push(6 $x);
            )*
          7 temp_vec
        }
    };
}
```

Lista 19-28: Versión simplificada de la definición de la macro `vec!`

> Nota: La definición real de la macro `vec!` en la biblioteca estándar incluye código para preasignar la cantidad correcta de memoria de antemano. Ese código es una optimización que no incluimos aquí para simplificar el ejemplo.

La anotación `#[macro_export]` \[1\] indica que esta macro debe estar disponible siempre que el crat en el que se define la macro se haga visible. Sin esta anotación, la macro no puede ser llevada al ámbito.

Luego comenzamos la definición de la macro con `macro_rules!` y el nombre de la macro que estamos definiendo _sin_ el signo de exclamación \[2\]. El nombre, en este caso `vec`, está seguido de llaves que denotan el cuerpo de la definición de la macro.

La estructura en el cuerpo de `vec!` es similar a la estructura de una expresión `match`. Aquí tenemos un brazo con el patrón `( $( $x:expr ),* )`, seguido de `=>` y el bloque de código asociado con este patrón \[3\]. Si el patrón coincide, el bloque de código asociado se emitirá. Dado que este es el único patrón en esta macro, solo hay una forma válida de coincidir; cualquier otro patrón resultará en un error. Las macros más complejas tendrán más de un brazo.

La sintaxis de patrón válida en las definiciones de macros es diferente de la sintaxis de patrón cubierta en el Capítulo 18 porque los patrones de macros se coinciden contra la estructura del código de Rust en lugar de valores. Vamos a analizar lo que significan las piezas de patrón en la Lista 19-28; para la sintaxis completa de patrón de macro, consulte la Referencia de Rust en *https://doc.rust-lang.org/reference/macros-by-example.html*.

Primero usamos un par de paréntesis para encerrar todo el patrón. Usamos un signo de dólar (`$`) para declarar una variable en el sistema de macros que contendrá el código de Rust que coincide con el patrón. El signo de dólar hace evidente que esta es una variable de macro en oposición a una variable regular de Rust. A continuación viene un par de paréntesis que captura los valores que coinciden con el patrón dentro de los paréntesis para su uso en el código de reemplazo. Dentro de `$()` está `$x:expr`, que coincide con cualquier expresión de Rust y le da el nombre `$x` a la expresión.

La coma que sigue a `$()` indica que un carácter separador literal de coma podría aparecer opcionalmente después del código que coincide con el código en `$()`. El `*` especifica que el patrón coincide con cero o más de lo que precede al `*`.

Cuando llamamos a esta macro con `vec![1, 2, 3];`, el patrón `$x` coincide tres veces con las tres expresiones `1`, `2` y `3`.

Ahora echemos un vistazo al patrón en el cuerpo del código asociado con este brazo: `temp_vec.push()` \[5\] dentro de `$()* en [4] y [7] se genera para cada parte que coincide con`$()` en el patrón cero o más veces dependiendo de cuántas veces el patrón coincide. El `$x`[6] se reemplaza con cada expresión coincidente. Cuando llamamos a esta macro con`vec\[1, 2, 3\];\`, el código generado que reemplaza esta llamada a macro será el siguiente:

    {
        let mut temp_vec = Vec::new();
        temp_vec.push(1);
        temp_vec.push(2);
        temp_vec.push(3);
        temp_vec
    }

Hemos definido una macro que puede tomar cualquier número de argumentos de cualquier tipo y puede generar código para crear un vector que contiene los elementos especificados.

Para aprender más sobre cómo escribir macros, consulte la documentación en línea u otros recursos, como "The Little Book of Rust Macros" en *https://veykril.github.io/tlborm* iniciado por Daniel Keep y continuado por Lukas Wirth.
