# Ein Beispielprogramm mit Structs

Um zu verstehen, wann wir Structs verwenden möchten, schreiben wir ein Programm, das die Fläche eines Rechtecks berechnet. Wir beginnen mit einzelnen Variablen und refaktorisieren das Programm, bis wir Structs verwenden.

Lassen Sie uns mit Cargo ein neues binäres Projekt namens _rectangles_ erstellen, das die Breite und Höhe eines Rechtecks in Pixeln angibt und die Fläche des Rechtecks berechnet. Listing 5-8 zeigt ein kurzes Programm, das genau das auf eine Weise in unserer Projekt-`src/main.rs` macht.

Dateiname: `src/main.rs`

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "Die Fläche des Rechtecks beträgt {} Quadratpixel.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

Listing 5-8: Berechnung der Fläche eines Rechtecks, das durch separate Breite- und Höhe-Variablen angegeben wird

Führen Sie nun dieses Programm mit `cargo run` aus:

```rust
Die Fläche des Rechtecks beträgt 1500 Quadratpixel.
```

Dieser Code gelangt erfolgreich zu der Fläche des Rechtecks, indem er die `area`-Funktion mit jeder Dimension aufruft, aber wir können noch mehr tun, um diesen Code klar und lesbar zu machen.

Das Problem mit diesem Code ist in der Signatur von `area` offensichtlich:

```rust
fn area(width: u32, height: u32) -> u32 {
```

Die `area`-Funktion soll die Fläche eines Rechtecks berechnen, aber die von uns geschriebene Funktion hat zwei Parameter, und es ist in unserem gesamten Programm nirgends klar, dass die Parameter zusammenhängen. Es wäre lesbarer und leichter zu verwalten, Breite und Höhe zusammen zu gruppieren. Wir haben bereits eine Möglichkeit diskutiert, wie wir das in "Der Tuple-Typ" tun könnten: indem wir Tupel verwenden.
