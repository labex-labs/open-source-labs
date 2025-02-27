# Partielle Verschiebungen

Innerhalb der \[Destrukturierung\] einer einzelnen Variable können sowohl `by-move`- als auch `by-reference`-Musterbindungen gleichzeitig verwendet werden. Dadurch wird eine _partielle Verschiebung_ der Variable durchgeführt, was bedeutet, dass Teile der Variable verschoben werden, während andere Teile bleiben. In einem solchen Fall kann die übergeordnete Variable danach nicht mehr als Ganzes verwendet werden, jedoch können die Teile, die nur referenziert (und nicht verschoben) werden, weiterhin verwendet werden.

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` wird aus `person` herausverschoben, aber `age` wird referenziert
    let Person { name, ref age } = person;

    println!("The person's age is {}", age);

    println!("The person's name is {}", name);

    // Fehler! Zugriff auf teilweise verschobenen Wert: `person` partielle Verschiebung auftritt
    //println!("The person struct is {:?}", person);

    // `person` kann nicht verwendet werden, aber `person.age` kann verwendet werden, da es nicht verschoben wird
    println!("The person's age from person struct is {}", person.age);
}
```

(In diesem Beispiel speichern wir die Variable `age` auf dem Heap, um die partielle Verschiebung zu veranschaulichen: Wenn man `ref` im obigen Code löscht, tritt ein Fehler auf, da die Eigentumsgewalt von `person.age` an die Variable `age` übergeben würde. Wenn `Person.age` auf dem Stack gespeichert wäre, wäre `ref` nicht erforderlich, da die Definition von `age` die Daten von `person.age` kopieren würde, ohne sie zu verschieben.)
