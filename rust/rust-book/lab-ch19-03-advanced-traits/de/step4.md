# Die Klärung von Methoden mit demselben Namen

In Rust hindert nichts daran, dass ein Trait eine Methode mit demselben Namen wie eine Methode eines anderen Traits hat, und Rust verhindert auch nicht, dass Sie beide Traits auf einem Typ implementieren. Es ist auch möglich, eine Methode direkt auf dem Typ mit demselben Namen wie Methoden aus Traits zu implementieren.

Wenn Sie Methoden mit demselben Namen aufrufen, müssen Sie Rust mitteilen, welche Sie verwenden möchten. Betrachten Sie den Code in Listing 19-16, in dem wir zwei Traits, `Pilot` und `Wizard`, definiert haben, die beide eine Methode namens `fly` haben. Anschließend implementieren wir beide Traits auf einem Typ `Human`, auf dem bereits eine Methode namens `fly` implementiert ist. Jede `fly`-Methode macht etwas anderes.

Dateiname: `src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

Listing 19-16: Zwei Traits werden definiert, um eine `fly`-Methode zu haben, und werden auf dem `Human`-Typ implementiert, und eine `fly`-Methode wird direkt auf `Human` implementiert.

Wenn wir `fly` auf einer Instanz von `Human` aufrufen, wählt der Compiler standardmäßig die Methode aus, die direkt auf dem Typ implementiert ist, wie in Listing 19-17 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Listing 19-17: Aufrufen von `fly` auf einer Instanz von `Human`

Wenn Sie diesen Code ausführen, wird `*waving arms furiously*` gedruckt, was zeigt, dass Rust die direkt auf `Human` implementierte `fly`-Methode aufgerufen hat.

Um die `fly`-Methoden aus dem `Pilot`-Trait oder dem `Wizard`-Trait aufzurufen, müssen wir eine etwas explizitere Syntax verwenden, um anzugeben, welche `fly`-Methode wir meinen. Listing 19-18 demonstriert diese Syntax.

Dateiname: `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Listing 19-18: Angeben, welche `fly`-Methode eines Traits wir aufrufen möchten

Das Angabe des Traitnamens vor dem Methodennamen klärt für Rust auf, welche `fly`-Implementierung wir aufrufen möchten. Wir könnten auch `Human::fly(&person)` schreiben, was der in Listing 19-18 verwendeten `person.fly()` entspricht, aber dies ist etwas länger zu schreiben, wenn wir keine Klärung benötigen.

Wenn Sie diesen Code ausführen, wird folgendes gedruckt:

    This is your captain speaking.
    Up!
    *waving arms furiously*

Da die `fly`-Methode einen `self`-Parameter akzeptiert, könnte Rust, wenn wir zwei _Typen_ haben, die beide ein _Trait_ implementieren, herausfinden, welche Traitimplementierung basierend auf dem Typ von `self` zu verwenden ist.

Assoziierte Funktionen, die keine Methoden sind, haben jedoch keinen `self`-Parameter. Wenn es mehrere Typen oder Traits gibt, die nicht-methodische Funktionen mit demselben Funktionsnamen definieren, weiß Rust nicht immer, welchen Typ Sie meinen, es sei denn, Sie verwenden die vollqualifizierte Syntax. Beispielsweise erstellen wir in Listing 19-19 ein Trait für einen Tierheim, das alle Welpen Spot nennen möchte. Wir erstellen ein `Animal`-Trait mit einer assoziierten nicht-methodischen Funktion `baby_name`. Das `Animal`-Trait wird für die Struktur `Dog` implementiert, für die wir ebenfalls direkt eine assoziierte nicht-methodische Funktion `baby_name` bereitstellen.

Dateiname: `src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

Listing 19-19: Ein Trait mit einer assoziierten Funktion und ein Typ mit einer assoziierten Funktion gleichen Namens, der auch das Trait implementiert

Wir implementieren den Code für das Nennen aller Welpen Spot in der assoziierten Funktion `baby_name`, die auf `Dog` definiert ist. Der `Dog`-Typ implementiert auch das Trait `Animal`, das die Eigenschaften beschreibt, die alle Tiere haben. Welpen werden Welpen genannt, und das wird in der Implementierung des `Animal`-Traits auf `Dog` in der mit dem `Animal`-Trait assoziierten `baby_name`-Funktion ausgedrückt.

In `main` rufen wir die `Dog::baby_name`-Funktion auf, die direkt die auf `Dog` definierte assoziierte Funktion aufruft. Dieser Code druckt folgendes aus:

```rust
A baby dog is called a Spot
```

Dieser Ausgabewert ist nicht der, den wir wollten. Wir möchten die `baby_name`-Funktion aufrufen, die Teil des `Animal`-Traits ist, das wir auf `Dog` implementiert haben, so dass der Code `A baby dog is called a puppy` druckt. Die Technik, die wir in Listing 19-18 verwendeten, um den Traitnamen anzugeben, hilft hier nicht; wenn wir `main` in den Code in Listing 19-20 ändern, erhalten wir einen Kompilierungsfehler.

Dateiname: `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Listing 19-20: Versuch, die `baby_name`-Funktion aus dem `Animal`-Trait aufzurufen, aber Rust weiß nicht, welche Implementierung zu verwenden

Da `Animal::baby_name` keinen `self`-Parameter hat und es möglicherweise andere Typen gibt, die das `Animal`-Trait implementieren, kann Rust nicht herausfinden, welche Implementierung von `Animal::baby_name` wir möchten. Wir erhalten diesen Compilerfehler:

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

Um die Klärung zu treffen und Rust zu sagen, dass wir die Implementierung von `Animal` für `Dog` verwenden möchten, im Gegensatz zur Implementierung von `Animal` für einen anderen Typ, müssen wir die vollqualifizierte Syntax verwenden. Listing 19-21 demonstriert, wie die vollqualifizierte Syntax verwendet wird.

Dateiname: `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Listing 19-21: Verwendung der vollqualifizierten Syntax, um anzugeben, dass wir die `baby_name`-Funktion aus dem `Animal`-Trait als auf `Dog` implementiert aufrufen möchten

Wir geben Rust eine Typanmerkung innerhalb der spitzen Klammern, was angibt, dass wir die `baby_name`-Methode aus dem `Animal`-Trait als auf `Dog` implementiert aufrufen möchten, indem wir sagen, dass wir den `Dog`-Typ für diesen Funktionsaufruf als `Animal` behandeln möchten. Dieser Code wird jetzt das ausgeben, was wir wollen:

```rust
A baby dog is called a puppy
```

Im Allgemeinen ist die vollqualifizierte Syntax wie folgt definiert:

```rust
<Type as Trait>::function(receiver_if_method, next_arg,...);
```

Für assoziierte Funktionen, die keine Methoden sind, gäbe es keinen `receiver`: es gäbe nur die Liste der anderen Argumente. Sie könnten die vollqualifizierte Syntax überall verwenden, wo Sie Funktionen oder Methoden aufrufen. Allerdings sind Sie berechtigt, beliebigen Teil dieser Syntax zu weglassen, den Rust aus anderen Informationen im Programm herausfinden kann. Sie müssen nur diese umständlichere Syntax in Fällen verwenden, in denen es mehrere Implementierungen gibt, die den gleichen Namen verwenden und Rust Hilfe benötigt, um zu identifizieren, welche Implementierung Sie aufrufen möchten.
