# Inferencia y Anotación de Tipo de Closure

Hay más diferencias entre funciones y closures. Los closures generalmente no requieren que anotes los tipos de los parámetros o el valor de retorno como lo hacen las funciones `fn`. Las anotaciones de tipo son necesarias en las funciones porque los tipos son parte de una interfaz explícita expuesta a tus usuarios. Definir esta interfaz rigidamente es importante para garantizar que todos estén de acuerdo sobre qué tipos de valores utiliza y devuelve una función. Los closures, por otro lado, no se utilizan en una interfaz expuesta como esta: se almacenan en variables y se utilizan sin nombrarlas y expuestas a los usuarios de nuestra biblioteca.

Los closures suelen ser cortos y solo son relevantes dentro de un contexto limitado en lugar de en cualquier escenario arbitrario. Dentro de estos contextos limitados, el compilador puede inferir los tipos de los parámetros y el tipo de retorno, de manera similar a cómo es capaz de inferir los tipos de la mayoría de las variables (hay casos raros en los que el compilador también necesita anotaciones de tipo de closure).

Al igual que con las variables, podemos agregar anotaciones de tipo si queremos aumentar la claridad y la explicitud a costa de ser más verboso de lo estrictamente necesario. Anotar los tipos para un closure se vería como la definición mostrada en la Lista 13-2. En este ejemplo, estamos definiendo un closure y almacenándolo en una variable en lugar de definir el closure en el lugar donde lo pasamos como argumento, como hicimos en la Lista 13-1.

Nombre de archivo: `src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Lista 13-2: Agregando anotaciones opcionales de los tipos de parámetro y valor de retorno en el closure

Con las anotaciones de tipo agregadas, la sintaxis de los closures se parece más a la sintaxis de las funciones. Aquí, definimos una función que suma 1 a su parámetro y un closure que tiene el mismo comportamiento, para comparación. Hemos agregado algunos espacios para alinear las partes relevantes. Esto ilustra cómo la sintaxis de los closures es similar a la sintaxis de las funciones excepto por el uso de tubos y la cantidad de sintaxis que es opcional:

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

La primera línea muestra una definición de función y la segunda línea muestra una definición de closure completamente anotada. En la tercera línea, eliminamos las anotaciones de tipo de la definición de closure. En la cuarta línea, eliminamos los corchetes, que son opcionales porque el cuerpo del closure tiene solo una expresión. Estas son todas definiciones válidas que producirán el mismo comportamiento cuando se llamen. Las líneas `add_one_v3` y `add_one_v4` requieren que se evalúen los closures para poder compilar porque los tipos se inferirán a partir de su uso. Esto es similar a `let v = Vec::new();` que necesita anotaciones de tipo o valores de algún tipo para ser insertados en el `Vec` para que Rust pueda inferir el tipo.

Para las definiciones de closure, el compilador inferirá un tipo concrete para cada uno de sus parámetros y para su valor de retorno. Por ejemplo, la Lista 13-3 muestra la definición de un closure corto que solo devuelve el valor que recibe como parámetro. Este closure no es muy útil excepto con fines de este ejemplo. Nota que no hemos agregado ninguna anotación de tipo a la definición. Debido a que no hay anotaciones de tipo, podemos llamar al closure con cualquier tipo, lo que hemos hecho aquí con `String` la primera vez. Si luego intentamos llamar a `example_closure` con un entero, obtendremos un error.

Nombre de archivo: `src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Lista 13-3: Intentando llamar a un closure cuyos tipos se inferen con dos tipos diferentes

El compilador nos da este error:

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

La primera vez que llamamos a `example_closure` con el valor `String`, el compilador infiere el tipo de `x` y el tipo de retorno del closure como `String`. Esos tipos se bloquean luego en el closure en `example_closure`, y obtenemos un error de tipo cuando intentamos usar un tipo diferente con el mismo closure a continuación.
