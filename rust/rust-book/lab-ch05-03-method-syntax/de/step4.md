# Assoziierte Funktionen

Alle Funktionen, die innerhalb eines `impl`-Blocks definiert werden, werden als _assoziierte Funktionen_ bezeichnet, weil sie mit dem Typ assoziiert sind, der nach dem `impl` benannt ist. Wir können assoziierte Funktionen definieren, die `self` nicht als ersten Parameter haben (und daher keine Methoden sind), weil sie keine Instanz des Typs benötigen, um zu funktionieren. Wir haben bereits eine solche Funktion verwendet: die `String::from`-Funktion, die auf dem `String`-Typ definiert ist.

Assoziierte Funktionen, die keine Methoden sind, werden oft für Konstruktoren verwendet, die eine neue Instanz der Struktur zurückgeben. Diese werden oft `new` genannt, aber `new` ist kein spezieller Name und ist nicht in die Sprache eingebaut. Beispielsweise könnten wir eine assoziierte Funktion namens `square` bereitstellen, die einen Dimensionenparameter hätte und diesen als Breite und Höhe verwenden würde, was es somit einfacher macht, ein quadratisches `Rectangle` zu erstellen, anstatt den gleichen Wert zweimal angeben zu müssen:

Dateiname: `src/main.rs`

```rust
impl Rectangle {
    fn square(size: u32) -> 1 Self  {
      2 Self  {
            width: size,
            height: size,
        }
    }
}
```

Die `Self`-Schlüsselwörter im Rückgabetyp \[1\] und im Funktionskörper \[2\] sind Aliase für den Typ, der nach dem `impl`-Schlüsselwort erscheint, was in diesem Fall `Rectangle` ist.

Um diese assoziierte Funktion aufzurufen, verwenden wir die `::`-Syntax mit dem Struktur-Namen; `let sq = Rectangle::square(3);` ist ein Beispiel. Diese Funktion ist in der Struktur namenspezifiziert: Die `::`-Syntax wird sowohl für assoziierte Funktionen als auch für durch Module erstellte Namensräume verwendet. Wir werden in Kapitel 7 über Module sprechen.
