# Fehlerbehandlung mit Result

Wir beschäftigen uns immer noch mit dieser Codezeile. Wir diskutieren jetzt eine dritte Zeile des Codes, beachten Sie jedoch, dass es immer noch Teil einer einzelnen logischen Codezeile ist. Der nächste Teil ist diese Methode:

```rust
.expect("Fehler beim Lesen der Zeile");
```

Wir hätten diesen Code auch so schreiben können:

```rust
io::stdin().read_line(&mut guess).expect("Fehler beim Lesen der Zeile");
```

Allerdings ist eine lange Zeile schwer lesbar, daher ist es am besten, sie aufzuteilen. Es ist oft ratsam, einen Zeilenumbruch und andere Leerzeichen einzufügen, um lange Zeilen aufzubrechen, wenn Sie eine Methode mit der `.method_name()`-Syntax aufrufen. Jetzt besprechen wir, was diese Zeile macht.

Wie bereits erwähnt, schreibt `read_line` alles, was der Benutzer eingibt, in die Zeichenfolge, die wir an sie übergeben, aber es gibt auch einen `Result`-Wert zurück. `Result` ist eine _Enumeration_, oft auch als _Enum_ bezeichnet, das ein Typ ist, der in einem von mehreren möglichen Zuständen sein kann. Wir nennen jeden möglichen Zustand einen _Variant_.

Kapitel 6 wird Enums im Detail behandeln. Der Zweck dieser `Result`-Typen ist es, Fehlerbehandlungsinformationen zu codieren.

Die Varianten von `Result` sind `Ok` und `Err`. Die `Ok`-Variant zeigt an, dass die Operation erfolgreich war, und innerhalb von `Ok` ist der erfolgreich generierte Wert. Die `Err`-Variant bedeutet, dass die Operation fehlgeschlagen ist, und `Err` enthält Informationen darüber, wie oder warum die Operation fehlgeschlagen ist.

Werte des `Result`-Typs haben wie Werte jedes Typs Methoden, die auf ihnen definiert sind. Eine Instanz von `Result` hat eine `expect`-Methode, die Sie aufrufen können. Wenn diese `Result`-Instanz ein `Err`-Wert ist, wird `expect` das Programm abstürzen lassen und die Nachricht anzeigen, die Sie als Argument an `expect` übergeben haben. Wenn die `read_line`-Methode einen `Err` zurückgibt, ist dies wahrscheinlich das Ergebnis eines Fehlers, der von dem zugrunde liegenden Betriebssystem stammt. Wenn diese `Result`-Instanz ein `Ok`-Wert ist, nimmt `expect` den Rückgabewert, den `Ok` enthält, und gibt Ihnen genau diesen Wert zurück, damit Sie ihn verwenden können. In diesem Fall ist dieser Wert die Anzahl der Bytes in der Benutzer-Eingabe.

Wenn Sie `expect` nicht aufrufen, wird das Programm kompilieren, aber Sie erhalten eine Warnung:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust warnt, dass Sie den von `read_line` zurückgegebenen `Result`-Wert nicht verwendet haben, was darauf hinweist, dass das Programm einen möglichen Fehler nicht behandelt hat.

Der richtige Weg, die Warnung zu unterdrücken, ist es, tatsächlich Fehlerbehandlungs-Code zu schreiben, aber in unserem Fall möchten wir einfach das Programm abstürzen lassen, wenn ein Problem auftritt, daher können wir `expect` verwenden. Sie werden in Kapitel 9 lernen, wie man Fehler behebt.
