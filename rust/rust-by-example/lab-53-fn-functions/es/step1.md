# Funciones

Las funciones se declaran utilizando la palabra clave `fn`. Sus argumentos se anotan con su tipo, al igual que las variables, y, si la función devuelve un valor, el tipo de retorno debe especificarse después de una flecha `->`.

La última expresión en la función se utilizará como valor de retorno. Alternativamente, la instrucción `return` se puede utilizar para devolver un valor antes desde dentro de la función, incluso desde dentro de bucles o instrucciones `if`.

¡Vamos a reescribir FizzBuzz utilizando funciones!

```rust
// A diferencia de C/C++, no hay restricción sobre el orden de las definiciones de funciones
fn main() {
    // Podemos utilizar esta función aquí, y definirlas más adelante en algún lugar
    fizzbuzz_to(100);
}

// Función que devuelve un valor booleano
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // Caso especial, retorno temprano
    if rhs == 0 {
        return false;
    }

    // Esta es una expresión, la palabra clave `return` no es necesaria aquí
    lhs % rhs == 0
}

// Funciones que "no" devuelven un valor, en realidad devuelven el tipo unitario `()`
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// Cuando una función devuelve `()`, el tipo de retorno se puede omitir de la
// firma
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
