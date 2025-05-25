# Como parâmetros de entrada

Embora o Rust escolha como capturar variáveis em tempo de execução, principalmente sem anotação de tipo, essa ambiguidade não é permitida ao escrever funções. Ao receber um closure como parâmetro de entrada, o tipo completo do closure deve ser anotado usando um dos `traits`, e eles são determinados pelo que o closure faz com o valor capturado. Em ordem decrescente de restrição, eles são:

- `Fn`: o closure usa o valor capturado por referência (`&T`)
- `FnMut`: o closure usa o valor capturado por referência mutável (`&mut T`)
- `FnOnce`: o closure usa o valor capturado por valor (`T`)

Por variável, o compilador capturará as variáveis da maneira menos restritiva possível.

Por exemplo, considere um parâmetro anotado como `FnOnce`. Isso especifica que o closure _pode_ capturar por `&T`, `&mut T` ou `T`, mas o compilador escolherá com base em como as variáveis capturadas são usadas no closure.

Isso ocorre porque, se uma movimentação for possível, qualquer tipo de empréstimo também deve ser possível. Note que o inverso não é verdadeiro. Se o parâmetro for anotado como `Fn`, a captura de variáveis por `&mut T` ou `T` não é permitida. No entanto, `&T` é permitido.

No exemplo a seguir, tente trocar o uso de `Fn`, `FnMut` e `FnOnce` para ver o que acontece:

```rust
// Uma função que recebe um closure como argumento e o chama.
// <F> denota que F é um "parâmetro de tipo genérico"
fn apply<F>(f: F) where
    // O closure não recebe entrada e não retorna nada.
    F: FnOnce() {
    // ^ TODO: Tente mudar isso para `Fn` ou `FnMut`.

    f();
}

// Uma função que recebe um closure e retorna um `i32`.
fn apply_to_3<F>(f: F) -> i32 where
    // O closure recebe um `i32` e retorna um `i32`.
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // Um tipo não copiável.
    // `to_owned` cria dados possuídos a partir de dados emprestados
    let mut farewell = "goodbye".to_owned();

    // Captura 2 variáveis: `greeting` por referência e
    // `farewell` por valor.
    let diary = || {
        // `greeting` é por referência: requer `Fn`.
        println!("I said {}.", greeting);

        // A mutação força `farewell` a ser capturado por
        // referência mutável. Agora requer `FnMut`.
        farewell.push_str("!!!");
        println!("Then I screamed {}.", farewell);
        println!("Now I can sleep. zzzzz");

        // Chamar drop manualmente força `farewell` a
        // ser capturado por valor. Agora requer `FnOnce`.
        mem::drop(farewell);
    };

    // Chame a função que aplica o closure.
    apply(diary);

    // `double` satisfaz o limite de trait de `apply_to_3`
    let double = |x| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}
```
