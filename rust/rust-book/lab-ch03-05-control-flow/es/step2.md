# Expresiones `if`

Una expresión `if` te permite bifurcar tu código en función de condiciones. Tú proporcionas una condición y luego se establece: "Si se cumple esta condición, ejecuta este bloque de código. Si la condición no se cumple, no ejecutes este bloque de código".

Crea un nuevo proyecto llamado `branches` en tu directorio `project` para explorar la expresión `if`. En el archivo `src/main.rs`, escribe lo siguiente:

```bash
cd ~/project
cargo new branches
```

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

Todas las expresiones `if` empiezan con la palabra clave `if`, seguida de una condición. En este caso, la condición comprueba si la variable `number` tiene un valor menor que 5. Colocamos el bloque de código a ejecutar si la condición es `true` inmediatamente después de la condición dentro de llaves. Los bloques de código asociados con las condiciones en las expresiones `if` a veces se llaman _ramas_, al igual que las ramas en las expresiones `match` que discutimos en "Comparando la Adivinanza con el Número Secreto".

Opcionalmente, también podemos incluir una expresión `else`, que elegimos hacer aquí, para dar al programa un bloque alternativo de código a ejecutar si la condición evalúa a `false`. Si no proporcionas una expresión `else` y la condición es `false`, el programa simplemente saltará el bloque `if` y pasará al siguiente trozo de código.

Prueba a ejecutar este código; deberías ver la siguiente salida:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was true
```

Intentemos cambiar el valor de `number` a un valor que haga que la condición sea `false` para ver qué pasa:

```rust
    let number = 7;
```

Ejecuta el programa nuevamente y mira la salida:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was false
```

También vale la pena señalar que la condición en este código _debe_ ser un `bool`. Si la condición no es un `bool`, obtendremos un error. Por ejemplo, intenta ejecutar el siguiente código:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

La condición `if` evalúa a un valor de `3` esta vez, y Rust lanza un error:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected `bool`, found integer
```

El error indica que Rust esperaba un `bool` pero recibió un entero. A diferencia de lenguajes como Ruby y JavaScript, Rust no intentará automáticamente convertir tipos no booleanos a un booleano. Debes ser explícito y siempre proporcionar a `if` un booleano como su condición. Si queremos que el bloque de código `if` se ejecute solo cuando un número no es igual a `0`, por ejemplo, podemos cambiar la expresión `if` a la siguiente:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number!= 0 {
        println!("number was something other than zero");
    }
}
```

Ejecutar este código imprimirá `number was something other than zero`.
