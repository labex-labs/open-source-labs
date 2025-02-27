# El Tipo Array

Otra forma de tener una colección de múltiples valores es con un _array_. A diferencia de una tupla, cada elemento de un array debe tener el mismo tipo. A diferencia de los arrays en algunos otros lenguajes, los arrays en Rust tienen una longitud fija.

Escribimos los valores en un array como una lista separada por comas dentro de corchetes cuadrados:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```

Los arrays son útiles cuando quieres que tus datos se alojen en la pila en lugar de la memoria dinámica (hablaremos más sobre la pila y la memoria dinámica en el Capítulo 4) o cuando quieres asegurarte de siempre tener un número fijo de elementos. Sin embargo, un array no es tan flexible como el tipo vector. Un _vector_ es un tipo de colección similar proporcionado por la biblioteca estándar que _sí_ se puede permitir que crezca o contraiga en tamaño. Si no estás seguro de si usar un array o un vector, es probable que debas usar un vector. El Capítulo 8 discute los vectores en más detalle.

Sin embargo, los arrays son más útiles cuando sabes que el número de elementos no necesitará cambiar. Por ejemplo, si estuvieras usando los nombres de los meses en un programa, probablemente usarías un array en lugar de un vector porque sabes que siempre contendrá 12 elementos:

```rust
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

Escribes el tipo de un array usando corchetes cuadrados con el tipo de cada elemento, un punto y coma, y luego el número de elementos en el array, como esto:

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Aquí, `i32` es el tipo de cada elemento. Después del punto y coma, el número `5` indica que el array contiene cinco elementos.

También puedes inicializar un array para que contenga el mismo valor para cada elemento especificando el valor inicial, seguido de un punto y coma, y luego la longitud del array en corchetes cuadrados, como se muestra aquí:

```rust
let a = [3; 5];
```

El array nombrado `a` contendrá `5` elementos que todos se establecerán inicialmente en el valor `3`. Esto es lo mismo que escribir `let a = [3, 3, 3, 3, 3];` pero de una manera más concisa.
