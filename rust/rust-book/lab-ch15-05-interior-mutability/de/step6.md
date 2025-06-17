# Erlauben von mehreren Besitzern von veränderbaren Daten mit Rc`<T>` und RefCell`<T>`

Eine häufige Weise, `RefCell<T>` zu verwenden, ist in Kombination mit `Rc<T>`. Erinnern Sie sich, dass `Rc<T>` Ihnen ermöglicht, mehrere Besitzer eines bestimmten Datensatzes zu haben, aber es gibt nur unveränderlichen Zugang zu diesem Datensatz. Wenn Sie ein `Rc<T>` haben, das ein `RefCell<T>` enthält, können Sie einen Wert erhalten, der mehrere Besitzer haben _und_ den Sie mutieren können!

Zum Beispiel erinnern Sie sich an das Beispiel der Kons-Liste in Listing 15-18, in dem wir `Rc<T>` verwendet haben, um mehreren Listen die Möglichkeit zu geben, die Eigentumsverhältnisse einer anderen Liste zu teilen. Da `Rc<T>` nur unveränderliche Werte hält, können wir keine der Werte in der Liste ändern, nachdem wir sie erstellt haben. Fügen wir `RefCell<T>` hinzu, um seine Fähigkeit, die Werte in den Listen zu ändern. Listing 15-24 zeigt, dass wir, indem wir ein `RefCell<T>` in der `Cons`-Definition verwenden, den gespeicherten Wert in allen Listen ändern können.

Dateiname: `src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

Listing 15-24: Verwenden von `Rc<RefCell<i32>>` zum Erstellen einer `List`, die wir mutieren können

Wir erstellen einen Wert, der eine Instanz von `Rc<RefCell<i32>>` ist, und speichern ihn in einer Variable namens `value` \[1\], damit wir ihn später direkt zugreifen können. Dann erstellen wir eine `List` in `a` mit einer `Cons`-Variante, die `value` enthält \[2\]. Wir müssen `value` klonen, damit sowohl `a` als auch `value` die Eigentumsverhältnisse des inneren `5`-Werts haben, anstatt die Eigentumsverhältnisse von `value` an `a` zu übertragen oder `a` von `value` zu entleihen.

Wir umschließen die Liste `a` in einem `Rc<T>`, sodass wir, wenn wir Listen `b` und `c` erstellen, beide auf `a` verweisen können, wie wir es in Listing 15-18 getan haben.

Nachdem wir die Listen in `a`, `b` und `c` erstellt haben, möchten wir dem Wert in `value` 10 hinzufügen \[3\]. Wir tun dies, indem wir `borrow_mut` auf `value` aufrufen, was die automatische Dereferenzierungsmöglichkeit verwendet, die wir in "Wo ist der -\> Operator?" diskutiert haben, um die `Rc<T>` auf den inneren `RefCell<T>`-Wert umzudeuten. Die `borrow_mut`-Methode gibt einen Smart-Pointer vom Typ `RefMut<T>` zurück, und wir verwenden den Dereferenzierungsoperator darauf und ändern den inneren Wert.

Wenn wir `a`, `b` und `c` ausgeben, können wir sehen, dass alle den modifizierten Wert von `15` anstelle von `5` haben:

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

Diese Technik ist ziemlich praktisch! Indem wir `RefCell<T>` verwenden, haben wir einen äußerlich unveränderlichen `List`-Wert. Aber wir können die Methoden auf `RefCell<T>` verwenden, die den Zugang zu seiner internen Veränderbarkeit ermöglichen, sodass wir unsere Daten ändern können, wenn wir dies benötigen. Die Laufzeitprüfungen der Leihregeln schützen uns vor Datenkonflikten, und es lohnt sich manchmal, etwas an Geschwindigkeit für diese Flexibilität in unseren Datenstrukturen zu opfern. Beachten Sie, dass `RefCell<T>` für mehrthreadigen Code nicht funktioniert! `Mutex<T>` ist die threadsichere Version von `RefCell<T>`, und wir werden `Mutex<T>` im Kapitel 16 diskutieren.
