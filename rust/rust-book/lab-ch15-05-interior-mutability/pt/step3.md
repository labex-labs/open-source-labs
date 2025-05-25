# Mutabilidade Interior: Um Empréstimo Mutável para um Valor Imutável

Uma consequência das regras de empréstimo é que, quando você tem um valor imutável, você não pode emprestá-lo de forma mutável. Por exemplo, este código não compilará:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

Se você tentasse compilar este código, você obteria o seguinte erro:

```bash
error[E0596]: cannot borrow `x` as mutable, as it is not declared
as mutable
 --> src/main.rs:3:13
  |
2 |     let x = 5;
  |         - help: consider changing this to be mutable: `mut x`
3 |     let y = &mut x;
  |             ^^^^^^ cannot borrow as mutable
```

No entanto, existem situações em que seria útil para um valor se mutar em seus métodos, mas parecer imutável para outro código. O código fora dos métodos do valor não seria capaz de mutar o valor. Usar `RefCell<T>` é uma maneira de obter a capacidade de ter mutabilidade interior, mas `RefCell<T>` não contorna completamente as regras de empréstimo: o verificador de empréstimo (borrow checker) no compilador permite essa mutabilidade interior, e as regras de empréstimo são verificadas em tempo de execução em vez disso. Se você violar as regras, você obterá um `panic!` em vez de um erro do compilador.

Vamos analisar um exemplo prático onde podemos usar `RefCell<T>` para mutar um valor imutável e ver por que isso é útil.
