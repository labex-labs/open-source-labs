# Parámetros de función

Los parámetros de función también pueden ser patrones. El código en el Listado 18-6, que declara una función llamada `foo` que toma un parámetro llamado `x` de tipo `i32`, probablemente ya le sea familiar.

```rust
fn foo(x: i32) {
    // código aquí
}
```

Listado 18-6: Una firma de función que utiliza patrones en los parámetros

La parte `x` es un patrón ¡Como hicimos con `let`, podríamos hacer coincidir una tupla en los argumentos de una función con el patrón. El Listado 18-7 separa los valores de una tupla mientras la pasamos a una función.

Nombre del archivo: `src/main.rs`

```rust
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("Current location: ({x}, {y})");
}

fn main() {
    let point = (3, 5);
    print_coordinates(&point);
}
```

Listado 18-7: Una función con parámetros que desestructuran una tupla

Este código imprime `Current location: (3, 5)`. Los valores `&(3, 5)` coinciden con el patrón `&(x, y)`, por lo que `x` es el valor `3` y `y` es el valor `5`.

También podemos usar patrones en las listas de parámetros de cierre de la misma manera que en las listas de parámetros de función porque los cierres son similares a las funciones, como se discutió en el Capítulo 13.

En este momento, ha visto varias maneras de usar patrones, pero los patrones no funcionan del mismo modo en todos los lugares donde los podemos usar. En algunos lugares, los patrones deben ser irrefutables; en otras circunstancias, pueden ser refutables. Discutiremos estos dos conceptos a continuación.
