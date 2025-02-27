# Fonctions associées et méthodes

Certaines fonctions sont liées à un type particulier. Elles se présentent sous deux formes : les fonctions associées et les méthodes. Les fonctions associées sont des fonctions définies généralement sur un type, tandis que les méthodes sont des fonctions associées appelées sur une instance particulière d'un type.

```rust
struct Point {
    x: f64,
    y: f64,
}

// Bloc d'implémentation, toutes les fonctions et méthodes associées à `Point` y vont
impl Point {
    // Cette fonction est une "fonction associée" car elle est associée à
    // un type particulier, à savoir `Point`.
    //
    // Les fonctions associées ne doivent pas être appelées avec une instance.
    // Ces fonctions sont généralement utilisées comme des constructeurs.
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    // Une autre fonction associée, prenant deux arguments :
    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y }
    }
}

struct Rectangle {
    p1: Point,
    p2: Point,
}

impl Rectangle {
    // Cette fonction est une méthode
    // `&self` est un raccourci pour `self: &Self`, où `Self` est le type de l'objet appelant. Dans ce cas, `Self` = `Rectangle`
    fn area(&self) -> f64 {
        // `self` permet d'accéder aux champs de la structure via l'opérateur point
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        // `abs` est une méthode de `f64` qui renvoie la valeur absolue de l'appelant
        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    // Cette méthode nécessite que l'objet appelant soit mutable
    // `&mut self` se décompose en `self: &mut Self`
    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;

        self.p1.y += y;
        self.p2.y += y;
    }
}

// `Pair` possède des ressources : deux entiers alloués sur le tas
struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // Cette méthode "consomme" les ressources de l'objet appelant
    // `self` se décompose en `self: Self`
    fn destroy(self) {
        // Découpe `self`
        let Pair(first, second) = self;

        println!("Destroying Pair({}, {})", first, second);

        // `first` et `second` sortent de portée et sont libérés
    }
}

fn main() {
    let rectangle = Rectangle {
        // Les fonctions associées sont appelées en utilisant deux points
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // Les méthodes sont appelées en utilisant l'opérateur point
    // Notez que le premier argument `&self` est passé implicitement, c'est-à-dire que
    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // Erreur! `rectangle` est immuable, mais cette méthode nécessite un objet mutable
    //rectangle.translate(1.0, 0.0);
    // TODO ^ Essayez de décommenter cette ligne

    // Okay! Les objets mutables peuvent appeler les méthodes mutables
    square.translate(1.0, 1.0);

    let pair = Pair(Box::new(1), Box::new(2));

    pair.destroy();

    // Erreur! L'appel précédent à `destroy` a "consumé" `pair`
    //pair.destroy();
    // TODO ^ Essayez de décommenter cette ligne
}
```
