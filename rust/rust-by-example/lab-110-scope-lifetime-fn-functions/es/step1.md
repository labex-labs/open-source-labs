# Funciones

Ignorando la [elisión], las firmas de funciones con tiempos de vida tienen algunas restricciones:

- cualquier referencia _debe_ tener un tiempo de vida anotado.
- cualquier referencia devuelta _debe_ tener el mismo tiempo de vida que una entrada o ser `static`.

Además, tenga en cuenta que no está permitido devolver referencias sin entrada si eso implicaría devolver referencias a datos no válidos. El siguiente ejemplo muestra algunas formas válidas de funciones con tiempos de vida:

```rust
// Una referencia de entrada con tiempo de vida `'a` que debe existir
// al menos durante el tiempo que dure la función.
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x es {}", x);
}

// También es posible tener referencias mutables con tiempos de vida.
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// Varios elementos con diferentes tiempos de vida. En este caso,
// estaría bien que ambos tuvieran el mismo tiempo de vida `'a`, pero
// en casos más complejos, pueden ser necesarios tiempos de vida diferentes.
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x es {}, y es {}", x, y);
}

// Es aceptable devolver referencias que se han pasado como parámetros.
// Sin embargo, se debe devolver el tiempo de vida correcto.
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// Lo anterior es inválido: `'a` debe existir más tiempo que la función.
// Aquí, `&String::from("foo")` crearía una `String`, seguida de una
// referencia. Luego, los datos se eliminan al salir del ámbito, dejando
// una referencia a datos no válidos para ser devuelta.

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```
