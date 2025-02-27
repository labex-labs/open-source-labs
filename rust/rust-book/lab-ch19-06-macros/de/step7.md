# Funktionsähnliche Makros

Funktionsähnliche Makros definieren Makros, die wie Funktionsaufrufe aussehen. Ähnlich wie `macro_rules!`-Makros sind sie flexibler als Funktionen; beispielsweise können sie eine unbekannte Anzahl von Argumenten akzeptieren. Allerdings können `macro_rules!`-Makros nur mit der match-ähnlichen Syntax definiert werden, die wir in "Declarative Macros with macro_rules! for General Metaprogramming" diskutiert haben. Funktionsähnliche Makros nehmen einen `TokenStream`-Parameter entgegen, und ihre Definition manipuliert diesen `TokenStream` wie die anderen beiden Arten von prozeduralen Makros mit Rust-Code. Ein Beispiel für ein funktionsähnliches Makro ist ein `sql!`-Makro, das möglicherweise wie folgt aufgerufen wird:

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

Dieses Makro würde den SQL-Befehl darin analysieren und überprüfen, ob er syntaktisch korrekt ist, was eine viel komplexere Verarbeitung ist als das, was ein `macro_rules!`-Makro tun kann. Das `sql!`-Makro würde wie folgt definiert werden:

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

Diese Definition ähnelt der Signatur des benutzerdefinierten `derive`-Makros: Wir erhalten die Tokens, die innerhalb der Klammern sind, und geben den Code zurück, den wir generieren möchten.
