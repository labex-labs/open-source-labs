# Propiedad y moves

Debido a que las variables se encargan de liberar sus propios recursos, **un recurso solo puede tener un propietario**. Esto también evita que los recursos se liberen más de una vez. Tenga en cuenta que no todas las variables poseen recursos (por ejemplo, [referencias]).

Cuando se realizan asignaciones (`let x = y`) o se pasan argumentos de función por valor (`foo(x)`), se transfiere la _propiedad_ de los recursos. En el habla de Rust, esto se conoce como un _move_.

Después de mover los recursos, el propietario anterior ya no se puede utilizar. Esto evita la creación de punteros colgantes.

```rust
// Esta función toma la propiedad de la memoria asignada en el montón
fn destroy_box(c: Box<i32>) {
    println!("Destruyendo una caja que contiene {}", c);

    // `c` es destruida y la memoria se libera
}

fn main() {
    // Entero asignado en la _pila_
    let x = 5u32;

    // *Copiar* `x` en `y` - no se mueven recursos
    let y = x;

    // Ambos valores se pueden utilizar independientemente
    println!("x es {}, y y es {}", x, y);

    // `a` es un puntero a un entero asignado en el _montón_
    let a = Box::new(5i32);

    println!("a contiene: {}", a);

    // *Mover* `a` en `b`
    let b = a;
    // La dirección de puntero de `a` se copia (no los datos) en `b`.
    // Ambos ahora son punteros a los mismos datos asignados en el montón, pero
    // `b` ahora los posee.

    // Error! `a` ya no puede acceder a los datos, porque ya no posee la
    // memoria del montón
    //println!("a contiene: {}", a);
    // TODO ^ Intente descomentar esta línea

    // Esta función toma la propiedad de la memoria asignada en el montón de `b`
    destroy_box(b);

    // Dado que la memoria del montón se ha liberado en este punto, esta acción
    // resultaría en la referencia a memoria liberada, pero está prohibida por el compilador
    // Error! La misma razón que el Error anterior
    //println!("b contiene: {}", b);
    // TODO ^ Intente descomentar esta línea
}
```
