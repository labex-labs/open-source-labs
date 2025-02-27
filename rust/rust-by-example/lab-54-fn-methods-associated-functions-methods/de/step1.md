# Assoziierte Funktionen und Methoden

Einige Funktionen sind mit einem bestimmten Typ verbunden. Diese kommen in zwei Formen: assoziierte Funktionen und Methoden. Assoziierte Funktionen sind Funktionen, die im Allgemeinen für einen Typ definiert sind, während Methoden assoziierte Funktionen sind, die auf einer bestimmten Instanz eines Typs aufgerufen werden.

```rust
struct Point {
    x: f64,
    y: f64,
}

// Implementierungsblock, alle assoziierten Funktionen und Methoden von `Point` gehen hier rein
impl Point {
    // Dies ist eine "assoziierte Funktion", weil diese Funktion mit einem bestimmten Typ verbunden ist, nämlich `Point`.
    //
    // Assoziierte Funktionen müssen nicht mit einer Instanz aufgerufen werden.
    // Diese Funktionen werden im Allgemeinen wie Konstruktoren verwendet.
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    // Eine weitere assoziierte Funktion, die zwei Argumente annimmt:
    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y }
    }
}

struct Rectangle {
    p1: Point,
    p2: Point,
}

impl Rectangle {
    // Dies ist eine Methode
    // `&self` ist eine Abkürzung für `self: &Self`, wobei `Self` der Typ des aufrufenden Objekts ist. In diesem Fall ist `Self` = `Rectangle`
    fn area(&self) -> f64 {
        // `self` ermöglicht den Zugriff auf die Strukturfelder über den Punktoperator
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        // `abs` ist eine Methode von `f64`, die den absoluten Wert des aufrufenden Objekts zurückgibt
        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    // Diese Methode erfordert, dass das aufrufende Objekt veränderbar ist
    // `&mut self` wird zu `self: &mut Self` umgewandelt
    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;

        self.p1.y += y;
        self.p2.y += y;
    }
}

// `Pair` besitzt Ressourcen: zwei auf dem Heap zugewiesene Integer
struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // Diese Methode "verbraucht" die Ressourcen des aufrufenden Objekts
    // `self` wird zu `self: Self` umgewandelt
    fn destroy(self) {
        // Zerlege `self`
        let Pair(first, second) = self;

        println!("Destroying Pair({}, {})", first, second);

        // `first` und `second` verlassen den Geltungsbereich und werden freigegeben
    }
}

fn main() {
    let rectangle = Rectangle {
        // Assoziierte Funktionen werden mit Doppelpunkten aufgerufen
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // Methoden werden mit dem Punktoperator aufgerufen
    // Beachten Sie, dass das erste Argument `&self` implizit übergeben wird, d.h.
    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // Fehler! `rectangle` ist unveränderlich, aber diese Methode erfordert ein veränderbares Objekt
    //rectangle.translate(1.0, 0.0);
    // TODO ^ Versuchen Sie, diese Zeile zu dekommentieren

    // Okay! Veränderbare Objekte können veränderbare Methoden aufrufen
    square.translate(1.0, 1.0);

    let pair = Pair(Box::new(1), Box::new(2));

    pair.destroy();

    // Fehler! Der vorherige `destroy`-Aufruf hat `pair` "verbraucht"
    //pair.destroy();
    // TODO ^ Versuchen Sie, diese Zeile zu dekommentieren
}
```
