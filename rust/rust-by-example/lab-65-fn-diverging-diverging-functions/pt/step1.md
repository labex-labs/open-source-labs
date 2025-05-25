# Funções Divergentes

Funções divergentes nunca retornam. São marcadas usando `!`, que é um tipo vazio.

```rust
fn foo() -> ! {
    panic!("Esta chamada nunca retorna.");
}
```

Ao contrário de todos os outros tipos, este não pode ser instanciado, porque o conjunto de todos os valores possíveis que este tipo pode ter é vazio. Note que é diferente do tipo `()`, que tem exatamente um valor possível.

Por exemplo, esta função retorna normalmente, embora não haja informação no valor de retorno.

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("Esta função retorna e você pode ver esta linha.");
}
```

Ao contrário desta função, que nunca retornará o controle de volta para o chamador.

```rust
#![feature(never_type)]

fn main() {
    let x: ! = panic!("Esta chamada nunca retorna.");
    println!("Você nunca verá esta linha!");
}
```

Embora isso possa parecer um conceito abstrato, na verdade é muito útil e frequentemente prático. A principal vantagem deste tipo é que ele pode ser convertido para qualquer outro tipo e, portanto, usado em locais onde um tipo exato é necessário, por exemplo, em ramos `match`. Isso permite que escrevamos código como este:

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // Note que o tipo de retorno desta expressão match deve ser u32
            // devido ao tipo da variável "addition".
            let addition: u32 = match i%2 == 1 {
                // A variável "i" é do tipo u32, o que está perfeitamente bem.
                true => i,
                // Por outro lado, a expressão "continue" não retorna
                // u32, mas ainda está bem, porque nunca retorna e, portanto,
                // não viola os requisitos de tipo da expressão match.
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Soma dos números ímpares até 9 (excluindo): {}", sum_odd_numbers(9));
}
```

Também é o tipo de retorno de funções que loopam para sempre (por exemplo, `loop {}`), como servidores de rede, ou funções que terminam o processo (por exemplo, `exit()`).
