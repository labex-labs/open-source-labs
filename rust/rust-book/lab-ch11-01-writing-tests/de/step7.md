# Verwenden von Result\<T, E\> in Tests

Bisher landen alle unsere Tests im Fehlerfall im Zustand eines Panik. Wir können auch Tests schreiben, die `Result<T, E>` verwenden! Hier ist der Test aus Listing 11-1, umgeschrieben, um `Result<T, E>` zu verwenden und einen `Err` zurückzugeben, anstatt einen Fehler auszulösen:

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

Die `it_works`-Funktion hat jetzt den Rückgabetyp `Result<(), String>`. Im Funktionskörper geben wir statt dem Aufruf des `assert_eq!`-Makros `Ok(())` zurück, wenn der Test besteht, und einen `Err` mit einem `String` darin, wenn der Test fehlschlägt.

Das Schreiben von Tests, sodass sie einen `Result<T, E>` zurückgeben, ermöglicht es Ihnen, den Fragezeichen-Operator im Testkörper zu verwenden, was ein bequemer Weg sein kann, Tests zu schreiben, die fehlschlagen sollten, wenn eine beliebige Operation innerhalb von ihnen einen `Err`-Variant zurückgibt.

Sie können die `#[should_panic]`-Annotation nicht auf Tests verwenden, die `Result<T, E>` verwenden. Um zu überprüfen, dass eine Operation einen `Err`-Variant zurückgibt, _verwenden Sie_ nicht den Fragezeichen-Operator auf dem `Result<T, E>`-Wert. Verwenden Sie stattdessen `assert!(value.is_err())`.

Jetzt, da Sie verschiedene Möglichkeiten kennen, Tests zu schreiben, schauen wir uns an, was passiert, wenn wir unsere Tests ausführen, und erkunden die verschiedenen Optionen, die wir mit `cargo test` verwenden können.
