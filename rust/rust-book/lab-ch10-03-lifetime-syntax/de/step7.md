# Thinking in Terms of Lifetimes

Die Art, in der Sie Lebenszeitparameter angeben müssen, hängt davon ab, was Ihre Funktion macht. Beispielsweise würden wir keine Lebenszeit für den Parameter `y` angeben müssen, wenn wir die Implementierung der `longest`-Funktion ändern würden, um immer den ersten Parameter statt den längsten String-Slice zurückzugeben. Der folgende Code wird kompilieren:

Dateiname: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

Wir haben einen Lebenszeitparameter `'a` für den Parameter `x` und den Rückgabetyp angegeben, aber nicht für den Parameter `y`, weil die Lebenszeit von `y` keine Beziehung zur Lebenszeit von `x` oder zum Rückgabewert hat.

Wenn eine Referenz von einer Funktion zurückgegeben wird, muss der Lebenszeitparameter für den Rückgabetyp mit dem Lebenszeitparameter eines der Parameter übereinstimmen. Wenn die zurückgegebene Referenz _nicht_ auf einen der Parameter verweist, muss sie auf einen innerhalb dieser Funktion erstellten Wert verweisen. Dies wäre jedoch ein verhängender Verweis, da der Wert am Ende der Funktion außer Gültigkeitsbereich geht. Betrachten Sie diese versuchte Implementierung der `longest`-Funktion, die nicht kompilieren wird:

Dateiname: `src/main.rs`

```rust
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

Hier, obwohl wir einen Lebenszeitparameter `'a` für den Rückgabetyp angegeben haben, wird diese Implementierung fehlschlagen, weil die Lebenszeit des Rückgabewerts überhaupt keine Beziehung zur Lebenszeit der Parameter hat. Hier ist die Fehlermeldung, die wir erhalten:

```bash
error[E0515]: cannot return reference to local variable `result`
  --> src/main.rs:11:5
   |
11 |     result.as_str()
   |     ^^^^^^^^^^^^^^^ returns a reference to data owned by the
current function
```

Das Problem ist, dass `result` außer Gültigkeitsbereich geht und am Ende der `longest`-Funktion bereinigt wird. Wir versuchen auch, eine Referenz auf `result` aus der Funktion zurückzugeben. Es gibt keine Möglichkeit, dass wir Lebenszeitparameter angeben, die den verhängenden Verweis ändern würden, und Rust lässt uns keinen verhängenden Verweis erstellen. In diesem Fall wäre die beste Lösung, einen eigenen Datentyp zurückzugeben, anstatt eine Referenz, sodass die aufrufende Funktion dann für das Bereinigen des Werts verantwortlich ist.

Letztendlich ist die Lebenszeitsyntax dazu da, die Lebenszeiten verschiedener Parameter und Rückgabewerte von Funktionen zu verbinden. Wenn sie verbunden sind, hat Rust genug Informationen, um sicherheitsrelevante Operationen zu ermöglichen und Operationen zu verbieten, die verhängende Zeiger erzeugen oder anderweitig die Arbeitsspeichersicherheit verletzen.
