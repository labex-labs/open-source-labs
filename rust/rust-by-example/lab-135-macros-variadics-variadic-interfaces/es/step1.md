# Interfaces Variádicas

Una interfaz _variádica_ toma un número arbitrario de argumentos. Por ejemplo, `println!` puede tomar un número arbitrario de argumentos, según lo determinado por la cadena de formato.

Podemos extender la macro `calculate!` de la sección anterior para que sea variádica:

```rust
macro_rules! calculate {
    // El patrón para un solo `eval`
    (eval $e:expr) => {
        {
            let val: usize = $e; // Forzar que los tipos sean enteros
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // Descomponer múltiples `eval`s de forma recursiva
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // ¡Mira, mamá! `calculate!` variádica
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

Salida:

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
