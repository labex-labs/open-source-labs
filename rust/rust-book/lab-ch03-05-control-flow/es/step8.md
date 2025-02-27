# Etiquetas de Bucle para Desambiguar Entre Varios Bucles

Si tienes bucles dentro de bucles, `break` y `continue` se aplican al bucle más interno en ese momento. Puedes especificar opcionalmente una _etiqueta de bucle_ en un bucle que luego puedes usar con `break` o `continue` para especificar que esas palabras clave se aplican al bucle etiquetado en lugar del bucle más interno. Las etiquetas de bucle deben comenzar con una comilla simple. Aquí hay un ejemplo con dos bucles anidados:

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

El bucle externo tiene la etiqueta `'counting_up`, y contará desde 0 hasta 2. El bucle interno sin etiqueta cuenta hacia abajo desde 10 hasta 9. El primer `break` que no especifica una etiqueta solo saldrá del bucle interno. La declaración `break 'counting_up;` saldrá del bucle externo. Este código imprime:

       Compiling loops v0.1.0 (file:///projects/loops)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
