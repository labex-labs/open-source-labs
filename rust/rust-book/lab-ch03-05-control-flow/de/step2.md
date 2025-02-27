# if-Ausdrücke

Ein `if`-Ausdruck ermöglicht es Ihnen, Ihren Code abhängig von Bedingungen zu verzweigen. Sie geben eine Bedingung an und sagen dann: "Wenn diese Bedingung erfüllt ist, führe diesen Codeblock aus. Wenn die Bedingung nicht erfüllt ist, führe diesen Codeblock nicht aus."

Erstellen Sie ein neues Projekt namens `branches` im Verzeichnis `project`, um den `if`-Ausdruck zu erkunden. Öffnen Sie in der Datei `src/main.rs` den Editor und geben Sie Folgendes ein:

```bash
cd ~/project
cargo new branches
```

Dateiname: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

Alle `if`-Ausdrücke beginnen mit dem Schlüsselwort `if`, gefolgt von einer Bedingung. In diesem Fall prüft die Bedingung, ob die Variable `number` einen Wert kleiner als 5 hat. Wir platzieren den Codeblock, der ausgeführt werden soll, wenn die Bedingung `true` ist, direkt nach der Bedingung in geschweiften Klammern. Die Codeblöcke, die mit den Bedingungen in `if`-Ausdrücken assoziiert sind, werden manchmal als _Arme_ bezeichnet, ähnlich wie die Arme in `match`-Ausdrücken, über die wir in "Vergleichen der Vermutung mit der Geheimzahl" gesprochen haben.

Optional können wir auch einen `else`-Ausdruck hinzufügen, wie wir es hier getan haben, um dem Programm einen alternativen Codeblock zur Verfügung zu stellen, der ausgeführt werden soll, wenn die Bedingung `false` ausgewertet wird. Wenn Sie keinen `else`-Ausdruck angeben und die Bedingung `false` ist, springt das Programm einfach den `if`-Block über und geht zum nächsten Codeabschnitt über.

Versuchen Sie, diesen Code auszuführen; Sie sollten die folgende Ausgabe sehen:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was true
```

Lassen Sie uns versuchen, den Wert von `number` zu ändern, um eine Bedingung zu erhalten, die `false` ist, um zu sehen, was passiert:

```rust
    let number = 7;
```

Führen Sie das Programm erneut aus und betrachten Sie die Ausgabe:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was false
```

Es ist auch erwähnenswert, dass die Bedingung in diesem Code _muss_ ein `bool` sein. Wenn die Bedingung kein `bool` ist, erhalten wir einen Fehler. Versuchen Sie beispielsweise, den folgenden Code auszuführen:

Dateiname: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

Die `if`-Bedingung wertet sich diesmal zu einem Wert von `3` aus, und Rust wirft einen Fehler:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected `bool`, found integer
```

Der Fehler gibt an, dass Rust einen `bool` erwartet hat, aber eine Ganzzahl erhalten hat. Im Gegensatz zu Sprachen wie Ruby und JavaScript versucht Rust nicht automatisch, nicht-Boolean-Typen in einen Boolean zu konvertieren. Sie müssen explizit sein und `if` immer mit einem Boolean als Bedingung angeben. Wenn wir möchten, dass der `if`-Codeblock nur dann ausgeführt wird, wenn eine Zahl nicht gleich `0` ist, können wir den `if`-Ausdruck wie folgt ändern:

Dateiname: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number!= 0 {
        println!("number was something other than zero");
    }
}
```

Beim Ausführen dieses Codes wird `number was something other than zero` ausgegeben.
