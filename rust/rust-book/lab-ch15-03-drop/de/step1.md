# Code beim Aufräumen mit dem Drop-Trait ausführen

Das zweite für das Smart-Pointer-Muster wichtige Trait ist `Drop`, das es ermöglicht, anzugeben, was passiert, wenn ein Wert außer Gültigkeitsbereich gelangt. Sie können eine Implementierung für das `Drop`-Trait für jeden Typ bereitstellen, und dieser Code kann verwendet werden, um Ressourcen wie Dateien oder Netzwerkverbindungen freizugeben.

Wir führen `Drop` im Zusammenhang mit Smart-Pointern ein, weil die Funktionalität des `Drop`-Traits fast immer bei der Implementierung eines Smart-Pointers verwendet wird. Beispielsweise wird beim Löschen eines `Box<T>` der Speicherbereich auf dem Heap freigegeben, auf den die Box zeigt.

In einigen Sprachen müssen Programmierer für bestimmte Typen jedes Mal, wenn sie eine Instanz dieser Typen fertig verwenden, Code aufrufen, um den Speicher oder die Ressourcen freizugeben. Dazu gehören Dateihandle, Sockets und Locks. Wenn sie vergessen, kann das System überlastet werden und abstürzen. In Rust können Sie angeben, dass ein bestimmter Codeabschnitt ausgeführt wird, wenn ein Wert außer Gültigkeitsbereich gelangt, und der Compiler fügt diesen Code automatisch ein. Dadurch müssen Sie sich nicht darum kümmern, Bereinigungs-Code überall im Programm zu platzieren, wenn eine Instanz eines bestimmten Typs fertig ist – Sie verlieren trotzdem keine Ressourcen!

Sie geben den Code an, der ausgeführt werden soll, wenn ein Wert außer Gültigkeitsbereich gelangt, indem Sie das `Drop`-Trait implementieren. Das `Drop`-Trait erfordert, dass Sie eine Methode namens `drop` implementieren, die eine mutierende Referenz auf `self` annimmt. Um zu sehen, wann Rust `drop` aufruft, implementieren wir `drop` vorerst mit `println!`-Anweisungen.

Listing 15-14 zeigt eine `CustomSmartPointer`-Struktur, deren einzige benutzerdefinierte Funktionalität darin besteht, dass sie `Dropping CustomSmartPointer!` ausgibt, wenn die Instanz außer Gültigkeitsbereich gelangt, um zu zeigen, wann Rust die `drop`-Methode ausführt.

Dateiname: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14: Eine `CustomSmartPointer`-Struktur, die das `Drop`-Trait implementiert, wo wir unseren Bereinigungs-Code ablegen würden

Das `Drop`-Trait ist im Präludium enthalten, so dass wir es nicht in den Geltungsbereich bringen müssen. Wir implementieren das `Drop`-Trait für `CustomSmartPointer` \[1\] und geben eine Implementierung für die `drop`-Methode an, die `println!` aufruft \[2\]. Der Körper der `drop`-Methode ist der Ort, an dem Sie alle Logik ablegen können, die Sie ausführen möchten, wenn eine Instanz Ihres Typs außer Gültigkeitsbereich gelangt. Wir drucken hier einige Text aus, um visuell zu demonstrieren, wann Rust `drop` aufrufen wird.

In `main` erstellen wir zwei Instanzen von `CustomSmartPointer` bei \[3\] und \[4\] und geben dann `CustomSmartPointers created` aus \[5\]. Am Ende von `main` \[6\] gehen unsere `CustomSmartPointer`-Instanzen außer Gültigkeitsbereich, und Rust ruft den Code auf, den wir in die `drop`-Methode \[2\] geschrieben haben, und gibt unsere Endmeldung aus. Beachten Sie, dass wir die `drop`-Methode nicht explizit aufrufen mussten.

Wenn wir dieses Programm ausführen, sehen wir die folgende Ausgabe:

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

Rust hat automatisch `drop` für uns aufgerufen, als unsere Instanzen außer Gültigkeitsbereich gingen, und hat den von uns angegebenen Code aufgerufen. Variablen werden in umgekehrter Reihenfolge ihrer Erstellung gelöscht, sodass `d` vor `c` gelöscht wurde. Der Zweck dieses Beispiels ist es, Ihnen einen visuellen Leitfaden darüber zu geben, wie die `drop`-Methode funktioniert; normalerweise würden Sie den Bereinigungs-Code angeben, den Ihr Typ ausführen muss, anstatt eine Print-Nachricht.

Leider ist es nicht einfach, die automatische `drop`-Funktionalität zu deaktivieren. Das Deaktivieren von `drop` ist normalerweise nicht erforderlich; der ganze Sinn des `Drop`-Traits besteht darin, dass es automatisch übernommen wird. Gelegentlich möchten Sie jedoch einen Wert früher bereinigen. Ein Beispiel ist die Verwendung von Smart-Pointern, die Locks verwalten: Sie möchten möglicherweise die `drop`-Methode, die den Lock freigibt, erzwingen, sodass anderer Code im selben Gültigkeitsbereich den Lock erwerben kann. Rust lässt Ihnen die `drop`-Methode des `Drop`-Traits nicht manuell aufrufen; stattdessen müssen Sie die von der Standardbibliothek bereitgestellte `std::mem::drop`-Funktion aufrufen, wenn Sie einen Wert vor dem Ende seines Gültigkeitsbereichs zwingen möchten, gelöscht zu werden.

Wenn wir versuchen, die `drop`-Methode des `Drop`-Traits manuell aufzurufen, indem wir die `main`-Funktion aus Listing 15-14 ändern, wie in Listing 15-15 gezeigt, erhalten wir einen Compilerfehler.

Dateiname: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15: Versuch, die `drop`-Methode aus dem `Drop`-Trait manuell aufzurufen, um frühzeitig aufzuräumen

Wenn wir diesen Code versuchen, zu kompilieren, erhalten wir diesen Fehler:

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

Diese Fehlermeldung besagt, dass wir die `drop`-Methode nicht explizit aufrufen dürfen. Die Fehlermeldung verwendet den Begriff _Destruktor_, der der allgemeine Programmierbegriff für eine Funktion ist, die eine Instanz bereinigt. Ein _Destruktor_ ist analog zu einem _Konstruktor_, der eine Instanz erstellt. Die `drop`-Funktion in Rust ist ein bestimmter Destruktor.

Rust lässt uns die `drop`-Methode nicht explizit aufrufen, weil Rust an der Endet von `main` immer noch automatisch `drop` auf dem Wert aufrufen würde. Dies würde einen _Doppelfreigabe_ -Fehler verursachen, da Rust versuchen würde, den gleichen Wert zweimal zu bereinigen.

Wir können die automatische Einfügung von `drop` nicht deaktivieren, wenn ein Wert außer Gültigkeitsbereich gelangt, und wir können die `drop`-Methode nicht explizit aufrufen. Wenn wir daher einen Wert frühzeitig bereinigen müssen, verwenden wir die `std::mem::drop`-Funktion.

Die `std::mem::drop`-Funktion unterscheidet sich von der `drop`-Methode im `Drop`-Trait. Wir rufen sie auf, indem wir als Argument den Wert übergeben, den wir zwingen möchten, gelöscht zu werden. Die Funktion ist im Präludium enthalten, so dass wir `main` in Listing 15-15 ändern können, um die `drop`-Funktion aufzurufen, wie in Listing 15-16 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16: Aufrufen von `std::mem::drop`, um einen Wert explizit vor dem Verlassen seines Gültigkeitsbereichs zu löschen

Wenn wir diesen Code ausführen, wird die folgende Ausgabe gedruckt:

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

Der Text `Dropping CustomSmartPointer with data`some data`!` wird zwischen dem Text `CustomSmartPointer created.` und `CustomSmartPointer dropped before the end of main.` gedruckt, was zeigt, dass der `drop`-Methoden-Code aufgerufen wird, um `c` an diesem Punkt zu löschen.

Sie können den in einer `Drop`-Trait-Implementierung angegebenen Code auf viele Weise verwenden, um die Bereinigung bequem und sicher zu machen: Beispielsweise könnten Sie ihn verwenden, um Ihren eigenen Speicherzuweisungs-Allocator zu erstellen! Mit dem `Drop`-Trait und dem Besitzsystem von Rust müssen Sie sich nicht darum kümmern, zu bereinigen, weil Rust es automatisch macht.

Sie müssen sich auch nicht um Probleme sorgen, die aus Versehen beim Bereinigen von noch verwendeten Werten resultieren: Das Besitzsystem, das sicherstellt, dass Referenzen immer gültig sind, gewährleistet auch, dass `drop` nur einmal aufgerufen wird, wenn der Wert nicht mehr verwendet wird.

Jetzt, nachdem wir uns `Box<T>` und einige Eigenschaften von Smart-Pointern angeschaut haben, betrachten wir einige andere in der Standardbibliothek definierten Smart-Pointer.
