# Improving the Error Message

In Listing 12-8 fügen wir in der `new`-Funktion eine Prüfung hinzu, die überprüft, ob der Slice lang genug ist, bevor wir auf Index 1 und Index 2 zugreifen. Wenn der Slice nicht lang genug ist, bricht das Programm ab und zeigt eine bessere Fehlermeldung an.

Dateiname: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

Listing 12-8: Adding a check for the number of arguments

Dieser Code ähnelt der `Guess::new`-Funktion, die wir in Listing 9-13 geschrieben haben, wo wir `panic!` aufgerufen haben, wenn der `value`-Argument außerhalb des Bereichs gültiger Werte lag. Anstatt hier auf einen Bereich von Werten zu prüfen, überprüfen wir, dass die Länge von `args` mindestens `3` ist, und der Rest der Funktion kann unter der Annahme arbeiten, dass diese Bedingung erfüllt ist. Wenn `args` weniger als drei Elemente hat, wird diese Bedingung `true` sein, und wir rufen die `panic!`-Makro auf, um das Programm sofort zu beenden.

Mit diesen wenigen zusätzlichen Codezeilen in `new` führen wir das Programm erneut ohne Argumente aus, um zu sehen, wie die Fehlermeldung jetzt aussieht:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

Diese Ausgabe ist besser: wir haben jetzt eine vernünftige Fehlermeldung. Allerdings haben wir auch unnötige Informationen, die wir unseren Benutzern nicht geben möchten. Vielleicht ist die Technik, die wir in Listing 9-13 verwendet haben, hier nicht die beste: Ein Aufruf von `panic!` ist für ein Programmierproblem eher geeignet als für ein Benutzungsproblem, wie in Kapitel 9 diskutiert. Stattdessen werden wir die andere Technik verwenden, die Sie in Kapitel 9 gelernt haben - das Zurückgeben eines `Result`, das entweder Erfolg oder einen Fehler angibt.
