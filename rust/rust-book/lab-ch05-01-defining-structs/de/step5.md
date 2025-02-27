# Strukturen ohne Felder, ähnlich der Einheit

Es ist auch möglich, Structs zu definieren, die keine Felder haben! Diese werden als _einheitsähnliche Structs_ bezeichnet, weil sie ähnlich wie `()`, dem Einheitstyp, den wir in "The Tuple Type" erwähnt haben, verhalten. Einheitsähnliche Structs können nützlich sein, wenn Sie ein Merkmal auf einem bestimmten Typ implementieren müssen, aber keine Daten haben, die Sie in dem Typ selbst speichern möchten. Wir werden in Kapitel 10 über Merkmale sprechen. Hier ist ein Beispiel für die Deklaration und Instanziierung eines einheitlichen Structs namens `AlwaysEqual`:

Dateiname: `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

Um `AlwaysEqual` zu definieren, verwenden wir das Schlüsselwort `struct`, den Namen, den wir möchten, und dann ein Semikolon. Keine geschweiften Klammern oder Klammern erforderlich! Dann können wir in ähnlicher Weise eine Instanz von `AlwaysEqual` in der `subject`-Variablen erhalten: indem wir den definierten Namen verwenden, ohne jede geschweifte Klammer oder Klammer. Stellen Sie sich vor, dass wir später ein Verhalten für diesen Typ implementieren, sodass jede Instanz von `AlwaysEqual` immer gleich ist wie jede Instanz eines anderen Typs, vielleicht um ein bekanntes Ergebnis für Testzwecke zu haben. Wir bräuchten keine Daten, um dieses Verhalten zu implementieren! In Kapitel 10 werden Sie sehen, wie Sie Merkmale definieren und auf jeden Typ implementieren, einschließlich einheitsähnlicher Structs.

> **Eigentum an Struct-Daten**
>
> In der `User`-Struct-Definition in Listing 5-1 haben wir den eigenen `String`-Typ verwendet, statt des `&str`-String-Slices-Typs. Dies ist eine bewusste Wahl, weil wir möchten, dass jede Instanz dieses Structs alle ihre Daten besitzt und dass diese Daten solange gültig sind, wie der gesamte Struct gültig ist.
>
> Es ist auch möglich, dass Structs Referenzen auf Daten speichern, die von etwas anderem besessen werden, aber dazu muss das Konzept der _Lebensdauer_ verwendet werden, ein Rust-Feature, über das wir in Kapitel 10 sprechen werden. Lebensdauern gewährleisten, dass die von einem Struct referenzierten Daten solange gültig sind, wie der Struct selbst. Nehmen wir an, Sie versuchen, eine Referenz in einem Struct zu speichern, ohne die Lebensdauer anzugeben, wie im folgenden Beispiel in `src/main.rs`; dies wird nicht funktionieren:
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> Der Compiler wird anzeigen, dass Lebensdauerangaben erforderlich sind:
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> In Kapitel 10 werden wir diskutieren, wie diese Fehler behoben werden können, sodass Sie Referenzen in Structs speichern können, aber für jetzt werden wir Fehler wie diese mit eigenen Typen wie `String` anstelle von Referenzen wie `&str` beheben.
