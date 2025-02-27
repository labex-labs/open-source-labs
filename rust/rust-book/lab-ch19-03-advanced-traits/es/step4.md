# Desambiguación entre Métodos con el Mismo Nombre

En Rust, nada impide que un trait tenga un método con el mismo nombre que un método de otro trait, ni tampoco impide que implementes ambos traits en un mismo tipo. También es posible implementar un método directamente en el tipo con el mismo nombre que los métodos de los traits.

Cuando llamas a métodos con el mismo nombre, necesitarás decirle a Rust cuál quieres usar. Considera el código de la Lista 19-16 donde hemos definido dos traits, `Pilot` y `Wizard`, que ambos tienen un método llamado `fly`. Luego implementamos ambos traits en un tipo `Human` que ya tiene un método llamado `fly` implementado en él. Cada método `fly` hace algo diferente.

Nombre de archivo: `src/main.rs`

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

Lista 19-16: Se definen dos traits para tener un método `fly` y se implementan en el tipo `Human`, y se implementa un método `fly` en `Human` directamente.

Cuando llamamos a `fly` en una instancia de `Human`, el compilador por defecto llama al método que está directamente implementado en el tipo, como se muestra en la Lista 19-17.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Lista 19-17: Llamando a `fly` en una instancia de `Human`

Ejecutando este código imprimirá `*waving arms furiously*`, lo que muestra que Rust llamó al método `fly` implementado directamente en `Human`.

Para llamar a los métodos `fly` del trait `Pilot` o del trait `Wizard`, necesitamos usar una sintaxis más explícita para especificar qué método `fly` queremos decir. La Lista 19-18 demuestra esta sintaxis.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Lista 19-18: Especificando qué método `fly` de qué trait queremos llamar

Especificar el nombre del trait antes del nombre del método aclara a Rust qué implementación de `fly` queremos llamar. También podríamos escribir `Human::fly(&person)`, lo que es equivalente a `person.fly()` que usamos en la Lista 19-18, pero esto es un poco más largo de escribir si no necesitamos desambiguar.

Ejecutando este código imprime lo siguiente:

    This is your captain speaking.
    Up!
    *waving arms furiously*

Debido a que el método `fly` toma un parámetro `self`, si tuviéramos dos _tipos_ que ambos implementan un _trait_, Rust podría determinar qué implementación de un trait usar basado en el tipo de `self`.

Sin embargo, las funciones asociadas que no son métodos no tienen un parámetro `self`. Cuando hay múltiples tipos o traits que definen funciones no métodos con el mismo nombre de función, Rust no siempre sabe qué tipo quieres decir a menos que uses la sintaxis completamente cualificada. Por ejemplo, en la Lista 19-19 creamos un trait para un refugio de animales que quiere llamar a todos los cachorros Spot. Creamos un trait `Animal` con una función asociada no método `baby_name`. El trait `Animal` se implementa para la struct `Dog`, en la que también proporcionamos una función asociada no método `baby_name` directamente.

Nombre de archivo: `src/main.rs`

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

Lista 19-19: Un trait con una función asociada y un tipo con una función asociada del mismo nombre que también implementa el trait

Implementamos el código para llamar a todos los cachorros Spot en la función asociada `baby_name` que está definida en `Dog`. El tipo `Dog` también implementa el trait `Animal`, que describe las características que todos los animales tienen. Los cachorros se llaman cachorros, y eso se expresa en la implementación del trait `Animal` en `Dog` en la función `baby_name` asociada al trait `Animal`.

En `main`, llamamos a la función `Dog::baby_name`, que llama directamente a la función asociada definida en `Dog`. Este código imprime lo siguiente:

```rust
A baby dog is called a Spot
```

Esta salida no es lo que queremos. Queremos llamar a la función `baby_name` que es parte del trait `Animal` que implementamos en `Dog` para que el código imprima `A baby dog is called a puppy`. La técnica de especificar el nombre del trait que usamos en la Lista 19-18 no ayuda aquí; si cambiamos `main` al código de la Lista 19-20, obtendremos un error de compilación.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Lista 19-20: Intentando llamar a la función `baby_name` del trait `Animal`, pero Rust no sabe qué implementación usar

Debido a que `Animal::baby_name` no tiene un parámetro `self`, y podría haber otros tipos que implementen el trait `Animal`, Rust no puede determinar qué implementación de `Animal::baby_name` queremos. Obtendremos este error del compilador:

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

Para desambiguar y decirle a Rust que queremos usar la implementación de `Animal` para `Dog` en lugar de la implementación de `Animal` para algún otro tipo, necesitamos usar la sintaxis completamente cualificada. La Lista 19-21 demuestra cómo usar la sintaxis completamente cualificada.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Lista 19-21: Usando la sintaxis completamente cualificada para especificar que queremos llamar a la función `baby_name` del trait `Animal` como implementado en `Dog`

Estamos proporcionando a Rust una anotación de tipo dentro de los corchetes angulares, lo que indica que queremos llamar al método `baby_name` del trait `Animal` como implementado en `Dog` al decir que queremos tratar el tipo `Dog` como un `Animal` para esta llamada de función. Este código ahora imprimirá lo que queremos:

```rust
A baby dog is called a puppy
```

En general, la sintaxis completamente cualificada se define como sigue:

```rust
<Type as Trait>::function(receiver_if_method, next_arg,...);
```

Para funciones asociadas que no son métodos, no habría un `receiver`: solo habría la lista de otros argumentos. Podrías usar la sintaxis completamente cualificada en todos los lugares donde llamas a funciones o métodos. Sin embargo, se te permite omitir cualquier parte de esta sintaxis que Rust pueda deducir de otras informaciones en el programa. Solo necesitas usar esta sintaxis más verbosa en casos donde hay múltiples implementaciones que usan el mismo nombre y Rust necesita ayuda para identificar qué implementación quieres llamar.
