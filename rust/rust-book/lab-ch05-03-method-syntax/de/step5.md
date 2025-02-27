# Mehrere impl-Blöcke

Jeder Struktur ist es erlaubt, mehrere `impl`-Blöcke zu haben. Beispielsweise ist Listing 5-15 äquivalent zum in Listing 5-16 gezeigten Code, bei dem jede Methode in ihrem eigenen `impl`-Block steht.

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 5-16: Umformulierung von Listing 5-15 unter Verwendung mehrerer `impl`-Blöcke

Es gibt keinen Grund, diese Methoden hier in mehrere `impl`-Blöcke aufzuteilen, aber dies ist gültige Syntax. Wir werden in Kapitel 10, in dem wir generische Typen und Traits diskutieren, einen Fall sehen, in dem mehrere `impl`-Blöcke nützlich sind.
