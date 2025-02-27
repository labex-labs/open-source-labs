# Interne Veränderbarkeit: Ein veränderbarer Leihvorgang für einen unveränderbaren Wert

Eine Folge der Leihregeln ist, dass Sie, wenn Sie einen unveränderbaren Wert haben, diesen nicht veränderbar leihen können. Beispielsweise wird dieser Code nicht kompilieren:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

Wenn Sie diesen Code versuchen zu kompilieren, erhalten Sie den folgenden Fehler:

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

Es gibt jedoch Situationen, in denen es nützlich wäre, wenn ein Wert sich in seinen Methoden verändert, aber für anderen Code unveränderbar erscheint. Code außerhalb der Methoden des Werts wäre nicht in der Lage, den Wert zu mutieren. Das Verwenden von `RefCell<T>` ist eine Möglichkeit, die Fähigkeit zur internen Veränderbarkeit zu erhalten, aber `RefCell<T>` umgeht die Leihregeln nicht vollständig: Der Leihprüfungsmechanismus im Compiler erlaubt diese interne Veränderbarkeit, und die Leihregeln werden zur Laufzeit überprüft. Wenn Sie die Regeln verletzen, erhalten Sie einen `panic!` statt eines Compilerfehlers.

Betrachten wir ein praktisches Beispiel, in dem wir `RefCell<T>` verwenden können, um einen unveränderbaren Wert zu mutieren, und sehen, warum das nützlich ist.
