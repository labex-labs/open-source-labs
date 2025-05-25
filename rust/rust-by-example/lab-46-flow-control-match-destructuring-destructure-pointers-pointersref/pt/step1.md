# pointers/ref

Para ponteiros, é necessária uma distinção entre desestruturação e dereferenciação, pois são conceitos diferentes utilizados de forma distinta em relação a linguagens como C/C++.

- A dereferenciação utiliza `*`
- A desestruturação utiliza `&`, `ref` e `ref mut`

```rust
fn main() {
    // Atribui uma referência do tipo `i32`. O `&` indica que uma referência está sendo atribuída.
    let reference = &4;

    match reference {
        // Se `reference` for correspondido com o padrão `&val`, resulta
        // em uma comparação como:
        // `&i32`
        // `&val`
        // ^ Vemos que se os `&` de correspondência forem removidos, então o `i32`
        // deve ser atribuído a `val`.
        &val => println!("Obteve um valor por meio de desestruturação: {:?}", val),
    }

    // Para evitar o `&`, você desreferencia antes da correspondência.
    match *reference {
        val => println!("Obteve um valor por meio de dereferenciação: {:?}", val),
    }

    // E se você não começar com uma referência? `reference` era um `&`
    // porque o lado direito já era uma referência. Isso não é
    // uma referência porque o lado direito não é uma.
    let _not_a_reference = 3;

    // Rust fornece `ref` exatamente para esse propósito. Ele modifica a
    // atribuição para que uma referência seja criada para o elemento; esta
    // referência é atribuída.
    let ref _is_a_reference = 3;

    // Consequentemente, definindo 2 valores sem referências, referências
    // podem ser recuperadas via `ref` e `ref mut`.
    let value = 5;
    let mut mut_value = 6;

    // Use a palavra-chave `ref` para criar uma referência.
    match value {
        ref r => println!("Obteve uma referência a um valor: {:?}", r),
    }

    // Use `ref mut` de forma semelhante.
    match mut_value {
        ref mut m => {
            // Obteve uma referência. É preciso desreferenciá-la antes de
            // adicionar algo a ela.
            *m += 10;
            println!("Adicionamos 10. `mut_value`: {:?}", m);
        },
    }
}
```
