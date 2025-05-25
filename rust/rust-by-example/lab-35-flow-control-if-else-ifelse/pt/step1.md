# if/else

A ramificação com `if`-`else` é semelhante a outras linguagens. Ao contrário de muitas delas, a condição booleana não precisa ser envolvida por parênteses, e cada condição é seguida por um bloco. As condicionais `if`-`else` são expressões, e todos os ramos devem retornar o mesmo tipo.

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} is negative", n);
    } else if n > 0 {
        print!("{} is positive", n);
    } else {
        print!("{} is zero", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", and is a small number, increase ten-fold");

            // Esta expressão retorna um `i32`.
            10 * n
        } else {
            println!(", and is a big number, halve the number");

            // Esta expressão também deve retornar um `i32`.
            n / 2
            // TODO ^ Tente suprimir esta expressão com um ponto-e-vírgula.
        };
    //   ^ Não se esqueça de colocar um ponto-e-vírgula aqui! Todas as ligações `let` precisam dele.

    println!("{} -> {}", n, big_n);
}
```
