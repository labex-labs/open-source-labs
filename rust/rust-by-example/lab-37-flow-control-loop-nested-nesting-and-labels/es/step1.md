# Anidación y etiquetas

Es posible `romper` o `continuar` los bucles externos cuando se tratan bucles anidados. En estos casos, los bucles deben ser etiquetados con una `'etiqueta`, y la etiqueta debe ser pasada a la declaración `break`/`continue`.

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("Entró al bucle externo");

        'inner: loop {
            println!("Entró al bucle interno");

            // Esto solo rompería el bucle interno
            //break;

            // Esto rompe el bucle externo
            break 'outer;
        }

        println!("Este punto nunca se alcanzará");
    }

    println!("Salió del bucle externo");
}
```
