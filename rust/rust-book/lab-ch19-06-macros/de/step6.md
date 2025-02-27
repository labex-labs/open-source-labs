# Attributähnliche Makros

Attributähnliche Makros ähneln benutzerdefinierten `derive`-Makros, aber anstatt Code für das `derive`-Attribut zu generieren, ermöglichen sie es Ihnen, neue Attribute zu erstellen. Sie sind auch flexibler: `derive` funktioniert nur für Structs und Enums; Attribute können auch auf andere Elemente angewendet werden, wie z. B. Funktionen. Hier ist ein Beispiel für die Verwendung eines attributähnlichen Makros. Nehmen Sie an, Sie haben ein Attribut namens `route`, das Funktionen annotiert, wenn Sie ein Webanwendungsframework verwenden:

```rust
#[route(GET, "/")]
fn index() {
```

Dieses `#[route]`-Attribut würde vom Framework als prozedurales Makro definiert werden. Die Signatur der Makrodefinition-Funktion würde so aussehen:

    #[proc_macro_attribute]
    pub fn route(
        attr: TokenStream,
        item: TokenStream
    ) -> TokenStream {

Hier haben wir zwei Parameter vom Typ `TokenStream`. Der erste ist für den Inhalt des Attributes: der `GET, "/"`-Teil. Der zweite ist der Körper des Elements, an das das Attribut angefügt ist: in diesem Fall `fn index() {}` und der Rest des Funktionskörpers.

Ansonsten funktionieren attributähnliche Makros auf die gleiche Weise wie benutzerdefinierte `derive`-Makros: Sie erstellen ein Kratzerzeugnis mit dem `proc-macro`-Kratzertyp und implementieren eine Funktion, die den gewünschten Code generiert!
