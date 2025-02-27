# if/else

Das Verzweigen mit `if`-`else` ähnelt anderen Sprachen. Anders als viele davon muss die boolesche Bedingung nicht in Klammern eingeschlossen sein, und jeder Bedingung folgt ein Block. `if`-`else`-Bedingungen sind Ausdrücke, und alle Zweige müssen den gleichen Typ zurückgeben.

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} ist negativ", n);
    } else if n > 0 {
        print!("{} ist positiv", n);
    } else {
        print!("{} ist null", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", und ist eine kleine Zahl, zehnfach vergrößern");

            // Dieser Ausdruck gibt einen `i32` zurück.
            10 * n
        } else {
            println!(", und ist eine große Zahl, die Zahl halbieren");

            // Dieser Ausdruck muss ebenfalls einen `i32` zurückgeben.
            n / 2
            // TODO ^ Versuchen Sie, diesen Ausdruck mit einem Semikolon zu unterdrücken.
        };
    //   ^ Vergessen Sie nicht, hier ein Semikolon zu setzen! Alle `let`-Bindungen brauchen es.

    println!("{} -> {}", n, big_n);
}
```
