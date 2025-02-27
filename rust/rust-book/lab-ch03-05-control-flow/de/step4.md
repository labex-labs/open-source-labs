# Verwendung von if in einer let-Anweisung

Da `if` ein Ausdruck ist, können wir ihn auf der rechten Seite einer `let`-Anweisung verwenden, um das Ergebnis einer Variable zuzuweisen, wie in Listing 3-2 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```

Listing 3-2: Zuweisen des Ergebnisses eines `if`-Ausdrucks an eine Variable

Die Variable `number` wird anhand des Ergebnisses des `if`-Ausdrucks gebunden. Führen Sie diesen Code aus, um zu sehen, was passiert:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
The value of number is: 5
```

Denken Sie daran, dass Codeblöcke sich auf den letzten Ausdruck in ihnen auswerten und Zahlen für sich genommen ebenfalls Ausdrücke sind. In diesem Fall hängt der Wert des gesamten `if`-Ausdrucks davon ab, welcher Codeblock ausgeführt wird. Dies bedeutet, dass die Werte, die als Ergebnisse aus den Armen des `if` möglich sind, vom gleichen Typ sein müssen; in Listing 3-2 waren die Ergebnisse sowohl des `if`-Arms als auch des `else`-Arms `i32`-Integers. Wenn die Typen nicht übereinstimmen, wie im folgenden Beispiel, erhalten wir einen Fehler:

Dateiname: `src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

Wenn wir diesen Code kompilieren möchten, erhalten wir einen Fehler. Die `if`- und `else`-Arme haben Werttypen, die nicht kompatibel sind, und Rust zeigt genau an, wo das Problem im Programm zu finden ist:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: `if` and `else` have incompatible types
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ expected integer, found
`&str`
  |                                 |
  |                                 expected because of this
```

Der Ausdruck im `if`-Block wertet sich zu einem Integer aus, und der Ausdruck im `else`-Block wertet sich zu einem String aus. Dies funktioniert nicht, da Variablen nur einen einzigen Typ haben dürfen und Rust zur Compile-Zeit wissen muss, welchen Typ die Variable `number` hat, definitiv. Indem man den Typ von `number` kennt, kann der Compiler überprüfen, dass der Typ überall dort gültig ist, wo wir `number` verwenden. Rust wäre nicht in der Lage, das zu tun, wenn der Typ von `number` nur zur Laufzeit bestimmt würde; der Compiler wäre komplexer und würde über die Codegarantien weniger verfügen, wenn er für jede Variable mehrere hypothetische Typen verfolgen müsste.
