# El Tipo Tupla

Una _tupla_ es una forma general de agrupar una serie de valores de varios tipos en un solo tipo compuesto. Las tuplas tienen una longitud fija: una vez declaradas, no pueden crecer o contraerse en tamaño.

Creamos una tupla escribiendo una lista separada por comas de valores dentro de paréntesis. Cada posición en la tupla tiene un tipo, y los tipos de los diferentes valores en la tupla no tienen que ser los mismos. Hemos agregado anotaciones de tipo opcionales en este ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

La variable `tup` se asocia con toda la tupla porque una tupla se considera un solo elemento compuesto. Para extraer los valores individuales de una tupla, podemos usar la coincidencia de patrones para desestructurar un valor de tupla, como esto:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("El valor de y es: {y}");
}
```

Este programa primero crea una tupla y la asocia con la variable `tup`. Luego, utiliza un patrón con `let` para tomar `tup` y convertirla en tres variables separadas, `x`, `y` y `z`. Esto se llama _desestructuración_ porque divide la tupla única en tres partes. Finalmente, el programa imprime el valor de `y`, que es `6.4`.

También podemos acceder directamente a un elemento de tupla usando un punto (`.`) seguido del índice del valor que queremos acceder. Por ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

Este programa crea la tupla `x` y luego accede a cada elemento de la tupla usando sus respectivos índices. Al igual que en la mayoría de los lenguajes de programación, el primer índice en una tupla es 0.

La tupla sin ningún valor tiene un nombre especial, _unit_. Este valor y su tipo correspondiente se escriben ambos `()` y representan un valor vacío o un tipo de retorno vacío. Las expresiones devuelven implícitamente el valor unitario si no devuelven ningún otro valor.
