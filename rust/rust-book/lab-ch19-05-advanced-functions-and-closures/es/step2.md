# Punteros a funciones

Hemos hablado de cómo pasar cierres a funciones; ¡también puedes pasar funciones regulares a funciones! Esta técnica es útil cuando quieres pasar una función que ya has definido en lugar de definir un nuevo cierre. Las funciones se convierten en el tipo `fn` (con una _f_ en minúsculas), no confundir con el trato de cierre `Fn`. El tipo `fn` se llama _puntero a función_. Pasar funciones con punteros a funciones te permitirá usar funciones como argumentos para otras funciones.

La sintaxis para especificar que un parámetro es un puntero a función es similar a la de los cierres, como se muestra en la Lista 19-27, donde hemos definido una función `add_one` que suma 1 a su parámetro. La función `do_twice` toma dos parámetros: un puntero a función a cualquier función que tome un parámetro de tipo `i32` y devuelva un `i32`, y un valor de tipo `i32`. La función `do_twice` llama a la función `f` dos veces, pasándole el valor `arg`, luego suma los dos resultados de las llamadas a la función. La función `main` llama a `do_twice` con los argumentos `add_one` y `5`.

Nombre de archivo: `src/main.rs`

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

Lista 19-27: Usando el tipo `fn` para aceptar un puntero a función como argumento

Este código imprime `The answer is: 12`. Especificamos que el parámetro `f` en `do_twice` es un `fn` que toma un parámetro de tipo `i32` y devuelve un `i32`. Luego podemos llamar a `f` en el cuerpo de `do_twice`. En `main`, podemos pasar el nombre de la función `add_one` como primer argumento a `do_twice`.

A diferencia de los cierres, `fn` es un tipo en lugar de un trato, por lo que especificamos `fn` como el tipo de parámetro directamente en lugar de declarar un parámetro de tipo genérico con uno de los tratados `Fn` como un límite de trato.

Los punteros a funciones implementan los tres tratados de cierre (`Fn`, `FnMut` y `FnOnce`), lo que significa que siempre puedes pasar un puntero a función como argumento para una función que espera un cierre. Es mejor escribir funciones usando un tipo genérico y uno de los tratados de cierre para que tus funciones puedan aceptar tanto funciones como cierres.

Dicho esto, un ejemplo de donde solo querrías aceptar `fn` y no cierres es cuando se comunica con código externo que no tiene cierres: las funciones C pueden aceptar funciones como argumentos, pero C no tiene cierres.

Como ejemplo de donde podrías usar un cierre definido en línea o una función con nombre, echemos un vistazo a un uso del método `map` proporcionado por el trato `Iterator` en la biblioteca estándar. Para usar la función `map` para convertir un vector de números en un vector de cadenas, podríamos usar un cierre, como este:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(|i| i.to_string())
 .collect();
```

O podríamos nombrar una función como argumento de `map` en lugar del cierre, como este:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(ToString::to_string)
 .collect();
```

Tenga en cuenta que debemos usar la sintaxis completamente cualificada que hablamos en "Tratados avanzados" porque hay múltiples funciones disponibles con el nombre `to_string`.

Aquí, estamos usando la función `to_string` definida en el trato `ToString`, que la biblioteca estándar ha implementado para cualquier tipo que implemente `Display`.

Recuerde de "Valores de enumeración" que el nombre de cada variante de enumeración que definimos también se convierte en una función de inicialización. Podemos usar estas funciones de inicialización como punteros a funciones que implementan los tratados de cierre, lo que significa que podemos especificar las funciones de inicialización como argumentos para métodos que toman cierres, como sigue:

```rust
enum Status {
    Value(u32),
    Stop,
}

let list_of_statuses: Vec<Status> = (0u32..20)
 .map(Status::Value)
 .collect();
```

Aquí, creamos instancias de `Status::Value` usando cada valor de tipo `u32` en el rango en el que se llama a `map` usando la función de inicialización de `Status::Value`. Algunas personas prefieren este estilo y otras prefieren usar cierres. Se compilan en el mismo código, así que use el estilo que sea más claro para usted.
