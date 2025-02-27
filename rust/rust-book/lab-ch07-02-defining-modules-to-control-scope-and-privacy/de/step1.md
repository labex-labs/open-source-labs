# Defining Modules to Control Scope and Privacy

In diesem Abschnitt werden wir über Module und andere Teile des Modulsystems sprechen, nämlich _Pfade_, die es Ihnen ermöglichen, Elemente zu benennen; das `use`-Schlüsselwort, das einen Pfad in den Geltungsbereich bringt; und das `pub`-Schlüsselwort, um Elemente öffentlich zu machen. Wir werden auch über das `as`-Schlüsselwort, externe Pakete und den Glob-Operator sprechen.

_Module_ helfen uns, den Code innerhalb eines Kratzers für Lesbarkeit und einfache Wiederverwendung zu organisieren. Module ermöglichen uns auch, die _Privatsphäre_ von Elementen zu steuern, da der Code innerhalb eines Moduls standardmäßig privat ist. Private Elemente sind interne Implementierungsdetails, die nicht für die externe Verwendung verfügbar sind. Wir können wählen, Module und die darin enthaltenen Elemente öffentlich zu machen, was sie freigibt, um dass externe Code darauf zugreifen und davon abhängen kann.

Als Beispiel schreiben wir einen Bibliothekskratzer, der die Funktionalität eines Restaurants bietet. Wir werden die Signaturen von Funktionen definieren, aber deren Körper leer lassen, um uns auf die Organisation des Codes statt auf die Implementierung eines Restaurants zu konzentrieren.

In der Restaurantbranche werden einige Teile eines Restaurants als _Vorderseite_ und andere als _Hinterseite_ bezeichnet. Die Vorderseite ist der Bereich, in dem sich die Kunden befinden; dies umfasst den Bereich, in dem die Gastgeber die Kunden platzieren, die Kellner Bestellungen aufnehmen und Bezahlungen entgegennehmen und die Barkeeper Getränke machen. Die Hinterseite ist der Bereich, in dem die Köche und Kochs in der Küche arbeiten, die Geschirrspüler aufräumen und die Manager Verwaltungsarbeiten verrichten.

Um unseren Kratzer so zu strukturieren, können wir seine Funktionen in geschachtelte Module organisieren. Erstellen Sie einen neuen Bibliothekskratzer namens `restaurant`, indem Sie `cargo new restaurant --lib` ausführen. Fügen Sie dann den Code in Listing 7-1 in `src/lib.rs` ein, um einige Module und Funktionssignaturen zu definieren; Dieser Code ist der Vorderseite-Abschnitt.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

Listing 7-1: Ein `front_of_house`-Modul, das andere Module enthält, die dann Funktionen enthalten

Wir definieren ein Modul mit dem `mod`-Schlüsselwort, gefolgt vom Namen des Moduls (in diesem Fall `front_of_house`). Der Körper des Moduls befindet sich dann in geschweiften Klammern. Innerhalb von Modulen können wir andere Module platzieren, wie in diesem Fall mit den Modulen `hosting` und `serving`. Module können auch Definitionen für andere Elemente enthalten, wie Structs, Enums, Konstanten, Traits und - wie in Listing 7-1 - Funktionen.

Durch die Verwendung von Modulen können wir verwandte Definitionen zusammenfassen und erklären, warum sie zusammengehören. Programmierer, die diesen Code verwenden, können sich anhand der Gruppen durch den Code navigieren, anstatt alle Definitionen durchzulesen, was es einfacher macht, die ihnen relevanten Definitionen zu finden. Programmierer, die diesem Code neue Funktionalität hinzufügen möchten, würden wissen, wo sie den Code platzieren müssen, um das Programm organisiert zu halten.

Früher haben wir erwähnt, dass `src/main.rs` und `src/lib.rs` als Kratzerwurzeln bezeichnet werden. Der Grund für ihren Namen ist, dass der Inhalt einer dieser beiden Dateien einen Modul namens `crate` am Stamm der Modulstruktur des Kratzers bildet, der als _Modultree_ bekannt ist.

Listing 7-2 zeigt den Modultree für die Struktur in Listing 7-1.

```bash
crate
└── front_of_house
├── hosting
│ ├── add_to_waitlist
│ └── seat_at_table
└── serving
├── take_order
├── serve_order
└── take_payment
```

Listing 7-2: Der Modultree für den Code in Listing 7-1

Dieser Baum zeigt, wie einige Module in anderen Modulen geschachtelt sind; Beispielsweise ist `hosting` in `front_of_house` geschachtelt. Der Baum zeigt auch, dass einige Module _Geschwister_ sind, was bedeutet, dass sie in demselben Modul definiert sind; `hosting` und `serving` sind Geschwister, die innerhalb von `front_of_house` definiert sind. Wenn Modul A in Modul B enthalten ist, sagen wir, dass Modul A das _Kind_ von Modul B und dass Modul B der _Elternteil_ von Modul A ist. Beachten Sie, dass der gesamte Modultree unter dem impliziten Modul namens `crate` verwurzelt ist.

Der Modultree kann Ihnen an den Verzeichnisbaum Ihres Computers erinnern; Dies ist ein sehr passender Vergleich! Genau wie Verzeichnisse in einem Dateisystem verwenden Sie Module, um Ihren Code zu organisieren. Und genau wie Dateien in einem Verzeichnis benötigen wir einen Weg, unsere Module zu finden.
