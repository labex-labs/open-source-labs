# Pfade zum Verweisen auf ein Element im Modultree

Um Rust zu zeigen, wo es ein Element im Modultree finden soll, verwenden wir einen Pfad auf die gleiche Weise, wie wir einen Pfad verwenden, wenn wir einen Dateisystem navigieren. Um eine Funktion aufzurufen, müssen wir ihren Pfad kennen.

Ein Pfad kann zwei Formen annehmen:

- Ein _absoluter Pfad_ ist der vollständige Pfad, der von einer Kistenwurzel aus beginnt; für Code aus einem externen Kasten beginnt der absolute Pfad mit dem Kastennamen, und für Code aus dem aktuellen Kasten beginnt er mit dem Literal `crate`.
- Ein _relativer Pfad_ beginnt bei dem aktuellen Modul und verwendet `self`, `super` oder einen Bezeichner im aktuellen Modul.

Sowohl absolute als auch relative Pfade werden von einem oder mehreren Bezeichnern, die durch Doppelpunkte (`::`) getrennt sind, gefolgt.

Wenn wir zurück zu Listing 7-1 gehen, sagen wir, dass wir die `add_to_waitlist`-Funktion aufrufen möchten. Dies ist dasselbe wie fragen: Was ist der Pfad zur `add_to_waitlist`-Funktion? Listing 7-3 enthält Listing 7-1 mit einigen der Module und Funktionen entfernt.

Wir werden zwei Wege zeigen, um die `add_to_waitlist`-Funktion aus einer neuen Funktion, `eat_at_restaurant`, die in der Kistenwurzel definiert ist, aufzurufen. Diese Pfade sind korrekt, aber es bleibt noch ein weiteres Problem übrig, das verhindert, dass dieses Beispiel so kompiliert wird. Wir werden gleich erklären, warum.

Die `eat_at_restaurant`-Funktion ist Teil der öffentlichen API unseres Bibliothekskastens, daher markieren wir sie mit dem Schlüsselwort `pub`. In "Exposing Paths with the pub Keyword" werden wir genauer auf `pub` eingehen.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absoluter Pfad
    crate::front_of_house::hosting::add_to_waitlist();

    // Relativer Pfad
    front_of_house::hosting::add_to_waitlist();
}
```

Listing 7-3: Aufrufen der `add_to_waitlist`-Funktion mit absoluten und relativen Pfaden

Wenn wir die `add_to_waitlist`-Funktion zum ersten Mal in `eat_at_restaurant` aufrufen, verwenden wir einen absoluten Pfad. Die `add_to_waitlist`-Funktion ist in demselben Kasten wie `eat_at_restaurant` definiert, was bedeutet, dass wir das Schlüsselwort `crate` verwenden können, um einen absoluten Pfad zu beginnen. Wir fügen dann jedes der folgenden Module hinzu, bis wir zu `add_to_waitlist` gelangen. Man kann sich ein Dateisystem mit derselben Struktur vorstellen: Wir würden den Pfad `/front_of_house/hosting/add_to_waitlist` angeben, um das `add_to_waitlist`-Programm auszuführen; das Verwenden des `crate`-Namens, um von der Kistenwurzel aus zu beginnen, ist wie das Verwenden von `/`, um von der Dateisystemwurzel in Ihrer Shell aus zu beginnen.

Wenn wir die `add_to_waitlist` zum zweiten Mal in `eat_at_restaurant` aufrufen, verwenden wir einen relativen Pfad. Der Pfad beginnt mit `front_of_house`, dem Namen des Moduls, das auf derselben Ebene des Modultrees wie `eat_at_restaurant` definiert ist. Hier entspräche der Dateisystempfad dem Pfad `front_of_house/hosting/add_to_waitlist`. Ein Start mit einem Modulnamen bedeutet, dass der Pfad relativ ist.

Die Entscheidung, ob ein relativer oder absoluter Pfad verwendet werden soll, ist eine Entscheidung, die Sie aufgrund Ihres Projekts treffen müssen, und es hängt davon ab, ob Sie wahrscheinlicher die Elementdefinitionscode separat oder zusammen mit dem Code verschieben, der das Element verwendet. Beispielsweise würden wir, wenn wir das `front_of_house`-Modul und die `eat_at_restaurant`-Funktion in ein Modul namens `customer_experience` verschieben, den absoluten Pfad zu `add_to_waitlist` aktualisieren müssen, aber der relative Pfad würde immer noch gültig sein. Wenn wir die `eat_at_restaurant`-Funktion jedoch separat in ein Modul namens `dining` verschieben würden, würde der absolute Pfad zum `add_to_waitlist`-Aufruf gleich bleiben, aber der relative Pfad müsste aktualisiert werden. Unser allgemeines Präferenz besteht darin, absolute Pfade anzugeben, da es wahrscheinlicher ist, dass wir Codedefinitionen und Elementaufrufe unabhängig voneinander verschieben möchten.

Lassen Sie uns versuchen, Listing 7-3 zu kompilieren und herauszufinden, warum es noch nicht kompilieren wird! Die Fehler, die wir erhalten, werden in Listing 7-4 gezeigt.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: Modul `hosting` ist privat
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ privates Modul
  |
note: Das Modul `hosting` ist hier definiert
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: Modul `hosting` ist privat
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ privates Modul
   |
note: Das Modul `hosting` ist hier definiert
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

Listing 7-4: Compilerfehler beim Erstellen des Codes in Listing 7-3

Die Fehlermeldungen sagen, dass das Modul `hosting` privat ist. Mit anderen Worten, wir haben die korrekten Pfade für das `hosting`-Modul und die `add_to_waitlist`-Funktion, aber Rust lässt uns sie nicht verwenden, weil es keinen Zugang zu den privaten Abschnitten hat. In Rust sind alle Elemente (Funktionen, Methoden, Strukturen, Enums, Module und Konstanten) standardmäßig für übergeordnete Module privat. Wenn Sie ein Element wie eine Funktion oder eine Struktur privat machen möchten, legen Sie es in ein Modul.

Elemente in einem übergeordneten Modul können die privaten Elemente in Untermodulen nicht verwenden, aber Elemente in Untermodulen können die Elemente in ihren Vorfahrenmodulen verwenden. Dies liegt daran, dass Untermodule ihre Implementierungsdetails umschließen und verbergen, aber die Untermodule können den Kontext sehen, in dem sie definiert sind. Um mit unserer Metapher fortzufahren, denken Sie sich die Privatsphäre-Regeln wie das Hinterzimmer eines Restaurants: Was dort passiert, ist privat für Restaurantkunden, aber Büromanager können alles im Restaurant sehen und tun, das sie betreiben.

Rust hat die Modulsystemfunktion so gewählt, dass das Verbergen innerer Implementierungsdetails die Standard-Einstellung ist. Auf diese Weise wissen Sie, welche Teile des inneren Codes Sie ändern können, ohne den äußeren Code zu brechen. Rust gibt Ihnen jedoch die Möglichkeit, innere Teile des Codes von Untermodulen an übergeordnete Vorfahrenmodule zu exponieren, indem Sie das Schlüsselwort `pub` verwenden, um ein Element öffentlich zu machen.
