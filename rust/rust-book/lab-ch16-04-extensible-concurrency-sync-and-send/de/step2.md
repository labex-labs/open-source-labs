# Ermöglichen der Eigentumsübertragung zwischen Threads mit Send

Das Marker-Trait `Send` gibt an, dass das Eigentum an Werten des Typs, der `Send` implementiert, zwischen Threads übertragen werden kann. Fast jeder Rust-Typ ist `Send`, aber es gibt einige Ausnahmen, einschließlich `Rc<T>`: Dieses kann nicht `Send` sein, denn wenn Sie einen `Rc<T>`-Wert klonen und versuchen, das Eigentum des Klons an einen anderen Thread zu übertragen, könnten beide Threads gleichzeitig den Referenzzähler aktualisieren. Aus diesem Grund ist `Rc<T>` für die Verwendung in ein-Thread-Situationen implementiert, in denen Sie keine leistungsmindernden Auswirkungen der Thread-Sicherheit in Kauf nehmen möchten.

Daher stellen Rusts Typsystem und Trait-Bounds sicher, dass Sie niemals versehentlich einen `Rc<T>`-Wert unsicher über Threads senden können. Als wir dies in Listing 16-14 versuchten, erhielten wir den Fehler `the trait Send is not implemented for Rc<Mutex<i32>>`. Als wir zu `Arc<T>` wechselten, das `Send` ist, kompilierte der Code.

Jeder Typ, der vollständig aus `Send`-Typen besteht, wird automatisch ebenfalls als `Send` markiert. Fast alle primitiven Typen sind `Send`, abgesehen von Raw Pointern, die wir in Kapitel 19 besprechen werden.
