# Generic Lifetimes in Functions

Wir werden eine Funktion schreiben, die die längere von zwei String-Slices zurückgibt. Diese Funktion wird zwei String-Slices entgegennehmen und einen einzelnen String-Slice zurückgeben. Nachdem wir die `longest`-Funktion implementiert haben, sollte der Code in Listing 10-19 `The longest string is abcd` ausgeben.

Dateiname: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

Listing 10-19: Eine `main`-Funktion, die die `longest`-Funktion aufruft, um die längere von zwei String-Slices zu finden

Beachten Sie, dass wir möchten, dass die Funktion String-Slices entgegennimmt, die Referenzen sind, statt Strings, weil wir nicht möchten, dass die `longest`-Funktion die Eigentumsgewalt über ihre Parameter übernimmt. Lesen Sie "String Slices as Parameters" für eine detailliertere Diskussion darüber, warum die Parameter, die wir in Listing 10-19 verwenden, die richtigen sind.

Wenn wir versuchen, die `longest`-Funktion wie in Listing 10-20 zu implementieren, wird sie nicht kompilieren.

Dateiname: `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listing 10-20: Eine Implementierung der `longest`-Funktion, die die längere von zwei String-Slices zurückgibt, aber noch nicht kompiliert

Stattdessen erhalten wir den folgenden Fehler, der sich auf Lebenszeiten bezieht:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

Der Hilfetext zeigt, dass der Rückgabetyp einen generischen Lebenszeitparameter benötigt, weil Rust nicht wissen kann, auf welche der beiden Referenzen (`x` oder `y`) sich der zurückgegebene Wert bezieht. Tatsächlich wissen wir es auch nicht, weil der `if`-Block im Körper dieser Funktion eine Referenz auf `x` zurückgibt und der `else`-Block eine Referenz auf `y`!

Wenn wir diese Funktion definieren, wissen wir nicht, welche konkreten Werte in diese Funktion übergeben werden, also wissen wir nicht, ob der `if`-Fall oder der `else`-Fall ausgeführt wird. Wir wissen auch nicht die konkreten Lebenszeiten der Referenzen, die übergeben werden, also können wir nicht wie in Listings 10-17 und 10-18 die Bereiche betrachten, um zu bestimmen, ob die Referenz, die wir zurückgeben, immer gültig ist. Der Borrow-Checker kann dies auch nicht bestimmen, weil er nicht weiß, wie die Lebenszeiten von `x` und `y` zur Lebenszeit des Rückgabewerts zusammenhängen. Um diesen Fehler zu beheben, werden wir generische Lebenszeitparameter hinzufügen, die die Beziehung zwischen den Referenzen definieren, damit der Borrow-Checker seine Analyse durchführen kann.
