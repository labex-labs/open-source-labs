# Prozedurale Makros für die Generierung von Code aus Attributen

Die zweite Form von Makros ist das prozedurale Makro, das sich eher wie eine Funktion verhält (und eine Art Prozedur ist). _Prozedurale Makros_ akzeptieren einige Code als Eingabe, operieren auf diesem Code und erzeugen als Ausgabe einen anderen Code, anstatt wie deklarative Makros gegen Muster zu matchen und den Code mit anderem Code zu ersetzen. Die drei Arten von prozeduralen Makros sind benutzerdefiniertes `derive`, attributähnlich und funktionähnlich, und alle funktionieren auf ähnliche Weise.

Wenn Sie prozedurale Makros erstellen, müssen die Definitionen in ihrem eigenen Kratzerzeugnis mit einem speziellen Kratzertyp liegen. Dies liegt an komplexen technischen Gründen, die wir in Zukunft eliminieren möchten. In Listing 19-29 zeigen wir, wie Sie ein prozedurales Makro definieren, wobei `some_attribute` ein Platzhalter für die Verwendung einer bestimmten Makrovariante ist.

Dateiname: `src/lib.rs`

```rust
use proc_macro::TokenStream;

#[some_attribute]
pub fn some_name(input: TokenStream) -> TokenStream {
}
```

Listing 19-29: Ein Beispiel für die Definition eines prozeduralen Makros

Die Funktion, die ein prozedurales Makro definiert, nimmt einen `TokenStream` als Eingabe und erzeugt einen `TokenStream` als Ausgabe. Der `TokenStream`-Typ wird vom `proc_macro`-Kratzerzeugnis definiert, das mit Rust mitgeliefert wird, und stellt eine Sequenz von Tokens dar. Dies ist der Kern des Makros: Der Quellcode, auf dem das Makro operiert, bildet den Eingabe-`TokenStream` und der Code, den das Makro erzeugt, ist der Ausgabe-`TokenStream`. Die Funktion hat auch ein Attribut angefügt, das angibt, welche Art von prozeduralem Makro wir erstellen. Wir können in demselben Kratzerzeugnis mehrere Arten von prozeduralen Makros haben.

Lassen Sie uns die verschiedenen Arten von prozeduralen Makros betrachten. Wir beginnen mit einem benutzerdefinierten `derive`-Makro und erklären dann die kleinen Unterschiede, die die anderen Formen unterschiedlich machen.
