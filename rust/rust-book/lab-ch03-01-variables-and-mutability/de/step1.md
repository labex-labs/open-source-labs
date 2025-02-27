# Variablen und Veränderbarkeit

Wie in "Speichern von Werten mit Variablen" erwähnt, sind Variablen standardmäßig unveränderlich. Dies ist einer der vielen Hinweise, die Rust Ihnen gibt, um Ihren Code so zu schreiben, dass Sie die Sicherheit und die einfache Parallelität nutzen, die Rust bietet. Dennoch haben Sie die Option, Ihre Variablen veränderbar zu machen. Lassen Sie uns untersuchen, wie und warum Rust Sie ermutigt, die Unveränderbarkeit zu bevorzugen und warum Sie manchmal abweichen möchten.

Wenn eine Variable unveränderlich ist, können Sie den Wert, der an einen Namen gebunden ist, nicht mehr ändern, nachdem er einmal zugewiesen wurde. Um dies zu veranschaulichen, erstellen Sie ein neues Projekt namens _variables_ im `project`-Verzeichnis, indem Sie `cargo new variables` verwenden.

Öffnen Sie dann in Ihrem neuen `variables`-Verzeichnis `src/main.rs` und ersetzen Sie seinen Code durch folgenden Code, der noch nicht kompilieren wird:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Speichern Sie die Datei und führen Sie das Programm mit `cargo run` aus. Sie sollten eine Fehlermeldung über einen Unveränderbarkeitsfehler erhalten, wie in dieser Ausgabe zu sehen:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

Dieses Beispiel zeigt, wie der Compiler Ihnen hilft, Fehler in Ihrem Programm zu finden. Compilerfehler können frustrierend sein, aber im Grunde bedeuten sie nur, dass Ihr Programm noch nicht sicher macht, was Sie es tun möchten; sie bedeuten _nicht_, dass Sie kein guter Programmierer sind! Erfahrungene Rust-Entwickler erhalten immer noch Compilerfehler.

Sie haben die Fehlermeldung `cannot assign twice to immutable variable`x\``erhalten, weil Sie versucht haben, einen zweiten Wert an die unveränderliche Variable`x` zuzuweisen.

Es ist wichtig, dass wir Kompilierungsfehler erhalten, wenn wir versuchen, einen Wert zu ändern, der als unveränderlich markiert ist, da genau diese Situation zu Fehlern führen kann. Wenn ein Teil unseres Codes davon ausgeht, dass ein Wert sich niemals ändert und ein anderer Teil unseres Codes diesen Wert ändert, ist es möglich, dass der erste Teil des Codes nicht mehr das tut, was er ursprünglich getan haben soll. Der Grund für einen solchen Fehler kann sich nachträglich schwer verfolgen lassen, insbesondere wenn der zweite Codeabschnitt den Wert nur _manchmal_ ändert. Der Rust-Compiler garantiert, dass, wenn Sie angeben, dass ein Wert sich nicht ändern wird, er tatsächlich nicht ändern wird, so dass Sie sich nicht selbst darum kümmern müssen. Ihr Code ist daher einfacher zu verstehen.

Aber Veränderbarkeit kann sehr nützlich sein und das Schreiben von Code einfacher machen. Obwohl Variablen standardmäßig unveränderlich sind, können Sie sie veränderbar machen, indem Sie `mut` vor dem Variablennamen hinzufügen, wie Sie es im zweiten Kapitel getan haben. Das Hinzufügen von `mut` gibt auch der späteren Leserschaft des Codes die Absicht an, indem es angibt, dass andere Teile des Codes diesen Variablenwert ändern werden.

Beispielsweise ändern wir `src/main.rs` wie folgt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Wenn wir das Programm jetzt ausführen, erhalten wir Folgendes:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

Wir dürfen den an `x` gebundenen Wert von `5` auf `6` ändern, wenn `mut` verwendet wird. Letztendlich ist es Ihnen überlassen, ob Sie Veränderbarkeit verwenden oder nicht, und dies hängt davon ab, was Ihnen in dieser speziellen Situation am klarsten erscheint.
