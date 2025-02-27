# Erlauben der Übertragung der Eigentumsgewalt zwischen Threads mit Send

Das `Send`-Marker-Trait gibt an, dass die Eigentumsgewalt von Werten des Typs, der `Send` implementiert, zwischen Threads übertragen werden kann. Fast jeder Rust-Typ ist `Send`, aber es gibt einige Ausnahmen, darunter `Rc<T>`: Dies kann nicht `Send` sein, weil, wenn Sie einen `Rc<T>`-Wert klonen und versuchen, die Eigentumsgewalt des Klons an einen anderen Thread zu übertragen, beide Threads möglicherweise gleichzeitig die Referenzzählung aktualisieren. Aus diesem Grund ist `Rc<T>` für die Verwendung in einthreadigen Situationen implementiert, in denen Sie die Leistungsnachteile der Threadsicherheit vermeiden möchten.

Dadurch gewährleistet das Typsystem von Rust und die Trait-Bounds, dass Sie niemals versehentlich einen `Rc<T>`-Wert unsicher über Threads senden können. Als wir dies in Listing 16-14 versucht haben, haben wir den Fehler erhalten: `the trait`Send`is not implemented for`Rc\<Mutex`<i32>`{=html}\>\``. Als wir zu `Arc`<T>`{=html}`wechselten, das`Send` ist, hat der Code kompiliert.

Jeder Typ, der ausschließlich aus `Send`-Typen besteht, wird automatisch ebenfalls als `Send` markiert. Fast alle primitiven Typen sind `Send`, abgesehen von rohen Zeigern, über die wir im Kapitel 19 sprechen werden.
