# Besitz und Funktionen

Die Mechanismen beim Übergabe eines Werts an eine Funktion ähneln denen beim Zuweisen eines Werts an eine Variable. Das Übergeben einer Variable an eine Funktion wird entweder verschieben oder kopieren, genau wie die Zuweisung. Listing 4-3 zeigt ein Beispiel mit einigen Anmerkungen, die anzeigen, wann Variablen in und außerhalb ihres Gültigkeitsbereichs sind.

    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s tritt in den Gültigkeitsbereich

        takes_ownership(s);             // der Wert von s wird in die Funktion verschoben...
                                        //... und ist hier somit nicht mehr gültig

        let x = 5;                      // x tritt in den Gültigkeitsbereich

        makes_copy(x);                  // x würde in die Funktion verschoben werden,
                                        // aber i32 implementiert Copy, so dass es
                                        // danach noch in Ordnung ist, x zu verwenden

    } // Hier tritt x außerhalb seines Gültigkeitsbereichs, dann s. Allerdings
      // da der Wert von s verschoben wurde, passiert nichts Besonderes

    fn takes_ownership(some_string: String) { // some_string tritt in den Gültigkeitsbereich
        println!("{some_string}");
    } // Hier tritt some_string außerhalb seines Gültigkeitsbereichs und `drop`
      // wird aufgerufen. Der zugrunde liegende Arbeitsspeicher wird freigegeben

    fn makes_copy(some_integer: i32) { // some_integer tritt in den Gültigkeitsbereich
        println!("{some_integer}");
    } // Hier tritt some_integer außerhalb seines Gültigkeitsbereichs.
      // Passiert nichts Besonderes

Listing 4-3: Funktionen mit Besitz und Gültigkeitsbereich annotiert

Wenn wir versuchen, `s` nach dem Aufruf von `takes_ownership` zu verwenden, würde Rust einen Compile-Fehler werfen. Diese statischen Prüfungen schützen uns vor Fehlern. Versuchen Sie, Code in `main` hinzuzufügen, der `s` und `x` verwendet, um zu sehen, wo Sie sie verwenden können und wo die Besitzregeln Sie davon abhalten.
