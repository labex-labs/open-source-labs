# Funções de entrada

Como closures podem ser usadas como argumentos, você pode se perguntar se o mesmo pode ser dito sobre funções. E de fato pode! Se você declarar uma função que recebe uma closure como parâmetro, qualquer função que satisfaça a restrição de tipo dessa closure pode ser passada como parâmetro.

```rust
// Define uma função que recebe um argumento genérico `F`
// limitado por `Fn`, e a chama
fn call_me<F: Fn()>(f: F) {
    f();
}

// Define uma função wrapper que satisfaz a restrição `Fn`
fn function() {
    println!("Sou uma função!");
}

fn main() {
    // Define uma closure que satisfaz a restrição `Fn`
    let closure = || println!("Sou uma closure!");

    call_me(closure);
    call_me(function);
}
```

Como observação adicional, os traits `Fn`, `FnMut` e `FnOnce` ditam como uma closure captura variáveis do escopo envolvente.
