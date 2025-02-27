# Ausführen eines Teils der Tests nach Namen

Manchmal kann das Ausführen eines vollständigen Testpakets lange Zeit in Anspruch nehmen. Wenn du an einem bestimmten Bereich des Codes arbeitest, möchtest du möglicherweise nur die Tests ausführen, die sich auf diesen Code beziehen. Du kannst wählen, welche Tests ausgeführt werden sollen, indem du `cargo test` den Namen oder die Namen der zu ausführenden Tests als Argument übergibst.

Um zu demonstrieren, wie ein Teil der Tests ausgeführt wird, werden wir zunächst drei Tests für unsere `add_two`-Funktion erstellen, wie in Listing 11-11 gezeigt, und wählen, welche davon ausgeführt werden sollen.

Dateiname: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Listing 11-11: Drei Tests mit drei verschiedenen Namen

Wenn wir die Tests ohne Angabe von Argumenten ausführen, wie wir es zuvor gesehen haben, werden alle Tests parallel ausgeführt:

    running 3 tests
    test tests::add_three_and_two... ok
    test tests::add_two_and_two... ok
    test tests::one_hundred... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
