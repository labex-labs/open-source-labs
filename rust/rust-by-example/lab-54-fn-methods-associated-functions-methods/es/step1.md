# Funciones asociadas y Métodos

Algunas funciones están conectadas a un tipo particular. Estas vienen en dos formas: funciones asociadas y métodos. Las funciones asociadas son funciones que se definen en un tipo generalmente, mientras que los métodos son funciones asociadas que se llaman en una instancia particular de un tipo.

```rust
struct Point {
    x: f64,
    y: f64,
}

// Bloque de implementación, todas las funciones y métodos asociados a `Point` van aquí
impl Point {
    // Esta es una "función asociada" porque esta función está asociada con
    // un tipo particular, es decir, Point.
    //
    // Las funciones asociadas no necesitan ser llamadas con una instancia.
    // Estas funciones generalmente se usan como constructores.
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    // Otra función asociada, que toma dos argumentos:
    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y }
    }
}

struct Rectangle {
    p1: Point,
    p2: Point,
}

impl Rectangle {
    // Este es un método
    // `&self` es un atajo para `self: &Self`, donde `Self` es el tipo del
    // objeto llamante. En este caso `Self` = `Rectangle`
    fn area(&self) -> f64 {
        // `self` permite acceder a los campos del struct a través del operador punto
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        // `abs` es un método de `f64` que devuelve el valor absoluto del
        // llamante
        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    // Este método requiere que el objeto llamante sea mutable
    // `&mut self` se desugara a `self: &mut Self`
    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;

        self.p1.y += y;
        self.p2.y += y;
    }
}

// `Pair` posee recursos: dos enteros asignados en el heap
struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // Este método "consume" los recursos del objeto llamante
    // `self` se desugara a `self: Self`
    fn destroy(self) {
        // Desestructura `self`
        let Pair(first, second) = self;

        println!("Destroying Pair({}, {})", first, second);

        // `first` y `second` salen del ámbito y se liberan
    }
}

fn main() {
    let rectangle = Rectangle {
        // Las funciones asociadas se llaman usando dos puntos
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // Los métodos se llaman usando el operador punto
    // Tenga en cuenta que el primer argumento `&self` se pasa implícitamente, es decir,
    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // Error! `rectangle` es inmutable, pero este método requiere un objeto mutable
    //rectangle.translate(1.0, 0.0);
    // TODO ^ Intente descomentar esta línea

    // Okay! Los objetos mutables pueden llamar a métodos mutables
    square.translate(1.0, 1.0);

    let pair = Pair(Box::new(1), Box::new(2));

    pair.destroy();

    // Error! La llamada anterior a `destroy` "consumió" `pair`
    //pair.destroy();
    // TODO ^ Intente descomentar esta línea
}
```
