# Lenguajes Específicos de Dominio (DSLs)

Un DSL es un mini "lenguaje" incrustado en una macro de Rust. Es completamente código válido de Rust porque el sistema de macros se expande en constructos normales de Rust, pero parece un pequeño lenguaje. Esto te permite definir una sintaxis concisa o intuitiva para alguna funcionalidad especial (dentro de límites).

Supongamos que quiero definir una pequeña API de calculadora. Me gustaría suministrar una expresión y que se imprima la salida en la consola.

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // Forzar que los tipos sean enteros
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // jaja `eval` no es una palabra clave de Rust!
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

Salida:

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

Este fue un ejemplo muy simple.

También, nota los dos pares de llaves en la macro. Las externas son parte de la sintaxis de `macro_rules!`, además de `()` o `[]`.
