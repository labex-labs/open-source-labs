# Entwicklungsabhängigkeiten

Manchmal ist es erforderlich, Abhängigkeiten nur für Tests (oder Beispiele oder Benchmarks) zu haben. Solche Abhängigkeiten werden der `Cargo.toml` in der `[dev-dependencies]`-Sektion hinzugefügt. Diese Abhängigkeiten werden nicht an andere Pakete weitergegeben, die von diesem Paket abhängen.

Ein solches Beispiel ist [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html), das die standardmäßigen `assert_eq!`- und `assert_ne!`-Makros erweitert, um farbige Differenzen bereitzustellen.
Datei `Cargo.toml`:

```toml
# standard crate data is left out
[dev-dependencies]
pretty_assertions = "1"
```

Datei `src/lib.rs`:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // crate for test-only use. Cannot be used in non-test code.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
