# Usando Box`<T>` para almacenar datos en el montón

Antes de discutir el caso de uso de almacenamiento en el montón para `Box<T>`, cubriremos la sintaxis y cómo interactuar con los valores almacenados dentro de un `Box<T>`.

La Lista 15-1 muestra cómo usar una caja para almacenar un valor de `i32` en el montón.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let b = Box::new(5);
    println!("b = {b}");
}
```

Lista 15-1: Almacenando un valor de `i32` en el montón usando una caja

Definimos la variable `b` para que tenga el valor de una `Caja` que apunta al valor `5`, que se asigna en el montón. Este programa imprimirá `b = 5`; en este caso, podemos acceder a los datos en la caja de manera similar a como lo haríamos si estos datos estuvieran en la pila. Al igual que cualquier valor poseído, cuando una caja sale del ámbito, como lo hace `b` al final de `main`, se desasignará. La desasignación ocurre tanto para la caja (almacenada en la pila) como para los datos a los que apunta (almacenados en el montón).

Poner un solo valor en el montón no es muy útil, por lo que no usarás cajas por sí mismas de esta manera muy a menudo. Tener valores como un solo `i32` en la pila, donde se almacenan por defecto, es más adecuado en la mayoría de las situaciones. Veamos un caso en el que las cajas nos permiten definir tipos que no podríamos definir si no tuviéramos cajas.
