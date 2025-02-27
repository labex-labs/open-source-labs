# Hängende Referenzen

In Sprachen mit Zeigern ist es leicht, versehentlich einen _hängenden Zeiger_ zu erstellen - einen Zeiger, der auf einen Speicherort verweist, der möglicherweise an jemand anderen gegeben wurde - indem man einen Teil des Speichers freigibt, während ein Zeiger auf diesen Speicherort erhalten bleibt. Im Gegensatz dazu gewährleistet der Rust-Compiler, dass Referenzen niemals hängende Referenzen sein werden: Wenn Sie eine Referenz auf einige Daten haben, wird der Compiler sicherstellen, dass die Daten nicht außer Gültigkeitsbereich gelangen, bevor die Referenz auf die Daten außer Gültigkeitsbereich geht.

Lassen Sie uns versuchen, eine hängende Referenz zu erstellen, um zu sehen, wie Rust sie mit einem Kompilierfehler verhindert:

Dateiname: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Hier ist der Fehler:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

Diese Fehlermeldung bezieht sich auf eine Funktion, die wir noch nicht behandelt haben: Lebensdauern. Wir werden Lebensdauern im Kapitel 10 im Detail diskutieren. Wenn Sie jedoch die Teile über Lebensdauern außer Acht lassen, enthält die Meldung den Schlüssel zu dem, warum dieser Code ein Problem ist:

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

Schauen wir uns genauer an, was genau in jeder Phase unseres `dangle`-Codes geschieht:

    // src/main.rs
    fn dangle() -> &String { // dangle gibt eine Referenz auf eine String zurück

        let s = String::from("hello"); // s ist eine neue String

        &s // wir geben eine Referenz auf die String, s zurück
    } // Hier geht s außer Gültigkeitsbereich und wird gelöscht, also geht auch sein Speicher verloren
      // Gefahr!

Da `s` innerhalb von `dangle` erstellt wird, wird `s` deallokiert, wenn der Code von `dangle` abgeschlossen ist. Aber wir haben versucht, eine Referenz darauf zurückzugeben. Das bedeutet, dass diese Referenz auf einen ungültigen `String` verweisen würde. Das geht nicht! Rust lässt uns das nicht tun.

Die Lösung hier besteht darin, den `String` direkt zurückzugeben:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

Dies funktioniert ohne Probleme. Die Eigentumsgewalt wird übergeben, und nichts wird deallokiert.
