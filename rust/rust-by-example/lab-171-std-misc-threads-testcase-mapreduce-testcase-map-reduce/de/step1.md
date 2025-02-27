# Testfall: map-reduce

Rust macht es sehr einfach, die Datenverarbeitung parallel zu gestalten, ohne viele der Probleme, die traditionell mit einem solchen Versuch verbunden sind.

Die Standardbibliothek liefert hervorragende Threading-Primitive direkt aus dem Kasten. Diese, kombiniert mit Rust's Konzept der Besitzership und den Aliasing-Regeln, verhindern automatisch Datenkonflikte.

Die Aliasing-Regeln (ein schreibbarer Verweis XOR mehrere lesbare Verweise) verhindern automatisch, dass Sie den Zustand manipulieren, der für andere Threads sichtbar ist. (Wo Synchronisation erforderlich ist, gibt es Synchronisations-Primitive wie `Mutex`-Objekte oder `Channel`s.)

In diesem Beispiel werden wir die Summe aller Ziffern in einem Block von Zahlen berechnen. Wir werden dies tun, indem wir Teile des Blocks in verschiedene Threads aufteilen. Jeder Thread wird die Summe seiner kleinen Ziffernblock berechnen, und anschließend werden wir die Zwischensummen, die von jedem Thread erzeugt werden, addieren.

Beachten Sie, dass, obwohl wir Referenzen über Threadgrenzen hinweg übergeben, Rust versteht, dass wir nur schreibgeschützte Referenzen übergeben, und dass daher keine Unsicherheit oder Datenkonflikte auftreten können. Auch weil die Referenzen, die wir übergeben, `'static`-Lebensdauern haben, versteht Rust, dass unsere Daten nicht zerstört werden, während diese Threads noch laufen. (Wenn Sie nicht-`static`-Daten zwischen Threads teilen müssen, können Sie einen Smart-Pointer wie `Arc` verwenden, um die Daten am Leben zu halten und nicht-`static`-Lebensdauern zu vermeiden.)

```rust
use std::thread;

// Dies ist der `main`-Thread
fn main() {

    // Dies sind unsere zu verarbeitenden Daten.
    // Wir werden die Summe aller Ziffern über einen threaded map-reduce-Algorithmus berechnen.
    // Jeder durch Leerzeichen getrennte Teil wird in einem anderen Thread behandelt.
    //
    // TODO: sehen Sie sich an, was passiert mit der Ausgabe, wenn Sie Leerzeichen einfügen!
    let data = "86967897737416471853297327050364959
11861322575564723963297542624962850
70856234701860851907960690014725639
38397966707106094172783238747669219
52380795257888236525459303330302837
58495327135744041048897885734297812
69920216438980873548808413720956532
16278424637452589860345374828574668";

    // Erstellen Sie ein Vector, um die Kind-Threads zu speichern, die wir erzeugen werden.
    let mut children = vec![];

    /*************************************************************************
     * "Map"-Phase
     *
     * Teilen Sie unsere Daten in Segmente auf und wenden Sie die initiale Verarbeitung an
     ************************************************************************/

    // Teilen Sie unsere Daten in Segmente für die individuelle Berechnung auf
    // jedes Segment wird eine Referenz (&str) auf die tatsächlichen Daten sein
    let chunked_data = data.split_whitespace();

    // Iterieren Sie über die Datensegmente.
    //.enumerate() fügt den aktuellen Schleifenindex zu jedem Element hinzu, das iteriert wird
    // das resultierende Tupel "(index, element)" wird dann sofort
    // in zwei Variablen, "i" und "data_segment" mit einer
    // "Destrukturierungszuweisung" "zerlegt"
    for (i, data_segment) in chunked_data.enumerate() {
        println!("Datensegment {} ist \"{}\"", i, data_segment);

        // Verarbeiten Sie jedes Datensegment in einem separaten Thread
        //
        // spawn() gibt einen Handle auf den neuen Thread zurück,
        // das müssen wir behalten, um auf den zurückgegebenen Wert zuzugreifen
        //
        // 'move || -> u32' ist die Syntax für eine Closure, die:
        // * keine Argumente nimmt ('||')
        // * die Besitzership ihrer eingefangenen Variablen übernimmt ('move') und
        // * einen unsigned 32-Bit-Integer zurückgibt ('-> u32')
        //
        // Rust ist intelligent genug, um den '-> u32' aus der
        // Closure selbst zu inferieren, so dass wir das weglassen könnten.
        //
        // TODO: versuchen Sie, das'move' zu entfernen und sehen Sie, was passiert
        children.push(thread::spawn(move || -> u32 {
            // Berechnen Sie die Zwischensumme dieses Segments:
            let result = data_segment
                        // iterieren Sie über die Zeichen unseres Segments..
                       .chars()
                        //.. konvertieren Sie Textzeichen in ihre numerische Wert..
                       .map(|c| c.to_digit(10).expect("sollte eine Ziffer sein"))
                        //.. und addieren Sie das resultierende Iterator von Zahlen
                       .sum();

            // println! sperrt die Standardeingabeausgabe, so dass kein Textmischung auftritt
            println!("verarbeitetes Segment {}, result={}", i, result);

            // "return" nicht erforderlich, weil Rust eine "Ausdruckssprache" ist, der
            // der zuletzt ausgewertete Ausdruck in jedem Block automatisch seinen Wert ist.
            result

        }));
    }


    /*************************************************************************
     * "Reduce"-Phase
     *
     * Sammeln Sie unsere Zwischenergebnisse und kombinieren Sie sie zu einem endgültigen Ergebnis
     ************************************************************************/

    // Kombinieren Sie die Zwischenergebnisse jedes Threads zu einer einzigen endgültigen Summe.
    //
    // Wir verwenden die "Turbofish" ::<> um der sum() einen Typhinweis zu geben.
    //
    // TODO: versuchen Sie es ohne die Turbofish, indem Sie stattdessen explizit
    // den Typ von final_result angeben
    let final_result = children.into_iter().map(|c| c.join().unwrap()).sum::<u32>();

    println!("Endgültige Summenergebnis: {}", final_result);
}

```

## Aufgaben

Es ist nicht klug, die Anzahl unserer Threads von benutzerdefinierten Daten abhängig zu machen. Was passiert, wenn der Benutzer viele Leerzeichen einfügt? Möchten wir wirklich 2.000 Threads erzeugen? Ändern Sie das Programm so, dass die Daten immer in eine begrenzte Anzahl von Teilen aufgeteilt werden, definiert durch eine statische Konstante am Anfang des Programms.
