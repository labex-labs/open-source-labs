# Elisão (Elision)

Alguns padrões de tempo de vida (lifetime) são extremamente comuns, e por isso o verificador de empréstimos (borrow checker) permitirá que você os omita para economizar digitação e melhorar a legibilidade. Isso é conhecido como elisão (elision). A elisão existe em Rust unicamente porque esses padrões são comuns.

O código a seguir mostra alguns exemplos de elisão. Para uma descrição mais abrangente da elisão, consulte elisão de tempo de vida (lifetime elision) no livro.

```rust
// `elided_input` e `annotated_input` essencialmente têm assinaturas idênticas
// porque o tempo de vida de `elided_input` é inferido pelo compilador:
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// Similarmente, `elided_pass` e `annotated_pass` têm assinaturas idênticas
// porque o tempo de vida é adicionado implicitamente a `elided_pass`:
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}
```
