# `cfg`

Verificações condicionais de configuração são possíveis por meio de dois operadores diferentes:

- o atributo `cfg`: `#[cfg(...)]` em posição de atributo
- a macro `cfg!`: `cfg!(...)` em expressões booleanas

Enquanto o primeiro permite compilação condicional, o segundo avalia condicionalmente para literais `true` ou `false`, permitindo verificações em tempo de execução. Ambos utilizam sintaxe de argumento idêntica.

`cfg!`, ao contrário de `#[cfg]`, não remove nenhum código e apenas avalia para verdadeiro ou falso. Por exemplo, todos os blocos em uma expressão if/else precisam ser válidos quando `cfg!` é usado para a condição, independentemente do que `cfg!` esteja avaliando.

```rust
// Esta função só é compilada se o sistema operacional de destino for linux
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("Você está rodando linux!");
}

// E esta função só é compilada se o sistema operacional de destino *não* for linux
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("Você *não* está rodando linux!");
}

fn main() {
    are_you_on_linux();

    println!("Tem certeza?");
    if cfg!(target_os = "linux") {
        println!("Sim. É definitivamente linux!");
    } else {
        println!("Sim. É definitivamente *não* linux!");
    }
}
```
