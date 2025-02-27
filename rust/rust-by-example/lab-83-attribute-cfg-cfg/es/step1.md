# `cfg`

Es posible realizar comprobaciones condicionales de configuración a través de dos operadores diferentes:

- el atributo `cfg`: `#[cfg(...)]` en la posición del atributo
- la macro `cfg!`: `cfg!(...)` en expresiones booleanas

Mientras que el primero habilita la compilación condicional, el segundo se evalúa condicionalmente a los literales `true` o `false`, lo que permite realizar comprobaciones en tiempo de ejecución. Ambos utilizan la misma sintaxis de argumentos.

A diferencia de `#[cfg]`, `cfg!` no elimina ningún código y solo se evalúa a `true` o `false`. Por ejemplo, todos los bloques en una expresión if/else deben ser válidos cuando `cfg!` se utiliza para la condición, independientemente de lo que esté evaluando `cfg!`.

```rust
// Esta función solo se compila si el sistema operativo destino es linux
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// Y esta función solo se compila si el sistema operativo destino *no* es linux
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!");
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}
```
