# Namen mit `pub use` erneut exportieren

Wenn wir einen Namen mit dem `use`-Schlüsselwort in den Gültigkeitsbereich bringen, ist der Name, der im neuen Gültigkeitsbereich verfügbar ist, privat. Um es dem Code zu ermöglichen, der unseren Code aufruft, auf diesen Namen so zu verweisen, als wäre er in dem Gültigkeitsbereich des Codes definiert, können wir `pub` und `use` kombinieren. Diese Technik wird als _erneutes Exportieren_ bezeichnet, weil wir ein Element in den Gültigkeitsbereich bringen, aber dieses Element auch anderen zur Verfügung stellen, damit sie es in ihren Gültigkeitsbereich bringen können.

Listing 7-17 zeigt den Code aus Listing 7-11, wobei der `use` im Root-Modul in `pub use` geändert wurde.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-17: Einen Namen für jeden Code verfügbar machen, der ihn aus einem neuen Gültigkeitsbereich mit `pub use` verwenden kann

Bevor diese Änderung erfolgte, hätte externer Code die `add_to_waitlist`-Funktion aufrufen müssen, indem er den Pfad `restaurant::front_of_house::hosting::add_to_waitlist()` verwendet. Jetzt, da dieses `pub use` das `hosting`-Modul aus dem Root-Modul erneut exportiert hat, kann externer Code stattdessen den Pfad `restaurant::hosting::add_to_waitlist()` verwenden.

Das erneute Exportieren ist nützlich, wenn die interne Struktur Ihres Codes von der Art der Denkweise der Programmierer unterscheidet, die Ihren Code aufrufen. Beispielsweise denken die Menschen, die das Restaurant betreiben, an "Vorderseite des Hauses" und "Hinterseite des Hauses" im Rahmen dieser Restaurant-Metapher. Aber Kunden, die ein Restaurant besuchen, werden wahrscheinlich nicht in diesen Begriffen über die Teile des Restaurants nachdenken. Mit `pub use` können wir unseren Code mit einer Struktur schreiben, aber eine andere Struktur offenbaren. Dadurch wird unsere Bibliothek für Programmierer, die an der Bibliothek arbeiten, und Programmierer, die die Bibliothek aufrufen, gut strukturiert. Wir werden in "Exporting a Convenient Public API with pub use" ein weiteres Beispiel für `pub use` und wie es die Dokumentation Ihres Crates beeinflusst, betrachten.
