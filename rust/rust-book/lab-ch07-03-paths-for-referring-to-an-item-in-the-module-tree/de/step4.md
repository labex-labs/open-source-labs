# Machen von Structs und Enums öffentlich

Wir können auch `pub` verwenden, um Structs und Enums als öffentlich zu kennzeichnen, aber es gibt einige zusätzliche Details bei der Verwendung von `pub` mit Structs und Enums. Wenn wir `pub` vor einer Struct-Definition verwenden, machen wir die Struct öffentlich, aber die Felder der Struct bleiben immer noch privat. Wir können jedes Feld individuell öffentlich oder privat machen. In Listing 7-9 haben wir eine öffentliche `back_of_house::Breakfast`-Struct definiert, mit einem öffentlichen `toast`-Feld, aber einem privaten `seasonal_fruit`-Feld. Dies modelliert den Fall in einem Restaurant, in dem der Kunde die Art von Brot wählen kann, das zu einem Gericht gehört, aber der Koch entscheidet, welches Obst mit dem Gericht serviert wird, basierend auf der Saison und dem Vorrat. Das verfügbare Obst ändert sich schnell, sodass die Kunden das Obst nicht auswählen oder sogar nicht sehen können, welches sie erhalten.

Dateiname: `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Bestellen Sie ein Frühstück im Sommer mit Roggenbrot
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Ändern Sie sich über das Brot, das wir möchten
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // Die nächste Zeile wird nicht kompilieren, wenn wir sie entsperren; wir dürfen
    // nicht sehen oder ändern das saisonale Obst, das mit dem Gericht serviert wird
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Listing 7-9: Eine Struct mit einigen öffentlichen und einigen privaten Feldern

Da das `toast`-Feld in der `back_of_house::Breakfast`-Struct öffentlich ist, können wir in `eat_at_restaurant` auf das `toast`-Feld schreiben und lesen, indem wir die Punktnotation verwenden. Beachten Sie, dass wir das `seasonal_fruit`-Feld in `eat_at_restaurant` nicht verwenden können, da `seasonal_fruit` privat ist. Versuchen Sie, die Zeile zum Ändern des `seasonal_fruit`-Feldwerts zu entsperren, um zu sehen, welchen Fehler Sie erhalten!

Beachten Sie auch, dass die `back_of_house::Breakfast`-Struct ein privates Feld hat, daher muss die Struct eine öffentliche assoziierte Funktion bereitstellen, die eine Instanz von `Breakfast` konstruiert (wir haben sie hier `summer` genannt). Wenn `Breakfast` keine solche Funktion hätte, könnten wir in `eat_at_restaurant` keine Instanz von `Breakfast` erstellen, da wir den Wert des privaten `seasonal_fruit`-Felds in `eat_at_restaurant` nicht setzen könnten.

Im Gegensatz dazu, wenn wir einen Enum als öffentlich machen, sind alle seine Varianten dann öffentlich. Wir brauchen nur das `pub` vor dem `enum`-Schlüsselwort, wie in Listing 7-10 gezeigt.

Dateiname: `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

Listing 7-10: Das Kennzeichnen eines Enums als öffentlich macht alle seine Varianten öffentlich.

Da wir den `Appetizer`-Enum als öffentlich gemacht haben, können wir die `Soup`- und `Salad`-Varianten in `eat_at_restaurant` verwenden.

Enums sind nicht sehr nützlich, es sei denn, ihre Varianten sind öffentlich; es wäre lästig, in jedem Fall alle Enum-Varianten mit `pub` zu annotieren, daher ist die Standardeinstellung für Enum-Varianten, öffentlich zu sein. Structs sind oft nützlich, auch wenn ihre Felder nicht öffentlich sind, daher folgen Struct-Felder der allgemeinen Regel, dass alles standardmäßig privat ist, es sei denn, es wird mit `pub` annotiert.

Es gibt noch eine Situation, die `pub` betrifft, die wir noch nicht behandelt haben, und das ist unsere letzte Modulsystem-Funktion: das `use`-Schlüsselwort. Wir werden zuerst `use` für sich allein behandeln und dann zeigen, wie `pub` und `use` kombiniert werden können.
