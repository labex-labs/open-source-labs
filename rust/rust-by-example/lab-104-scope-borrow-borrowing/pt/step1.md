# _Borrowing_ (Empréstimo)

Na maioria das vezes, gostaríamos de acessar dados sem tomar posse (ownership) deles. Para conseguir isso, Rust usa um mecanismo de _borrowing_ (empréstimo). Em vez de passar objetos por valor (`T`), os objetos podem ser passados por referência (`&T`).

O compilador garante estaticamente (através de seu _borrow checker_) que as referências _sempre_ apontam para objetos válidos. Ou seja, enquanto existirem referências a um objeto, o objeto não pode ser destruído.

```rust
// Esta função toma posse de uma caixa e a destrói
fn eat_box_i32(boxed_i32: Box<i32>) {
    println!("Destruindo a caixa que contém {}", boxed_i32);
}

// Esta função empresta um i32
fn borrow_i32(borrowed_i32: &i32) {
    println!("Este inteiro é: {}", borrowed_i32);
}

fn main() {
    // Cria um i32 em uma caixa e um i32 na pilha
    let boxed_i32 = Box::new(5_i32);
    let stacked_i32 = 6_i32;

    // Empresta o conteúdo da caixa. A posse não é tomada,
    // então o conteúdo pode ser emprestado novamente.
    borrow_i32(&boxed_i32);
    borrow_i32(&stacked_i32);

    {
        // Toma uma referência aos dados contidos dentro da caixa
        let _ref_to_i32: &i32 = &boxed_i32;

        // Erro!
        // Não é possível destruir `boxed_i32` enquanto o valor interno é emprestado mais tarde no escopo.
        eat_box_i32(boxed_i32);
        // FIXME ^ Comente esta linha

        // Tenta emprestar `_ref_to_i32` após o valor interno ser destruído
        borrow_i32(_ref_to_i32);
        // `_ref_to_i32` sai do escopo e não está mais emprestado.
    }

    // `boxed_i32` agora pode ceder a posse para `eat_box` e ser destruído
    eat_box_i32(boxed_i32);
}
```
