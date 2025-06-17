# Verfolgen von Leihvorgängen zur Laufzeit mit RefCell`<T>`

Beim Erstellen unveränderbarer und veränderbarer Referenzen verwenden wir die `&`- und `&mut`-Syntax entsprechend. Mit `RefCell<T>` verwenden wir die Methoden `borrow` und `borrow_mut`, die Teil der sicheren API von `RefCell<T>` sind. Die `borrow`-Methode gibt den Smart-Pointer-Typ `Ref<T>` zurück, und `borrow_mut` gibt den Smart-Pointer-Typ `RefMut<T>` zurück. Beide Typen implementieren `Deref`, sodass wir sie wie reguläre Referenzen behandeln können.

`RefCell<T>` verfolgt, wie viele Smart-Pointer vom Typ `Ref<T>` und `RefMut<T>` aktuell aktiv sind. Jedes Mal, wenn wir `borrow` aufrufen, erhöht `RefCell<T>` die Anzahl der aktiven unveränderbaren Leihvorgänge. Wenn ein `Ref<T>`-Wert außerhalb des Gültigkeitsbereichs gelangt, geht die Anzahl der unveränderbaren Leihvorgänge um 1 zurück. Genau wie die Leihregeln zur Compilezeit lässt `RefCell<T>` uns zu jedem Zeitpunkt viele unveränderbare Leihvorgänge oder einen veränderbaren Leihvorgang haben.

Wenn wir versuchen, diese Regeln zu verletzen, wird die Implementierung von `RefCell<T>` statt eines Compilerfehlers wie bei Referenzen zur Laufzeit einen `panic!` auslösen. Listing 15-23 zeigt eine Änderung der Implementierung von `send` in Listing 15-22. Wir versuchen absichtlich, zwei veränderbare Leihvorgänge für denselben Gültigkeitsbereich zu erstellen, um zu zeigen, dass `RefCell<T>` uns dies zur Laufzeit verhindert.

Dateiname: `src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

Listing 15-23: Erstellen von zwei veränderbaren Referenzen im selben Gültigkeitsbereich, um zu sehen, dass `RefCell<T>` einen `panic!` auslösen wird

Wir erstellen eine Variable `one_borrow` für den von `borrow_mut` zurückgegebenen Smart-Pointer vom Typ `RefMut<T>`. Dann erstellen wir in der gleichen Weise einen weiteren veränderbaren Leihvorgang in der Variable `two_borrow`. Dies erzeugt zwei veränderbare Referenzen im selben Gültigkeitsbereich, was nicht erlaubt ist. Wenn wir die Tests für unsere Bibliothek ausführen, wird der Code in Listing 15-23 ohne Fehler kompilieren, aber der Test wird fehlschlagen:

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Beachten Sie, dass der Code mit der Fehlermeldung `already borrowed: BorrowMutError` einen `panic!` ausgelöst hat. So behandelt `RefCell<T>` Verletzungen der Leihregeln zur Laufzeit.

Das Entscheiden, Leihfehler zur Laufzeit statt zur Compilezeit zu fangen, wie wir es hier getan haben, bedeutet, dass Sie möglicherweise Fehler in Ihrem Code erst später im Entwicklungsprozess finden: möglicherweise erst, wenn Ihr Code in der Produktion bereitgestellt wird. Außerdem würde Ihr Code aufgrund der Verfolgung der Leihvorgänge zur Laufzeit statt zur Compilezeit einen geringen Leistungsverlust bei der Laufzeit aufweisen. Allerdings ermöglicht das Verwenden von `RefCell<T>`, ein Mock-Objekt zu schreiben, das sich selbst modifizieren kann, um die Nachrichten zu verfolgen, die es gesehen hat, während Sie es in einem Kontext verwenden, in dem nur unveränderbare Werte erlaubt sind. Sie können `RefCell<T>` trotz seiner Nachteile verwenden, um mehr Funktionalität zu erhalten als reguläre Referenzen bieten.
