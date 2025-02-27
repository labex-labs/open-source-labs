# Closure-Typenschlussfolgerung und -Annotation

Es gibt weitere Unterschiede zwischen Funktionen und Closures. Closures erfordern normalerweise nicht, dass Sie die Typen der Parameter oder des Rückgabewerts wie `fn`-Funktionen annotieren. Typenannotationen sind bei Funktionen erforderlich, weil die Typen Teil einer expliziten Schnittstelle sind, die Ihren Benutzern präsentiert wird. Die strikte Definition dieser Schnittstelle ist wichtig, um sicherzustellen, dass alle übereinstimmen, welche Typen von Werten eine Funktion verwendet und zurückgibt. Closures hingegen werden nicht in einer so offenen Schnittstelle verwendet: Sie werden in Variablen gespeichert und ohne Namensgebung und Offenlegung an die Benutzer unserer Bibliothek verwendet.

Closures sind typischerweise kurz und nur innerhalb eines engen Kontexts relevant, nicht in beliebigen Szenarien. Innerhalb dieser begrenzten Zusammenhänge kann der Compiler die Typen der Parameter und den Rückgabetyp ableiten, ähnlich wie er es für die meisten Variablen kann (es gibt seltene Fälle, in denen der Compiler auch Closure-Typenannotationen benötigt).

Wie bei Variablen können wir Typenannotationen hinzufügen, wenn wir die Exaktheit und Klarheit erhöhen möchten, allerdings auf Kosten einer höheren Wortlautlänge als strikt erforderlich. Die Typenannotation für einen Closure würde wie in Listing 13-2 aussehen. In diesem Beispiel definieren wir einen Closure und speichern es in einer Variable, anstatt wie in Listing 13-1 den Closure direkt an der Stelle zu definieren, wo wir ihn als Argument übergeben.

Dateiname: `src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Listing 13-2: Hinzufügen von optionalen Typenannotationen für die Parameter- und Rückgabetypen im Closure

Mit den hinzugefügten Typenannotationen sieht die Syntax von Closures ähnlicher wie die von Funktionen aus. Hier definieren wir eine Funktion, die 1 zu ihrem Parameter addiert, und einen Closure mit dem gleichen Verhalten, zum Vergleich. Wir haben einige Leerzeichen hinzugefügt, um die relevanten Teile zu aligngen. Dies veranschaulicht, wie die Closure-Syntax ähnlich wie die Funktions-Syntax ist, außer für die Verwendung von Rohren und die Menge an optionaler Syntax:

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

Die erste Zeile zeigt eine Funktionsdefinition und die zweite Zeile zeigt eine vollständige annotierte Closure-Definition. In der dritten Zeile entfernen wir die Typenannotationen aus der Closure-Definition. In der vierten Zeile entfernen wir die geschweiften Klammern, die optional sind, weil der Closure-Körper nur einen Ausdruck hat. Dies sind alle gültige Definitionen, die das gleiche Verhalten haben, wenn sie aufgerufen werden. Die Zeilen `add_one_v3` und `add_one_v4` erfordern die Auswertung der Closures, um zu kompilieren, weil die Typen aus ihrer Verwendung abgeleitet werden müssen. Dies ist ähnlich wie `let v = Vec::new();`, das entweder Typenannotationen oder Werte eines bestimmten Typs benötigt, um in den `Vec` eingefügt zu werden, damit Rust den Typ ableiten kann.

Für Closure-Definitionen wird der Compiler für jeden ihrer Parameter und für ihren Rückgabetyp einen konkreten Typ ableiten. Beispielsweise zeigt Listing 13-3 die Definition eines kurzen Closures, das einfach den Wert zurückgibt, den es als Parameter erhält. Dieser Closure ist außerhalb dieses Beispiels nicht sehr nützlich. Beachten Sie, dass wir keine Typenannotationen zur Definition hinzugefügt haben. Da es keine Typenannotationen gibt, können wir den Closure mit jedem Typ aufrufen, was wir hier zum ersten Mal mit `String` getan haben. Wenn wir dann versuchen, `example_closure` mit einem Integer aufzurufen, erhalten wir einen Fehler.

Dateiname: `src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Listing 13-3: Versuch, einen Closure aufzurufen, dessen Typen aus zwei verschiedenen Typen abgeleitet werden

Der Compiler gibt uns diesen Fehler:

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

Als erstes Mal rufen wir `example_closure` mit dem `String`-Wert auf. Der Compiler leitet dann den Typ von `x` und den Rückgabetyp des Closures als `String` ab. Diese Typen werden dann im Closure in `example_closure festgelegt, und wir erhalten einen Typfehler, wenn wir dann versuchen, einen anderen Typ mit demselben Closure zu verwenden.
