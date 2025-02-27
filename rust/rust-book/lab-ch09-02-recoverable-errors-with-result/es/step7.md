# Dónde se puede usar el operador?

El operador `?` solo se puede usar en funciones cuyo tipo de retorno sea compatible con el valor en el que se usa el `?`. Esto se debe a que el operador `?` está definido para realizar una devolución temprana de un valor fuera de la función, de la misma manera que la expresión `match` que definimos en la Lista 9-6. En la Lista 9-6, la `match` estaba usando un valor de `Result`, y el brazo de retorno temprano devolvía un valor `Err(e)`. El tipo de retorno de la función debe ser un `Result` para que sea compatible con esta `return`.

En la Lista 9-10, veamos el error que obtendremos si usamos el operador `?` en una función `main` con un tipo de retorno que no es compatible con el tipo del valor en el que usamos `?`.

Nombre del archivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

Lista 9-10: Intentar usar el `?` en la función `main` que devuelve `()` no se compilará.

Este código abre un archivo, lo que podría fallar. El operador `?` sigue el valor de `Result` devuelto por `File::open`, pero esta función `main` tiene el tipo de retorno de `()`, no `Result`. Cuando compilamos este código, obtenemos el siguiente mensaje de error:

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

Este error señala que solo se nos permite usar el operador `?` en una función que devuelve `Result`, `Option` o otro tipo que implemente `FromResidual`.

Para corregir el error, tienes dos opciones. Una opción es cambiar el tipo de retorno de tu función para que sea compatible con el valor en el que estás usando el operador `?`, siempre y cuando no tengas restricciones que lo impidan. La otra opción es usar una `match` o uno de los métodos de `Result<T, E>` para manejar el `Result<T, E>` de la manera que sea adecuada.

El mensaje de error también mencionó que `?` se puede usar con valores de `Option<T>` también. Al igual que al usar `?` en `Result`, solo se puede usar `?` en `Option` en una función que devuelve un `Option`. El comportamiento del operador `?` cuando se llama en un `Option<T>` es similar a su comportamiento cuando se llama en un `Result<T, E>`: si el valor es `None`, el `None` se devolverá temprano de la función en ese momento. Si el valor es `Some`, el valor dentro del `Some` es el valor resultante de la expresión, y la función continúa. La Lista 9-11 tiene un ejemplo de una función que encuentra el último carácter de la primera línea en el texto dado.

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

Lista 9-11: Usando el operador `?` en un valor de `Option<T>`

Esta función devuelve `Option<char>` porque es posible que haya un carácter ahí, pero también es posible que no haya. Este código toma el argumento de rebanada de cadena `text` y llama al método `lines` en él, que devuelve un iterador sobre las líneas de la cadena. Debido a que esta función quiere examinar la primera línea, llama a `next` en el iterador para obtener el primer valor del iterador. Si `text` es la cadena vacía, esta llamada a `next` devolverá `None`, en cuyo caso usamos `?` para detener y devolver `None` desde `last_char_of_first_line`. Si `text` no es la cadena vacía, `next` devolverá un valor `Some` que contiene una rebanada de cadena de la primera línea en `text`.

El `?` extrae la rebanada de cadena, y podemos llamar a `chars` en esa rebanada de cadena para obtener un iterador de sus caracteres. Estamos interesados en el último carácter en esta primera línea, así que llamamos a `last` para devolver el último elemento del iterador. Esto es un `Option` porque es posible que la primera línea sea la cadena vacía; por ejemplo, si `text` empieza con una línea en blanco pero tiene caracteres en otras líneas, como en `"\nhi"`. Sin embargo, si hay un último carácter en la primera línea, se devolverá en la variante `Some`. El operador `?` en el medio nos da una forma concisa de expresar esta lógica, lo que nos permite implementar la función en una línea. Si no pudiéramos usar el operador `?` en `Option`, tendríamos que implementar esta lógica usando más llamadas a métodos o una expresión `match`.

Tenga en cuenta que puede usar el operador `?` en un `Result` en una función que devuelve `Result`, y puede usar el operador `?` en un `Option` en una función que devuelve `Option`, pero no puede mezclarlos. El operador `?` no convertirá automáticamente un `Result` en un `Option` o viceversa; en esos casos, puede usar métodos como el método `ok` en `Result` o el método `ok_or` en `Option` para hacer la conversión explícitamente.

Hasta ahora, todas las funciones `main` que hemos usado devuelven `()`. La función `main` es especial porque es el punto de entrada y salida de un programa ejecutable, y hay restricciones sobre cuál puede ser su tipo de retorno para que el programa se comporte como se espera.

Por suerte, `main` también puede devolver un `Result<(), E>`. La Lista 9-12 tiene el código de la Lista 9-10, pero hemos cambiado el tipo de retorno de `main` a ser `Result<(), Box<dyn Error>>` y agregado un valor de retorno `Ok(())` al final. Este código ahora se compilará.

Nombre del archivo: `src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

Lista 9-12: Cambiar `main` para devolver `Result<(), E>` permite el uso del operador `?` en valores de `Result`.

El tipo `Box<dyn Error>` es un _objeto de trato_, sobre el que hablaremos en "Usando Objetos de Trato que Permiten Valores de Diferentes Tipos". Por ahora, puede leer `Box<dyn Error>` como "cualquier tipo de error". Usar `?` en un valor de `Result` en una función `main` con el tipo de error `Box<dyn Error>` está permitido porque permite que cualquier valor `Err` se devuelva temprano. Aunque el cuerpo de esta función `main` solo devolverá errores del tipo `std::io::Error`, al especificar `Box<dyn Error>`, esta firma seguirá siendo correcta incluso si se agrega más código que devuelva otros errores al cuerpo de `main`.

Cuando una función `main` devuelve un `Result<(), E>`, el programa ejecutable saldrá con un valor de `0` si `main` devuelve `Ok(())` y saldrá con un valor distinto de cero si `main` devuelve un valor `Err`. Los programas ejecutables escritos en C devuelven enteros cuando salen: los programas que salen con éxito devuelven el entero `0`, y los programas que tienen errores devuelven algún entero distinto de `0`. Rust también devuelve enteros desde los programas ejecutables para ser compatible con esta convención.

La función `main` puede devolver cualquier tipo que implemente el trato `std::process::Termination`, que contiene una función `report` que devuelve un `ExitCode`. Consulte la documentación de la biblioteca estándar para obtener más información sobre la implementación del trato `Termination` para sus propios tipos.

Ahora que hemos discutido los detalles de llamar a `panic!` o devolver `Result`, volvamos al tema de cómo decidir cuál es el adecuado para usar en cada caso.
