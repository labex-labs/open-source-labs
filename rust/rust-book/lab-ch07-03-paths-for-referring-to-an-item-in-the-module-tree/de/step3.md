# Starten von relativen Pfaden mit super

Wir können relative Pfade konstruieren, die im übergeordneten Modul beginnen, anstatt im aktuellen Modul oder der Kistenwurzel, indem wir `super` am Anfang des Pfads verwenden. Dies ist wie das Starten eines Dateisystempfads mit der `..`-Syntax. Das Verwenden von `super` ermöglicht es uns, auf ein Element zu verweisen, das wir wissen, sich im übergeordneten Modul befindet, was das Umorganisieren des Modultrees einfacher macht, wenn das Modul eng mit dem übergeordneten Modul zusammenhängt, aber das übergeordnete Modul vielleicht eines Tages an einen anderen Ort im Modultree verschoben wird.

Betrachten Sie den Code in Listing 7-8, der die Situation modelliert, in der ein Koch eine falsche Bestellung behebt und sie persönlich an den Kunden bringt. Die Funktion `fix_incorrect_order`, die im Modul `back_of_house` definiert ist, ruft die Funktion `deliver_order`, die im übergeordneten Modul definiert ist, auf, indem sie den Pfad zu `deliver_order` angibt, beginnend mit `super`.

Dateiname: `src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

Listing 7-8: Aufrufen einer Funktion mit einem relativen Pfad, der mit `super` beginnt

Die `fix_incorrect_order`-Funktion befindet sich im Modul `back_of_house`, daher können wir `super` verwenden, um zum übergeordneten Modul von `back_of_house` zu gelangen, was in diesem Fall `crate`, die Wurzel, ist. Von dort suchen wir nach `deliver_order` und finden es. Erfolg! Wir denken, dass das Modul `back_of_house` und die `deliver_order`-Funktion wahrscheinlicher in derselben Beziehung zueinander bleiben und zusammen verschoben werden, sollten wir uns entscheiden, den Modultree der Kiste umzuarbeiten. Daher haben wir `super` verwendet, damit wir in Zukunft weniger Stellen im Code aktualisieren müssen, wenn dieser Code in ein anderes Modul verschoben wird.
