# Ein Anwendungsfall für interne Veränderbarkeit: Mock-Objekte

Manchmal verwendet ein Programmierer während des Tests einen Typ anstelle eines anderen Typs, um bestimmte Verhaltensweisen zu beobachten und sicherzustellen, dass diese korrekt implementiert sind. Dieser Platzhaltertyp wird als _Testdoublé_ bezeichnet. Man kann sich das in etwa so vorstellen wie einen Stuntman in der Filmproduktion, der für einen Schauspieler tritt, um eine besonders schwierige Szene zu filmen. Testdoublés vertreten andere Typen, wenn wir Tests ausführen. _Mock-Objekte_ sind spezielle Arten von Testdoublés, die aufzeichnen, was während eines Tests passiert, sodass Sie feststellen können, ob die richtigen Aktionen stattgefunden haben.

Rust hat keine Objekte im selben Sinne wie andere Sprachen, und das Standardbibliothek von Rust hat keine eingebautes Mock-Objekt-Funktionalität wie einige andere Sprachen. Allerdings können Sie definitiv eine Struktur erstellen, die die gleichen Zwecke wie ein Mock-Objekt erfüllt.

Hier ist die Szene, die wir testen werden: Wir werden eine Bibliothek erstellen, die einen Wert im Vergleich zu einem maximalen Wert verfolgt und Nachrichten sendet, je nachdem, wie nah der aktuelle Wert am maximalen Wert ist. Diese Bibliothek könnte beispielsweise verwendet werden, um die Quote der Anzahl der API-Aufrufe zu verfolgen, die ein Benutzer tätigen darf.

Unsere Bibliothek wird nur die Funktionalität zur Verfügung stellen, um zu verfolgen, wie nah ein Wert am maximalen Wert ist und welche Nachrichten zu welchen Zeiten gesendet werden sollten. Anwendungen, die unsere Bibliothek verwenden, sollen das Mechanismus zum Senden der Nachrichten bereitstellen: Die Anwendung könnte eine Nachricht in der Anwendung ablegen, eine E-Mail senden, eine SMS senden oder etwas anderes tun. Die Bibliothek muss diese Details nicht kennen. Alles, was sie benötigt, ist etwas, das ein von uns bereitgestelltes Merkmal namens `Messenger` implementiert. Listing 15-20 zeigt den Code der Bibliothek.

Dateiname: `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
             .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
             .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
             .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Listing 15-20: Eine Bibliothek, um zu verfolgen, wie nah ein Wert am maximalen Wert ist und eine Warnung auszugeben, wenn der Wert auf bestimmten Niveaus ist

Ein wichtiger Teil dieses Codes ist, dass das `Messenger`-Merkmal eine Methode namens `send` hat, die eine unveränderbare Referenz auf `self` und den Text der Nachricht annimmt \[1\]. Dieses Merkmal ist die Schnittstelle, die unser Mock-Objekt implementieren muss, damit das Mock auf die gleiche Weise wie ein echtes Objekt verwendet werden kann. Der andere wichtige Teil ist, dass wir das Verhalten der `set_value`-Methode auf dem `LimitTracker` testen möchten \[2\]. Wir können das, was wir für den `value`-Parameter übergeben, ändern, aber `set_value` gibt nichts zurück, worauf wir uns als Behauptung verlassen können. Wir möchten in der Lage sein zu sagen, dass wenn wir einen `LimitTracker` mit etwas erstellen, das das `Messenger`-Merkmal implementiert und einen bestimmten Wert für `max`, wenn wir verschiedene Zahlen für `value` übergeben, der Messenger dazu aufgefordert wird, die entsprechenden Nachrichten zu senden.

Wir brauchen ein Mock-Objekt, das statt einer E-Mail oder SMS zu senden, wenn wir `send` aufrufen, nur die Nachrichten verfolgen wird, die es aufgefordert wird zu senden. Wir können eine neue Instanz des Mock-Objekts erstellen, einen `LimitTracker` erstellen, der das Mock-Objekt verwendet, die `set_value`-Methode auf `LimitTracker` aufrufen und dann überprüfen, ob das Mock-Objekt die Nachrichten hat, die wir erwarten. Listing 15-21 zeigt einen Versuch, ein Mock-Objekt zu implementieren, um genau das zu tun, aber der Leihprüfungsmechanismus wird es nicht zulassen.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Listing 15-21: Ein Versuch, ein `MockMessenger` zu implementieren, das nicht vom Leihprüfungsmechanismus zugelassen wird

Dieser Testcode definiert eine `MockMessenger`-Struktur \[1\], die ein `sent_messages`-Feld mit einem `Vec` von `String`-Werten hat \[2\], um die Nachrichten zu verfolgen, die es aufgefordert wird zu senden. Wir definieren auch eine assoziierte Funktion `new` \[3\], um es bequem zu machen, neue `MockMessenger`-Werte zu erstellen, die mit einer leeren Liste von Nachrichten beginnen. Wir implementieren dann das `Messenger`-Merkmal für `MockMessenger` \[4\], sodass wir ein `MockMessenger` einem `LimitTracker` geben können. In der Definition der `send`-Methode \[5\] nehmen wir die als Parameter übergebene Nachricht entgegen und speichern sie in der `MockMessenger`-Liste von `sent_messages`.

Im Test testen wir, was passiert, wenn der `LimitTracker` aufgefordert wird, `value` auf etwas zu setzen, das mehr als 75 Prozent des `max`-Werts ist \[6\]. Zunächst erstellen wir ein neues `MockMessenger`, das mit einer leeren Liste von Nachrichten beginnen wird. Dann erstellen wir einen neuen `LimitTracker` und geben ihm eine Referenz auf das neue `MockMessenger` und einen `max`-Wert von `100`. Wir rufen die `set_value`-Methode auf dem `LimitTracker` mit einem Wert von `80` auf, was mehr als 75 Prozent von 100 ist. Dann stellen wir sicher, dass die Liste der Nachrichten, die das `MockMessenger` verfolgt, jetzt eine Nachricht enthalten sollte.

Allerdings gibt es ein Problem mit diesem Test, wie hier gezeigt:

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

Wir können das `MockMessenger` nicht ändern, um die Nachrichten zu verfolgen, weil die `send`-Methode eine unveränderbare Referenz auf `self` annimmt. Wir können auch nicht den Vorschlag aus der Fehlermeldung folgen und `&mut self` verwenden, weil dann die Signatur von `send` nicht mit der Signatur in der `Messenger`-Merkmaldefinition übereinstimmen würde (versuchen Sie es gerne und sehen Sie, welche Fehlermeldung Sie erhalten).

Dies ist eine Situation, in der die interne Veränderbarkeit helfen kann! Wir werden die `sent_messages` in einer `RefCell<T>` speichern, und dann wird die `send`-Methode in der Lage sein, `sent_messages` zu ändern, um die Nachrichten zu speichern, die wir gesehen haben. Listing 15-22 zeigt, wie das aussieht.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3.borrow_mut()
               .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Listing 15-22: Verwenden von `RefCell<T>` zum Mutieren eines inneren Werts, während der äußere Wert als unveränderbar betrachtet wird

Das `sent_messages`-Feld ist jetzt vom Typ `RefCell<Vec<String>>` \[1\] anstelle von `Vec<String>`. In der `new`-Funktion erstellen wir eine neue `RefCell<Vec<String>>`-Instanz um den leeren Vektor \[2\].

Für die Implementierung der `send`-Methode ist der erste Parameter immer noch eine unveränderbare Referenz auf `self`, was der Merkmaldefinition entspricht. Wir rufen `borrow_mut` auf der `RefCell<Vec<String>>` in `self.sent_messages` auf \[3\], um eine veränderbare Referenz auf den Wert innerhalb der `RefCell<Vec<String>>`, also auf den Vektor, zu erhalten. Dann können wir `push` auf der veränderbaren Referenz auf den Vektor aufrufen, um die Nachrichten während des Tests zu verfolgen.

Die letzte Änderung, die wir vornehmen müssen, ist in der Behauptung: Um zu sehen, wie viele Elemente im inneren Vektor sind, rufen wir `borrow` auf der `RefCell<Vec<String>>` auf, um eine unveränderbare Referenz auf den Vektor zu erhalten \[4\].

Jetzt, nachdem Sie gesehen haben, wie man `RefCell<T>` verwendet, lassen Sie uns untersuchen, wie es funktioniert!
