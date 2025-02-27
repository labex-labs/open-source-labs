# Deklarative Makros mit macro_rules! für die allgemeine Metaprogrammierung

Die am weitesten verbreitete Form von Makros in Rust ist das _deklarative Makro_. Diese werden manchmal auch als "Makros am Beispiel", "`macro_rules!`-Makros" oder einfach nur "Makros" bezeichnet. Im Kern erlauben deklarative Makros es Ihnen, etwas zu schreiben, das ähnelt einem Rust-`match`-Ausdruck. Wie in Kapitel 6 besprochen, sind `match`-Ausdrücke Steuerstrukturen, die einen Ausdruck nehmen, den resultierenden Wert des Ausdrucks mit Mustern vergleichen und dann den mit dem passenden Muster assoziierten Code ausführen. Makros vergleichen auch einen Wert mit Mustern, die mit bestimmten Codeblöcken assoziiert sind: In dieser Situation ist der Wert der in den Makro übergebene literale Rust-Quellcode; die Muster werden mit der Struktur dieses Quellcodes verglichen; und der mit jedem Muster assoziierte Code ersetzt, wenn er übereinstimmt, den an den Makro übergebenen Code. Alles dies geschieht während der Kompilierung.

Um ein Makro zu definieren, verwenden Sie den `macro_rules!`-Konstrukt. Lassen Sie uns untersuchen, wie `macro_rules!` verwendet wird, indem wir uns ansehen, wie das `vec!`-Makro definiert ist. Kapitel 8 hat gezeigt, wie wir das `vec!`-Makro verwenden können, um einen neuen Vektor mit bestimmten Werten zu erstellen. Beispielsweise erzeugt das folgende Makro einen neuen Vektor, der drei ganze Zahlen enthält:

```rust
let v: Vec<u32> = vec![1, 2, 3];
```

Wir könnten auch das `vec!`-Makro verwenden, um einen Vektor von zwei ganzen Zahlen oder einen Vektor von fünf Zeichenfolien zu erstellen. Wir könnten eine Funktion nicht verwenden, um das Gleiche zu tun, da wir die Anzahl oder den Typ der Werte im Voraus nicht kennen würden.

Listing 19-28 zeigt eine leicht vereinfachte Definition des `vec!`-Makros.

Dateiname: `src/lib.rs`

```rust
1 #[macro_export]
2 macro_rules! vec {
  3 ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
          4 $(
              5 temp_vec.push(6 $x);
            )*
          7 temp_vec
        }
    };
}
```

Listing 19-28: Eine vereinfachte Version der `vec!`-Makrodefinition

> Hinweis: Die tatsächliche Definition des `vec!`-Makros in der Standardbibliothek enthält Code, um das richtige Speichervolumen im Voraus zuzuweisen. Dieser Code ist eine Optimierung, die wir hier nicht einschließen, um das Beispiel einfacher zu halten.

Die `#[macro_export]`-Annotation \[1\] gibt an, dass dieses Makro verfügbar sein sollte, wenn das Kratzerzeugnis, in dem das Makro definiert ist, in den Gültigkeitsbereich gebracht wird. Ohne diese Annotation kann das Makro nicht in den Gültigkeitsbereich gebracht werden.

Wir beginnen dann die Makrodefinition mit `macro_rules!` und dem Namen des Makros, das wir definieren, _ohne_ das Ausrufezeichen \[2\]. Der Name, in diesem Fall `vec`, wird von geschweiften Klammern gefolgt, die den Körper der Makrodefinition bezeichnen.

Die Struktur im `vec!`-Körper ähnelt der Struktur eines `match`-Ausdrucks. Hier haben wir einen Arm mit dem Muster `( $( $x:expr ),* )`, gefolgt von `=>` und dem Codeblock, der mit diesem Muster assoziiert ist \[3\]. Wenn das Muster übereinstimmt, wird der zugehörige Codeblock ausgegeben. Da dies das einzige Muster in diesem Makro ist, gibt es nur eine gültige Möglichkeit, zu matchen; jedes andere Muster führt zu einem Fehler. Komplexere Makros werden mehr als einen Arm haben.

Die gültige Mustersyntax in Makrodefinitionen unterscheidet sich von der Mustersyntax, die in Kapitel 18 behandelt wurde, da Makromuster gegen die Rust-Codestruktur statt gegen Werte gematcht werden. Lassen Sie uns durchgehen, was die Musterteile in Listing 19-28 bedeuten; für die volle Makromustersyntax siehe die Rust-Referenz unter *https://doc.rust-lang.org/reference/macros-by-example.html*.

Zunächst verwenden wir eine Klammerung, um das gesamte Muster zu umfassen. Wir verwenden ein Dollarzeichen (`$`), um eine Variable im Makrosystem zu deklarieren, die den mit dem Muster übereinstimmenden Rust-Code enthalten wird. Das Dollarzeichen macht klar, dass es sich um eine Makrovariable handelt, im Gegensatz zu einer normalen Rust-Variable. Danach folgt eine Klammerung, die Werte fängt, die mit dem Muster innerhalb der Klammer übereinstimmen, um in den Ersetzungscode zu verwenden. Innerhalb von `$()` ist `$x:expr`, das mit jedem Rust-Ausdruck übereinstimmt und dem Ausdruck den Namen `$x` gibt.

Das Komma nach `$()` gibt an, dass ein literales Komma-Separatorzeichen optional nach dem Code erscheinen könnte, der mit dem Code in `$()` übereinstimmt. Das `*` gibt an, dass das Muster null oder mehr von dem, was vor dem `*` steht, übereinstimmt.

Wenn wir dieses Makro mit `vec![1, 2, 3];` aufrufen, stimmt das `$x`-Muster dreimal mit den drei Ausdrücken `1`, `2` und `3` überein.

Lassen Sie uns jetzt das Muster im Körper des Codes betrachten, der mit diesem Arm assoziiert ist: `temp_vec.push()` \[5\] innerhalb von `$()* bei [4] und [7] wird für jedes Teil generiert, das mit`$()` im Muster null oder mehr mal übereinstimmt, je nachdem, wie oft das Muster übereinstimmt. Das `$x`[6] wird mit jedem übereinstimmenden Ausdruck ersetzt. Wenn wir dieses Makro mit`vec\[1, 2, 3\];\` aufrufen, wird der generierte Code, der diesen Makroaufruf ersetzt, der folgende sein:

    {
        let mut temp_vec = Vec::new();
        temp_vec.push(1);
        temp_vec.push(2);
        temp_vec.push(3);
        temp_vec
    }

Wir haben ein Makro definiert, das beliebig viele Argumente beliebigen Typs akzeptieren kann und Code generieren kann, um einen Vektor zu erstellen, der die angegebenen Elemente enthält.

Um mehr über die Schreibung von Makros zu erfahren, konsultieren Sie die Online-Dokumentation oder andere Ressourcen, wie "The Little Book of Rust Macros" unter *https://veykril.github.io/tlborm*, das von Daniel Keep gestartet und von Lukas Wirth fortgesetzt wurde.
