# Usando Supertraits

Às vezes, você pode escrever uma definição de trait que depende de outra trait: para que um tipo implemente a primeira trait, você deseja exigir que esse tipo também implemente a segunda trait. Você faria isso para que sua definição de trait possa usar os itens associados da segunda trait. A trait em que sua definição de trait está se baseando é chamada de _supertrait_ da sua trait.

Por exemplo, digamos que queremos criar uma trait `OutlinePrint` com um método `outline_print` que imprimirá um determinado valor formatado para que seja enquadrado em asteriscos. Ou seja, dado uma struct `Point` que implementa a trait da biblioteca padrão `Display` para resultar em `(x, y)`, quando chamamos `outline_print` em uma instância de `Point` que tem `1` para `x` e `3` para `y`, ela deve imprimir o seguinte:

    **********
    *        *
    * (1, 3) *
    *        *
    **********

Na implementação do método `outline_print`, queremos usar a funcionalidade da trait `Display`. Portanto, precisamos especificar que a trait `OutlinePrint` funcionará apenas para tipos que também implementam `Display` e fornecem a funcionalidade que `OutlinePrint` precisa. Podemos fazer isso na definição da trait especificando `OutlinePrint: Display`. Essa técnica é semelhante a adicionar uma restrição de trait à trait. A Listagem 19-22 mostra uma implementação da trait `OutlinePrint`.

Nome do arquivo: `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Listagem 19-22: Implementando a trait `OutlinePrint` que requer a funcionalidade de `Display`

Como especificamos que `OutlinePrint` requer a trait `Display`, podemos usar a função `to_string` que é implementada automaticamente para qualquer tipo que implemente `Display`. Se tentássemos usar `to_string` sem adicionar dois pontos e especificar a trait `Display` após o nome da trait, obteríamos um erro dizendo que nenhum método chamado `to_string` foi encontrado para o tipo `&Self` no escopo atual.

Vamos ver o que acontece quando tentamos implementar `OutlinePrint` em um tipo que não implementa `Display`, como a struct `Point`:

Nome do arquivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Obtemos um erro dizendo que `Display` é necessário, mas não implementado:

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

Para corrigir isso, implementamos `Display` em `Point` e satisfazemos a restrição que `OutlinePrint` requer, assim:

Nome do arquivo: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Então, implementar a trait `OutlinePrint` em `Point` compilará com sucesso, e podemos chamar `outline_print` em uma instância de `Point` para exibi-la dentro de um contorno de asteriscos.
