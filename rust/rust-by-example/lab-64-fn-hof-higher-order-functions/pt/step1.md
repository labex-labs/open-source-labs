# Funções de Ordem Superior

Rust fornece Funções de Ordem Superior (FOS). Essas são funções que recebem uma ou mais funções e/ou produzem uma função mais útil. FOS e iteradores preguiçosos conferem a Rust seu sabor funcional.

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Encontre a soma de todos os quadrados de números ímpares abaixo de 1000");
    let upper = 1000;

    // Abordagem imperativa
    // Declarar variável acumuladora
    let mut acc = 0;
    // Iterar: 0, 1, 2, ... até infinito
    for n in 0.. {
        // Elevar o número ao quadrado
        let n_squared = n * n;

        if n_squared >= upper {
            // Interromper o loop se ultrapassar o limite superior
            break;
        } else if is_odd(n_squared) {
            // Acumular o valor, se for ímpar
            acc += n_squared;
        }
    }
    println!("estilo imperativo: {}", acc);

    // Abordagem funcional
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // Todos os números naturais ao quadrado
             .take_while(|&n_squared| n_squared < upper) // Abaixo do limite superior
             .filter(|&n_squared| is_odd(n_squared))     // Que são ímpares
             .sum();                                     // Somá-los
    println!("estilo funcional: {}", sum_of_squared_odd_numbers);
}
```

Os tipos `Option` e `Iterator` implementam várias FOS.
