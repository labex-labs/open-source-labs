# Varios patrones

En las expresiones `match`, puedes coincidir con varios patrones utilizando la sintaxis `|`, que es el operador _o_ de patrones. Por ejemplo, en el siguiente código coincidimos el valor de `x` con los brazos de coincidencia, el primero de los cuales tiene una opción _o_, lo que significa que si el valor de `x` coincide con cualquiera de los valores en ese brazo, el código de ese brazo se ejecutará:

Nombre de archivo: `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("uno o dos"),
    3 => println!("tres"),
    _ => println!("cualquier cosa"),
}
```

Este código imprime `uno o dos`.
