# `panic`

O mecanismo de tratamento de erros mais simples que veremos é o `panic`. Ele imprime uma mensagem de erro, começa a desenrolar a pilha (unwinding the stack) e geralmente encerra o programa. Aqui, chamamos explicitamente `panic` em nossa condição de erro:

```rust
fn drink(beverage: &str) {
    // You shouldn't drink too much sugary beverages.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
