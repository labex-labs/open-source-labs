# Constantes

Rust possui dois tipos diferentes de constantes que podem ser declaradas em qualquer escopo, incluindo o global. Ambos exigem anotação de tipo explícita:

- `const`: Um valor imutável (o caso comum).
- `static`: Uma variável possivelmente mutável com tempo de vida `'static`. O tempo de vida estático é inferido e não precisa ser especificado. Acessar ou modificar uma variável estática mutável é `unsafe`.

```rust
// As variáveis globais são declaradas fora de todos os outros escopos.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Acessar constante em alguma função
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Acessar constante na thread principal
    println!("Este é {}", LANGUAGE);
    println!("O limite é {}", THRESHOLD);
    println!("{} é {}", n, if is_big(n) { "grande" } else { "pequeno" });

    // Erro! Não é possível modificar uma constante.
    THRESHOLD = 5;
    // FIXME ^ Comente esta linha
}
```
