# Verwendung von Supertraits

Manchmal könnten Sie eine Trait-Definition schreiben, die von einem anderen Trait abhängt: Damit ein Typ die erste Trait implementiert, möchten Sie verlangen, dass dieser Typ auch das zweite Trait implementiert. Sie würden dies tun, um die assoziierten Elemente des zweiten Traits in Ihrer Trait-Definition nutzen zu können. Das Trait, auf das Ihre Trait-Definition zurückgreift, wird als _Supertrait_ Ihres Traits bezeichnet.

Nehmen wir beispielsweise an, dass wir ein `OutlinePrint`-Trait mit einer `outline_print`-Methode erstellen möchten, die einen gegebenen Wert so formatiert ausgibt, dass er in Sternchen eingerahmt ist. Das heißt, wenn wir eine `Point`-Struktur haben, die das Standardbibliothekstrait `Display` implementiert, um `(x, y)` zu ergeben, und wir `outline_print` auf einer `Point`-Instanz aufrufen, die `1` für `x` und `3` für `y` hat, sollte es folgendes ausgeben:

    **********
    *        *
    * (1, 3) *
    *        *
    **********

In der Implementierung der `outline_print`-Methode möchten wir die Funktionalität des `Display`-Traits nutzen. Daher müssen wir angeben, dass das `OutlinePrint`-Trait nur für Typen funktionieren wird, die auch `Display` implementieren und die Funktionalität bieten, die `OutlinePrint` benötigt. Wir können das in der Trait-Definition tun, indem wir `OutlinePrint: Display` angeben. Diese Technik ähnelt der Hinzufügung eines Trait-Bounds zu einem Trait. Listing 19-22 zeigt eine Implementierung des `OutlinePrint`-Traits.

Dateiname: `src/main.rs`

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

Listing 19-22: Implementierung des `OutlinePrint`-Traits, das die Funktionalität von `Display` benötigt

Da wir angegeben haben, dass `OutlinePrint` das `Display`-Trait erfordert, können wir die `to_string`-Funktion verwenden, die automatisch für jeden Typ implementiert wird, der `Display` implementiert. Wenn wir versuchten, `to_string` zu verwenden, ohne einen Doppelpunkt hinzuzufügen und das `Display`-Trait nach dem Traitnamen anzugeben, würden wir einen Fehler erhalten, der besagt, dass keine Methode namens `to_string` für den Typ `&Self` im aktuellen Gültigkeitsbereich gefunden wurde.

Schauen wir uns an, was passiert, wenn wir versuchen, `OutlinePrint` auf einem Typ zu implementieren, der `Display` nicht implementiert, wie die `Point`-Struktur:

Dateiname: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Wir erhalten einen Fehler, der besagt, dass `Display` erforderlich ist, aber nicht implementiert ist:

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

Um dies zu beheben, implementieren wir `Display` auf `Point` und erfüllen die Einschränkung, die `OutlinePrint` erfordert, wie folgt:

Dateiname: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Anschließend wird die Implementierung des `OutlinePrint`-Traits auf `Point` erfolgreich kompilieren, und wir können `outline_print` auf einer `Point`-Instanz aufrufen, um sie innerhalb eines Sternchenrahmens anzuzeigen.
