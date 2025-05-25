# Anonimato de Tipo

Closures capturam sucintamente variáveis de escopos envolventes. Isto tem consequências? Certamente. Observe como usar um closure como parâmetro de função requer [genéricos], o que é necessário devido à forma como eles são definidos:

```rust
// `F` deve ser genérico.
fn apply<F>(f: F) where
    F: FnOnce() {
    f();
}
```

Quando um closure é definido, o compilador cria implicitamente uma nova estrutura anónima para armazenar as variáveis capturadas internamente, ao mesmo tempo que implementa a funcionalidade através de um dos `traits`: `Fn`, `FnMut` ou `FnOnce` para este tipo desconhecido. Este tipo é atribuído à variável que é armazenada até à chamada.

Como este novo tipo é de tipo desconhecido, qualquer utilização numa função exigirá genéricos. No entanto, um parâmetro de tipo ilimitado `<T>` ainda seria ambíguo e não seria permitido. Assim, a delimitação por um dos `traits`: `Fn`, `FnMut` ou `FnOnce` (que ele implementa) é suficiente para especificar o seu tipo.

```rust
// `F` deve implementar `Fn` para um closure que não recebe
// entradas e não retorna nada - exatamente o que é necessário
// para `print`.
fn apply<F>(f: F) where
    F: Fn() {
    f();
}

fn main() {
    let x = 7;

    // Captura `x` num tipo anónimo e implementa
    // `Fn` para ele. Armazena-o em `print`.
    let print = || println!("{}", x);

    apply(print);
}
```
