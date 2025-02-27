# Kommentieren von enthaltenen Elementen

Der Dokumenationskommentar `//!` fügt Dokumentation zu dem Element hinzu, das die Kommentare _enthält_, anstatt zu den Elementen, die _nach_ den Kommentaren stehen. Wir verwenden diese Dokumenationskommentare normalerweise innerhalb der Crate-Wurzeldatei (`src/lib.rs` üblicherweise) oder innerhalb eines Moduls, um die gesamte Crate oder das Modul zu dokumentieren.

Zum Beispiel, um Dokumentation hinzuzufügen, die den Zweck der `my_crate`-Crate beschreibt, die die `add_one`-Funktion enthält, fügen wir Dokumenationskommentare hinzu, die mit `//!` beginnen, am Anfang der `src/lib.rs`-Datei, wie in Listing 14-2 gezeigt.

Dateiname: `src/lib.rs`

```rust
//! # Meine Crate
//!
//! `my_crate` ist eine Sammlung von Hilfsmitteln, um bestimmte
//! Berechnungen einfacher durchzuführen.

/// Fügt eins zur angegebenen Zahl hinzu.
--snip--
```

Listing 14-2: Dokumentation für die gesamte `my_crate`-Crate

Beachten Sie, dass nach der letzten Zeile, die mit `//!` beginnt, kein Code mehr vorhanden ist. Da wir die Kommentare mit `//!` statt mit `///` begonnen haben, dokumentieren wir das Element, das diesen Kommentar enthält, anstatt ein Element, das diesem Kommentar folgt. In diesem Fall ist das Element die `src/lib.rs`-Datei, die die Crate-Wurzel ist. Diese Kommentare beschreiben die gesamte Crate.

Wenn wir `cargo doc --open` ausführen, werden diese Kommentare auf der Titelseite der Dokumentation für `my_crate` über der Liste der öffentlichen Elemente in der Crate angezeigt, wie in Abbildung 14-2 gezeigt.

Abbildung 14-2: Gerenderte Dokumentation für `my_crate`, einschließlich des Kommentars, der die gesamte Crate beschreibt

Dokumentationskommentare innerhalb von Elementen sind besonders nützlich für die Beschreibung von Crates und Modulen. Verwenden Sie sie, um den Gesamtzweck des Containers zu erklären, um Ihren Benutzern zu helfen, die Struktur der Crate zu verstehen.
