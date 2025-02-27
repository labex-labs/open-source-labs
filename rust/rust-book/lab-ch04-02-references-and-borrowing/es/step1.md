# Referencias y Prestamos

El problema con el código de tupla en la Lista 4-5 es que tenemos que devolver la `String` a la función llamante para que aún podamos usar la `String` después de llamar a `calculate_length`, porque la `String` fue movida a `calculate_length`. En cambio, podemos proporcionar una referencia al valor de la `String`. Una _referencia_ es como un puntero en el sentido de que es una dirección que podemos seguir para acceder a los datos almacenados en esa dirección; esos datos son propiedad de alguna otra variable. A diferencia de un puntero, se garantiza que una referencia apunte a un valor válido de un tipo particular durante la vida de esa referencia.

Aquí está cómo definir y usar una función `calculate_length` que tiene una referencia a un objeto como parámetro en lugar de tomar posesión del valor:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Primero, observa que todo el código de tupla en la declaración de variable y el valor de retorno de la función desapareció. Segundo, observa que pasamos `&s1` a `calculate_length` y, en su definición, tomamos `&String` en lugar de `String`. Estos signos de admiración representan _referencias_, y te permiten referirte a algún valor sin tomar posesión de él. La Figura 4-5 describe este concepto.

Figura 4-5: Un diagrama de `&String s` apuntando a `String s1`

> Nota: Lo contrario de referenciar usando `&` es _desreferenciar_, lo que se logra con el operador de desreferencia, `*`. Veremos algunos usos del operador de desreferencia en el Capítulo 8 y discutiremos los detalles de la desreferencia en el Capítulo 15.

Echemos un vistazo más detenido a la llamada de función aquí:

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

La sintaxis `&s1` nos permite crear una referencia que _se refiere_ al valor de `s1` pero no lo posee. Debido a que no lo posee, el valor al que apunta no se eliminará cuando la referencia deje de usarse.

Del mismo modo, la firma de la función usa `&` para indicar que el tipo del parámetro `s` es una referencia. Vamos a agregar algunas anotaciones explicativas:

```rust
fn calculate_length(s: &String) -> usize { // s es una referencia a una String
    s.len()
} // Aquí, s sale del ámbito. Pero debido a que no tiene posesión de lo
  // a lo que se refiere, la String no se elimina
```

El ámbito en el que la variable `s` es válida es el mismo que el ámbito de cualquier parámetro de función, pero el valor al que apunta la referencia no se elimina cuando `s` deja de usarse, porque `s` no tiene posesión. Cuando las funciones tienen referencias como parámetros en lugar de los valores reales, no necesitaremos devolver los valores para devolver la posesión, porque nunca tuvimos posesión.

Llamamos a la acción de crear una referencia _prestar_. Al igual que en la vida real, si una persona posee algo, puedes prestarlo de ellos. Cuando hayas terminado, debes devolverlo. No lo posees.

Entonces, ¿qué pasa si intentamos modificar algo que estamos prestando? Prueba el código en la Lista 4-6. Alerta: ¡no funciona!

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Lista 4-6: Intentando modificar un valor prestado

Aquí está el error:

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

Al igual que las variables son inmutables por defecto, también lo son las referencias. No se nos permite modificar algo a lo que tenemos una referencia.
