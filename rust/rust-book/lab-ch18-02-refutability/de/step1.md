# Refutierbarkeit: Ob ein Muster fehlschlagen kann

Muster kommen in zwei Formen: refutierbar und nicht-refutierbar. Muster, die für jeden möglichen übergebenen Wert übereinstimmen, sind _nicht-refutierbar_. Ein Beispiel dafür wäre `x` in der Anweisung `let x = 5;`, da `x` alles übereinstimmt und daher nicht fehlschlagen kann. Muster, die für einige mögliche Werte fehlschlagen können, sind _refutierbar_. Ein Beispiel wäre `Some(x)` im Ausdruck `if let Some(x) = a_value`, denn wenn der Wert in der `a_value`-Variable `None` ist, anstatt `Some`, wird das Muster `Some(x)` nicht übereinstimmen.

Funktionsparameter, `let`-Anweisungen und `for`-Schleifen können nur nicht-refutierbare Muster akzeptieren, da das Programm nichts Sinnvolles tun kann, wenn die Werte nicht übereinstimmen. Die `if let`- und `while let`-Ausdrücke akzeptieren refutierbare und nicht-refutierbare Muster, aber der Compiler gibt eine Warnung bei nicht-refutierbaren Mustern, da sie per Definition dazu gedacht sind, mögliches Fehlschlagen zu behandeln: Die Funktionalität einer bedingten Anweisung liegt darin, dass sie je nach Erfolg oder Misserfolg unterschiedlich funktioniert.

Im Allgemeinen musst du dich nicht um die Unterscheidung zwischen refutierbaren und nicht-refutierbaren Mustern kümmern; du musst jedoch mit dem Konzept der Refutierbarkeit vertraut sein, damit du reagieren kannst, wenn du es in einer Fehlermeldung siehst. In diesen Fällen musst du entweder das Muster oder den Konstrukt, mit dem du das Muster verwendest, ändern, je nachdem, was das gewünschte Verhalten des Codes ist.

Schauen wir uns ein Beispiel an, was passiert, wenn wir versuchen, ein refutierbares Muster zu verwenden, wo Rust ein nicht-refutierbares Muster erwartet, und umgekehrt. Listing 18-8 zeigt eine `let`-Anweisung, aber für das Muster haben wir `Some(x)` angegeben, ein refutierbares Muster. Wie du wahrscheinlich erwartest, wird dieser Code nicht kompilieren.

```rust
let Some(x) = some_option_value;
```

Listing 18-8: Versuch, ein refutierbares Muster mit `let` zu verwenden

Wenn `some_option_value` ein `None`-Wert wäre, würde es dem Muster `Some(x)` nicht entsprechen, was bedeutet, dass das Muster refutierbar ist. Die `let`-Anweisung kann jedoch nur ein nicht-refutierbares Muster akzeptieren, da es nichts Gültiges gibt, was der Code mit einem `None`-Wert tun kann. Zur Compile-Zeit wird Rust klagen, dass wir versucht haben, ein refutierbares Muster zu verwenden, wo ein nicht-refutierbares Muster erforderlich ist:

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

Da wir mit dem Muster `Some(x)` nicht alle gültigen Werte abgedeckt haben (und auch nicht abdecken können!), produziert Rust mit Recht einen Compilerfehler.

Wenn wir ein refutierbares Muster haben, wo ein nicht-refutierbares Muster erforderlich ist, können wir es beheben, indem wir den Code ändern, der das Muster verwendet: Anstatt `let` zu verwenden, können wir `if let` verwenden. Dann, wenn das Muster nicht übereinstimmt, wird der Code einfach den Code in den geschweiften Klammern überspringen, was ihm einen Weg gibt, gültig fortzufahren. Listing 18-9 zeigt, wie man den Code in Listing 18-8 behebt.

    if let Some(x) = some_option_value {
        println!("{x}");
    }

Listing 18-9: Verwenden von `if let` und einem Block mit refutierbaren Mustern anstelle von `let`

Wir haben dem Code eine Ausweichmöglichkeit gegeben! Dieser Code ist vollkommen gültig, obwohl es bedeutet, dass wir kein nicht-refutierbares Muster verwenden können, ohne einen Fehler zu erhalten. Wenn wir `if let` ein Muster geben, das immer übereinstimmen wird, wie `x`, wie in Listing 18-10 gezeigt, gibt der Compiler eine Warnung.

    if let x = 5 {
        println!("{x}");
    };

Listing 18-10: Versuch, ein nicht-refutierbares Muster mit `if let` zu verwenden

Rust klagt an, dass es keinen Sinn macht, `if let` mit einem nicht-refutierbaren Muster zu verwenden:

    warning: irrefutable `if let` pattern
     --> src/main.rs:2:8
      |
    2 |     if let x = 5 {
      |        ^^^^^^^^^
      |
      = note: `#[warn(irrefutable_let_patterns)]` on by default
      = note: this pattern will always match, so the `if let` is
    useless
      = help: consider replacing the `if let` with a `let`

Aus diesem Grund müssen `match`-Arme refutierbare Muster verwenden, außer für den letzten Arm, der alle verbleibenden Werte mit einem nicht-refutierbaren Muster übereinstimmen sollte. Rust erlaubt uns, ein nicht-refutierbares Muster in einem `match` mit nur einem Arm zu verwenden, aber diese Syntax ist nicht besonders nützlich und könnte durch eine einfachere `let`-Anweisung ersetzt werden.

Jetzt, da du weißt, wo du Muster verwenden kannst und den Unterschied zwischen refutierbaren und nicht-refutierbaren Mustern kennst, lass uns alle Syntax betrachten, die wir verwenden können, um Muster zu erstellen.
