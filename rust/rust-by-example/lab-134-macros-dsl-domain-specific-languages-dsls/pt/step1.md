# Linguagens de Domínio Específico (DSLs)

Uma DSL é uma mini "linguagem" embutida em uma macro Rust. É Rust completamente válido porque o sistema de macros se expande em construções Rust normais, mas se parece com uma pequena linguagem. Isso permite que você defina uma sintaxe concisa ou intuitiva para alguma funcionalidade especial (dentro de limites).

Suponha que eu queira definir uma pequena API de calculadora. Eu gostaria de fornecer uma expressão e ter a saída impressa no console.

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // Force types to be integers
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // hehehe `eval` is _not_ a Rust keyword!
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

Saída:

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

Este foi um exemplo muito simples.

Observe também os dois pares de chaves na macro. As externas fazem parte da sintaxe de `macro_rules!`, além de `()` ou `[]`.
