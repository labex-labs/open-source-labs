# Expressões

Um programa Rust é (principalmente) composto por uma série de instruções:

```rust
fn main() {
    // instrução
    // instrução
    // instrução
}
```

Existem alguns tipos de instruções em Rust. As duas mais comuns são declarar uma ligação de variável e usar um `;` com uma expressão:

```rust
fn main() {
    // ligação de variável
    let x = 5;

    // expressão;
    x;
    x + 1;
    15;
}
```

Os blocos também são expressões, pelo que podem ser usados como valores em atribuições. A última expressão no bloco será atribuída ao local onde a expressão está, como uma variável local. No entanto, se a última expressão do bloco terminar com um ponto e vírgula, o valor de retorno será `()`.

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Esta expressão será atribuída a `y`
        x_cube + x_squared + x
    };

    let z = {
        // O ponto e vírgula suprime esta expressão e `()` é atribuído a `z`
        2 * x;
    };

    println!("x é {:?}", x);
    println!("y é {:?}", y);
    println!("z é {:?}", z);
}
```
