# El verificador de préstamos

El compilador de Rust tiene un _verificador de préstamos_ que compara los ámbitos para determinar si todos los préstamos son válidos. La Lista 10-17 muestra el mismo código que la Lista 10-16 pero con anotaciones que muestran los lifetimes de las variables.

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

Lista 10-17: Anotaciones de los lifetimes de `r` y `x`, denominados `'a` y `'b`, respectivamente

Aquí, hemos anotado el lifetime de `r` con `'a` y el lifetime de `x` con `'b`. Como se puede ver, el bloque interno `'b` es mucho más pequeño que el bloque de lifetime externo `'a`. En tiempo de compilación, Rust compara el tamaño de los dos lifetimes y ve que `r` tiene un lifetime de `'a` pero que se refiere a memoria con un lifetime de `'b`. El programa es rechazado porque `'b` es más corto que `'a`: el objeto de la referencia no tiene la misma duración que la referencia.

La Lista 10-18 corrige el código para que no tenga una referencia colgante y se compile sin errores.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Lista 10-18: Una referencia válida porque los datos tienen un lifetime más largo que la referencia

Aquí, `x` tiene el lifetime `'b`, que en este caso es mayor que `'a`. Esto significa que `r` puede referirse a `x` porque Rust sabe que la referencia en `r` siempre será válida mientras `x` sea válida.

Ahora que sabes dónde están los lifetimes de las referencias y cómo Rust analiza los lifetimes para garantizar que las referencias siempre serán válidas, exploremos los lifetimes genéricos de los parámetros y los valores de retorno en el contexto de funciones.
