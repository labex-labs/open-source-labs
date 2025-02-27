# Standardgenerische Typparameter und Operatorüberladung

Wenn wir generische Typparameter verwenden, können wir einen Standardkonkreten Typ für den generischen Typ angeben. Dies eliminiert die Notwendigkeit für die Implementierer eines Traits, einen konkreten Typ anzugeben, wenn der Standardtyp funktioniert. Sie geben einen Standardtyp an, wenn Sie einen generischen Typ mit der `<`PlatzhalterTyp`=`KonkreterTyp`>`-Syntax deklarieren.

Ein großartiges Beispiel für eine Situation, in der diese Technik nützlich ist, ist die _Operatorüberladung_, bei der Sie das Verhalten eines Operators (wie `+`) in bestimmten Situationen anpassen.

Rust erlaubt es Ihnen nicht, eigene Operatoren zu erstellen oder beliebige Operatoren zu überladen. Sie können jedoch die Operationen und die zugehörigen Traits in `std::ops` überladen, indem Sie die mit dem Operator assoziierten Traits implementieren. Beispielsweise überladen wir in Listing 19-14 den `+`-Operator, um zwei `Point`-Instanzen zusammenzuzählen. Wir tun dies, indem wir den `Add`-Trait auf einer `Point`-Struktur implementieren.

Dateiname: `src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Listing 19-14: Implementieren des `Add`-Traits, um den `+`-Operator für `Point`-Instanzen zu überladen

Die `add`-Methode addiert die `x`-Werte von zwei `Point`-Instanzen und die `y`-Werte von zwei `Point`-Instanzen, um eine neue `Point` zu erstellen. Der `Add`-Trait hat einen assoziierten Typ namens `Output`, der den Typ bestimmt, der von der `add`-Methode zurückgegeben wird.

Der Standardgenerische Typ in diesem Code befindet sich innerhalb des `Add`-Traits. Hier ist seine Definition:

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

Dieser Code sollte generell vertraut sein: ein Trait mit einer Methode und einem assoziierten Typ. Der neue Teil ist `Rhs=Self`: Diese Syntax wird als _Standardtypparameter_ bezeichnet. Der generische Typparameter `Rhs` (Abkürzung für "right-hand side") definiert den Typ des `rhs`-Parameters in der `add`-Methode. Wenn wir keinen konkreten Typ für `Rhs` angeben, wenn wir den `Add`-Trait implementieren, wird der Typ von `Rhs` standardmäßig auf `Self` gesetzt, was der Typ sein wird, für den wir `Add` implementieren.

Als wir `Add` für `Point` implementiert haben, haben wir den Standardwert für `Rhs` verwendet, weil wir zwei `Point`-Instanzen addieren wollten. Schauen wir uns ein Beispiel an, bei dem wir den `Add`-Trait implementieren, bei dem wir den `Rhs`-Typ anpassen möchten, anstatt den Standardwert zu verwenden.

Wir haben zwei Structs, `Millimeters` und `Meters`, die Werte in unterschiedlichen Einheiten speichern. Diese dünne Umhüllung eines vorhandenen Typs in einem anderen Struct wird als _Newtype-Pattern_ bezeichnet, das wir im Abschnitt "Verwendung des Newtype-Patterns, um externe Traits auf externe Typen zu implementieren" im Detail beschreiben. Wir möchten die Werte in Millimetern zu den Werten in Metern addieren und die Implementierung von `Add` so konfigurieren, dass die Umrechnung korrekt durchgeführt wird. Wir können `Add` für `Millimeters` mit `Meters` als `Rhs` implementieren, wie in Listing 19-15 gezeigt.

Dateiname: `src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

Listing 19-15: Implementieren des `Add`-Traits auf `Millimeters`, um `Millimeters` und `Meters` zu addieren

Um `Millimeters` und `Meters` zu addieren, geben wir `impl Add<Meters>` an, um den Wert des `Rhs`-Typparameters festzulegen, anstatt den Standardwert von `Self` zu verwenden.

Sie werden Standardtypparameter auf zwei Hauptweisen verwenden:

1.  Um einen Typ zu erweitern, ohne vorhandenen Code zu brechen
2.  Um in bestimmten Fällen eine Anpassung zu ermöglichen, die die meisten Benutzer nicht benötigen werden

Der `Add`-Trait der Standardbibliothek ist ein Beispiel für den zweiten Zweck: Normalerweise werden Sie zwei ähnliche Typen addieren, aber der `Add`-Trait bietet die Möglichkeit, darüber hinaus anzupassen. Die Verwendung eines Standardtypparameters in der `Add`-Trait-Definition bedeutet, dass Sie die zusätzliche Parameter in der Regel nicht angeben müssen. Mit anderen Worten, ein bisschen Implementierungsaufwand ist nicht erforderlich, was es einfacher macht, den Trait zu verwenden.

Der erste Zweck ist ähnlich wie der zweite, nur umgekehrt: Wenn Sie einem bestehenden Trait einen Typparameter hinzufügen möchten, können Sie ihm einen Standardwert geben, um die Funktionalität des Traits zu erweitern, ohne den vorhandenen Implementierungscode zu brechen.
