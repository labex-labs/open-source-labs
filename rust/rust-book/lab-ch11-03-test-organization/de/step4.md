# Das Testen von privaten Funktionen

Innerhalb der Testcommunity besteht eine Debatte darüber, ob private Funktionen direkt getestet werden sollten, und in anderen Sprachen ist es schwierig oder unmöglich, private Funktionen zu testen. Unabhängig davon, welchem Testideologie du folgst, erlauben Rusts Privatsphäre-Regeln es dir, private Funktionen zu testen. Betrachte den Code in Listing 11-12 mit der privaten Funktion `internal_adder`.

Dateiname: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

Listing 11-12: Das Testen einer privaten Funktion

Beachte, dass die Funktion `internal_adder` nicht als `pub` markiert ist. Tests sind einfach Rust-Code, und das `tests`-Modul ist einfach ein weiteres Modul. Wie wir in "Pfade für die Referenz auf ein Element im Modultree" diskutiert haben, können Elemente in Untermodulen die Elemente in ihren Vorfahrenmodulen verwenden. In diesem Test bringen wir alle Elemente des Elternmoduls des `test`-Moduls in den Geltungsbereich mit `use super::*`, und dann kann der Test `internal_adder` aufrufen. Wenn du denkst, dass private Funktionen nicht getestet werden sollten, zwingt dich nichts in Rust dazu, dies zu tun.
