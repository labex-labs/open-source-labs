# Implementieren des Traits

Jetzt werden wir einige Typen hinzufügen, die den `Draw`-Trait implementieren. Wir werden den `Button`-Typ bereitstellen. Wiederholen wir, dass die tatsächliche Implementierung einer GUI-Bibliothek außerhalb des Rahmens dieses Buches liegt, sodass die `draw`-Methode keinen nützlichen Implementierungsrumpf haben wird. Um uns vorzustellen, wie die Implementierung aussehen könnte, könnte eine `Button`-Struct Felder für `width`, `height` und `label` haben, wie in Listing 17-7 gezeigt.

Dateiname: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // code to actually draw a button
    }
}
```

Listing 17-7: Eine `Button`-Struct, die den `Draw`-Trait implementiert

Die Felder `width`, `height` und `label` auf `Button` werden sich von den Feldern auf anderen Komponenten unterscheiden; beispielsweise könnte ein `TextField`-Typ diese gleichen Felder plus ein `placeholder`-Feld haben. Jeder der Typen, die wir auf dem Bildschirm zeichnen möchten, wird den `Draw`-Trait implementieren, aber wird in der `draw`-Methode unterschiedlicher Code verwenden, um zu definieren, wie diesen bestimmten Typ zu zeichnen ist, wie dies hier bei `Button` der Fall ist (ohne den tatsächlichen GUI-Code, wie erwähnt). Der `Button`-Typ könnte beispielsweise einen zusätzlichen `impl`-Block enthalten, der Methoden enthält, die mit dem was passiert, wenn ein Benutzer auf die Schaltfläche klickt, zusammenhängen. Solche Methoden werden nicht auf Typen wie `TextField` anwendbar sein.

Wenn jemand, der unsere Bibliothek verwendet, eine `SelectBox`-Struct implementieren möchte, die Felder für `width`, `height` und `options` hat, würden sie auch den `Draw`-Trait auf dem `SelectBox`-Typ implementieren, wie in Listing 17-8 gezeigt.

Dateiname: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // code to actually draw a select box
    }
}
```

Listing 17-8: Ein weiterer Kasten, der `gui` verwendet und den `Draw`-Trait auf einer `SelectBox`-Struct implementiert

Der Benutzer unserer Bibliothek kann jetzt seine `main`-Funktion schreiben, um eine `Screen`-Instanz zu erstellen. Zu der `Screen`-Instanz können sie eine `SelectBox` und einen `Button` hinzufügen, indem sie jedes in eine `Box<T>` stecken, um ein Trait-Objekt zu werden. Sie können dann die `run`-Methode auf der `Screen`-Instanz aufrufen, was `draw` auf jeder der Komponenten aufrufen wird. Listing 17-9 zeigt diese Implementierung.

Dateiname: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Listing 17-9: Verwenden von Trait-Objekten, um Werte unterschiedlicher Typen zu speichern, die denselben Trait implementieren

Als wir die Bibliothek geschrieben haben, wussten wir nicht, dass jemand den `SelectBox`-Typ hinzufügen könnte, aber unsere `Screen`-Implementierung war in der Lage, auf dem neuen Typ zu operieren und ihn zu zeichnen, weil `SelectBox` den `Draw`-Trait implementiert, was bedeutet, dass es die `draw`-Methode implementiert.

Dieser Begriff - nur auf die Nachrichten zu achten, auf die ein Wert reagiert, anstatt auf den konkreten Typ des Werts - ähnelt dem Begriff des _Duck-Typings_ in dynamisch typisierten Sprachen: Wenn es wie eine Ente läuft und wie eine Ente quakt, dann muss es eine Ente sein! In der Implementierung von `run` auf `Screen` in Listing 17-5 muss `run` nicht wissen, was der konkrete Typ jeder Komponente ist. Es überprüft nicht, ob eine Komponente eine Instanz eines `Button` oder eines `SelectBox` ist, es ruft einfach die `draw`-Methode auf der Komponente auf. Indem wir `Box<dyn Draw>` als Typ der Werte im `components`-Vektor angeben, haben wir definiert, dass `Screen` Werte benötigt, auf denen wir die `draw`-Methode aufrufen können.

Der Vorteil der Verwendung von Trait-Objekten und des Rust-Typsystems, um Code zu schreiben, der ähnlich wie Code mit Duck-Typing ist, besteht darin, dass wir nie überprüfen müssen, ob ein Wert eine bestimmte Methode zur Laufzeit implementiert, oder uns Sorgen machen müssen, Fehler zu bekommen, wenn ein Wert eine Methode nicht implementiert, aber wir sie trotzdem aufrufen. Rust wird unseren Code nicht kompilieren, wenn die Werte die Traits nicht implementieren, die die Trait-Objekte benötigen.

Zum Beispiel zeigt Listing 17-10, was passiert, wenn wir versuchen, eine `Screen` mit einer `String` als Komponente zu erstellen.

Dateiname: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Listing 17-10: Versuch, einen Typ zu verwenden, der den Trait des Trait-Objekts nicht implementiert

Wir erhalten diesen Fehler, weil `String` den `Draw`-Trait nicht implementiert:

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

Dieser Fehler lässt uns wissen, dass wir entweder etwas an `Screen` übergeben, das wir nicht übergeben möchten und daher einen anderen Typ übergeben sollten, oder dass wir `Draw` auf `String` implementieren sollten, damit `Screen` in der Lage ist, `draw` auf ihm aufzurufen.
