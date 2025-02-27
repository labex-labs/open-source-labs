# Captura

Los closures son inherentemente flexibles y harán lo que la funcionalidad requiera para que el closure funcione sin anotación. Esto permite que la captura se adapte flexiblemente al caso de uso, a veces moviendo y a veces prestando. Los closures pueden capturar variables:

- por referencia: `&T`
- por referencia mutable: `&mut T`
- por valor: `T`

Prefieren capturar variables por referencia y solo se bajan de nivel cuando es necesario.

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // Un closure para imprimir `color` que inmediatamente presta (`&`) `color` y
    // almacena el préstamo y el closure en la variable `print`. Permanecerá
    // prestado hasta que `print` se use por última vez.
    //
    // `println!` solo requiere argumentos por referencia inmutable, por lo que no
    // impone nada más restrictivo.
    let print = || println!("`color`: {}", color);

    // Llame al closure usando el préstamo.
    print();

    // `color` se puede prestar de nuevo inmutablemente, porque el closure solo
    // tiene una referencia inmutable a `color`.
    let _reborrow = &color;
    print();

    // Un movimiento o re-préstamo está permitido después del último uso de `print`
    let _color_moved = color;


    let mut count = 0;
    // Un closure para incrementar `count` podría tomar `&mut count` o `count`
    // pero `&mut count` es menos restrictivo, por lo que lo toma. Presta inmediatamente
    // `count`.
    //
    // Se requiere un `mut` en `inc` porque se almacena un `&mut` dentro. Por lo tanto,
    // llamar al closure muta el closure, lo que requiere un `mut`.
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // Llame al closure usando un préstamo mutable.
    inc();

    // El closure todavía presta mutuamente `count` porque se llama más tarde.
    // Un intento de re-prestar causará un error.
    // let _reborrow = &count;
    // ^ TODO: intente descomentar esta línea.
    inc();

    // El closure ya no necesita prestar `&mut count`. Por lo tanto, es
    // posible re-prestar sin error
    let _count_reborrowed = &mut count;


    // Un tipo no copiable.
    let movable = Box::new(3);

    // `mem::drop` requiere `T`, por lo que esto debe tomar por valor. Un tipo copiable
    // se copiaría en el closure dejando el original intacto.
    // Un tipo no copiable debe moverse y, por lo tanto, `movable` se mueve inmediatamente en
    // el closure.
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` consume la variable, por lo que solo se puede llamar una vez.
    consume();
    // consume();
    // ^ TODO: Intente descomentar esta línea.
}
```

Usando `move` antes de los tubos verticales fuerza al closure a tomar posesión de las variables capturadas:

```rust
fn main() {
    // `Vec` tiene semánticas no copiables.
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ Descomentar la línea anterior resultará en un error de compilación
    // porque el verificador de préstamos no permite reutilizar la variable después de que
    // se ha movido.

    // Quitar `move` de la firma del closure hará que el closure
    // preste inmutablemente la variable _haystack_, por lo tanto _haystack_ todavía
    // está disponible y descomentar la línea anterior no causará un error.
}
```
