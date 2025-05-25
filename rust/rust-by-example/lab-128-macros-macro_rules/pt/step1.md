# macro_rules!

Rust fornece um poderoso sistema de macros que permite a metaprogramação. Como você viu nos capítulos anteriores, as macros se parecem com funções, exceto que seus nomes terminam com um ponto de exclamação `!`, mas em vez de gerar uma chamada de função, as macros são expandidas em código-fonte que é compilado com o restante do programa. No entanto, ao contrário das macros em C e outras linguagens, as macros Rust são expandidas em árvores de sintaxe abstrata (AST - Abstract Syntax Trees), em vez de pré-processamento de strings, para que você não tenha bugs inesperados de precedência.

Macros são criadas usando a macro `macro_rules!`.

```rust
// This is a simple macro named `say_hello`.
macro_rules! say_hello {
    // `()` indicates that the macro takes no argument.
    () => {
        // The macro will expand into the contents of this block.
        println!("Hello!")
    };
}

fn main() {
    // This call will expand into `println!("Hello")`
    say_hello!()
}
```

Então, por que as macros são úteis?

1.  Não se repita (Don't repeat yourself). Existem muitos casos em que você pode precisar de funcionalidades semelhantes em vários lugares, mas com tipos diferentes. Frequentemente, escrever uma macro é uma maneira útil de evitar a repetição de código. (Mais sobre isso mais tarde)

2.  Linguagens específicas de domínio (Domain-specific languages). Macros permitem que você defina uma sintaxe especial para um propósito específico. (Mais sobre isso mais tarde)

3.  Interfaces variádicas (Variadic interfaces). Às vezes, você deseja definir uma interface que receba um número variável de argumentos. Um exemplo é `println!`, que pode receber qualquer número de argumentos, dependendo da string de formatação. (Mais sobre isso mais tarde)
