# Phantom-Typ-Parameter

Ein Phantom-Typ-Parameter ist ein Parameter, der zur Laufzeit nicht auftritt, sondern statisch (und nur) zur Compile-Zeit überprüft wird.

Datentypen können zusätzliche generische Typ-Parameter verwenden, um als Marker zu fungieren oder zur Typüberprüfung zur Compile-Zeit zu dienen. Diese zusätzlichen Parameter speichern keine Werte und haben keine Laufzeit-Behavior.

Im folgenden Beispiel kombinieren wir \[std::marker::PhantomData\] mit dem Phantom-Typ-Parameter-Konzept, um Tupel zu erstellen, die verschiedene Datentypen enthalten.

```rust
use std::marker::PhantomData;

// Ein Phantom-Tupel-Struct, das über `A` generisch ist mit verstecktem Parameter `B`.
#[derive(PartialEq)] // Erlaube Gleichheitstest für diesen Typ.
struct PhantomTuple<A, B>(A, PhantomData<B>);

// Ein Phantom-Typ-Struct, der über `A` generisch ist mit verstecktem Parameter `B`.
#[derive(PartialEq)] // Erlaube Gleichheitstest für diesen Typ.
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// Hinweis: Speicher wird für den generischen Typ `A` zugewiesen, aber nicht für `B`.
// Daher kann `B` nicht in Berechnungen verwendet werden.

fn main() {
    // Hier sind `f32` und `f64` die versteckten Parameter.
    // PhantomTuple-Typ angegeben als `<char, f32>`.
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // PhantomTuple-Typ angegeben als `<char, f64>`.
    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);

    // Typ angegeben als `<char, f32>`.
    let _struct1: PhantomStruct<char, f32> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };
    // Typ angegeben als `<char, f64>`.
    let _struct2: PhantomStruct<char, f64> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };

    // Compile-Zeitfehler! Typfehler, daher können diese nicht verglichen werden:
    // println!("_tuple1 == _tuple2 liefert: {}",
    //           _tuple1 == _tuple2);

    // Compile-Zeitfehler! Typfehler, daher können diese nicht verglichen werden:
    // println!("_struct1 == _struct2 liefert: {}",
    //           _struct1 == _struct2);
}
```
