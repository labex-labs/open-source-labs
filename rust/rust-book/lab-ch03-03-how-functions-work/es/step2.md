# Parámetros

Podemos definir funciones con _parámetros_, que son variables especiales que forman parte de la firma de una función. Cuando una función tiene parámetros, puedes proporcionarle valores concretos para esos parámetros. Técnicamente, los valores concretos se llaman _argumentos_, pero en la conversación cotidiana, la gente tiende a usar las palabras _parámetro_ y _argumento_ de manera intercambiable tanto para las variables en la definición de una función como para los valores concretos que se pasan cuando se llama a una función.

En esta versión de `another_function` agregamos un parámetro:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

Intenta ejecutar este programa; deberías obtener la siguiente salida:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

La declaración de `another_function` tiene un parámetro llamado `x`. El tipo de `x` se especifica como `i32`. Cuando pasamos `5` a `another_function`, la macro `println!` coloca `5` donde estaba el par de llaves que contenía `x` en la cadena de formato.

En las firmas de funciones, _debes_ declarar el tipo de cada parámetro. Esta es una decisión deliberada en el diseño de Rust: exigir anotaciones de tipo en las definiciones de funciones significa que el compilador casi nunca necesita que las uses en otros lugares del código para entender qué tipo quieres decir. El compilador también puede dar mensajes de error más útiles si sabe qué tipos espera la función.

Cuando se definen múltiples parámetros, separa las declaraciones de parámetros con comas, como esto:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

Este ejemplo crea una función llamada `print_labeled_measurement` con dos parámetros. El primer parámetro se llama `value` y es un `i32`. El segundo se llama `unit_label` y es de tipo `char`. Luego, la función imprime texto que contiene tanto el `value` como el `unit_label`.

Vamos a intentar ejecutar este código. Reemplaza el programa que actualmente está en el archivo `src/main.rs` de tu proyecto _functions_ con el ejemplo anterior y ejecútalo usando `cargo run`:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

Debido a que llamamos a la función con `5` como valor para `value` y `'h'` como valor para `unit_label`, la salida del programa contiene esos valores.
