# Verwirklichung nützlicher Dokumentationskommentare

Genau dokumentieren Sie Ihre Pakete, um anderen Benutzern zu helfen, zu verstehen, wie und wann sie diese verwenden können. Es lohnt sich daher, die Zeit für die Erstellung von Dokumentationen aufzuwenden. Im dritten Kapitel haben wir diskutiert, wie man Rust-Code mit zwei Schrägstrichen (`//`) kommentiert. Rust hat auch einen speziellen Art von Kommentar für die Dokumentation, der bequem als _Dokumentationskommentar_ bezeichnet wird und HTML-Dokumentation erzeugt. Die HTML-Anzeige zeigt den Inhalt von Dokumentationskommentaren für öffentliche API-Elemente an, die für Programmierer von Interesse sind, die wissen möchten, wie sie Ihr Crate _verwenden_, im Gegensatz zu wie Ihr Crate _implementiert_ ist.

Dokumentationskommentare verwenden drei Schrägstriche (`///`) anstelle von zwei und unterstützen die Markdown-Notation zur Formatierung des Textes. Platzieren Sie die Dokumentationskommentare direkt vor dem Element, das sie dokumentieren. Listing 14-1 zeigt die Dokumentationskommentare für eine `add_one`-Funktion in einem Crate namens `my_crate`.

Dateiname: `src/lib.rs`

````rust
/// Fügt eins zur angegebenen Zahl hinzu.
///
/// # Beispiele
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
````

Listing 14-1: Ein Dokumentationskommentar für eine Funktion

Hier geben wir eine Beschreibung davon, was die `add_one`-Funktion macht, beginnen einen Abschnitt mit dem Titel `Beispiele` und geben dann Code, der zeigt, wie man die `add_one`-Funktion verwendet. Wir können die HTML-Dokumentation aus diesem Dokumentationskommentar generieren, indem wir `cargo doc` ausführen. Dieser Befehl führt das mit Rust verteilte `rustdoc`-Tool aus und legt die generierte HTML-Dokumentation im `target/doc`-Verzeichnis ab.

Zur Bequemlichkeit führt `cargo doc --open` die HTML-Erstellung für die Dokumentation Ihres aktuellen Crates (sowie die Dokumentation aller Abhängigkeiten Ihres Crates) durch und öffnet das Ergebnis in einem Webbrowser. Navigieren Sie zur `add_one`-Funktion, und Sie werden sehen, wie der Text in den Dokumentationskommentaren gerendert wird, wie in Abbildung 14-1 gezeigt.

Abbildung 14-1: HTML-Dokumentation für die `add_one`-Funktion
