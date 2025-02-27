# Desambiguación de rasgos superpuestos

Un tipo puede implementar muchos diferentes rasgos. ¿Qué pasa si dos rasgos requieren el mismo nombre? Por ejemplo, muchos rasgos pueden tener un método llamado `get()`. ¡Incluso pueden tener diferentes tipos de retorno!

Buena noticia: debido a que cada implementación de rasgo tiene su propio bloque `impl`, queda claro qué método `get` de qué rasgo estás implementando.

¿Qué pasa cuando llega el momento de _llamar_ a esos métodos? Para desambiguar entre ellos, tenemos que usar la Sintaxis Cualificada Completa.

```rust
trait UsernameWidget {
    // Obtener el nombre de usuario seleccionado de este widget
    fn get(&self) -> String;
}

trait AgeWidget {
    // Obtener la edad seleccionada de este widget
    fn get(&self) -> u8;
}

// Un formulario con tanto un UsernameWidget como un AgeWidget
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // Si descomentas esta línea, obtendrás un error que dice
    // "se encontraron múltiples `get`". Porque, después de todo, hay múltiples métodos
    // llamados `get`.
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
