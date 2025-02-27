# Encapsulación que oculta los detalles de implementación

Otro aspecto comúnmente asociado con la programación orientada a objetos es la idea de _encapsulación_, que significa que los detalles de implementación de un objeto no son accesibles para el código que utiliza ese objeto. Por lo tanto, la única manera de interactuar con un objeto es a través de su API pública; el código que utiliza el objeto no debería poder acceder a los internos del objeto y cambiar directamente los datos o el comportamiento. Esto permite al programador cambiar y refactorizar los internos de un objeto sin necesidad de cambiar el código que utiliza el objeto.

Discutimos cómo controlar la encapsulación en el Capítulo 7: podemos utilizar la palabra clave `pub` para decidir qué módulos, tipos, funciones y métodos en nuestro código deben ser públicos, y por defecto todo lo demás es privado. Por ejemplo, podemos definir un struct `AveragedCollection` que tiene un campo que contiene un vector de valores de `i32`. El struct también puede tener un campo que contiene el promedio de los valores en el vector, lo que significa que el promedio no tiene que ser calculado sobre demanda cada vez que alguien lo necesita. En otras palabras, `AveragedCollection` cacheará el promedio calculado para nosotros. La Lista 17-1 tiene la definición del struct `AveragedCollection`.

Nombre de archivo: `src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

Lista 17-1: Un struct `AveragedCollection` que mantiene una lista de enteros y el promedio de los elementos en la colección

El struct está marcado `pub` para que otro código pueda utilizarlo, pero los campos dentro del struct siguen siendo privados. Esto es importante en este caso porque queremos asegurarnos de que cada vez que se agrega o quita un valor de la lista, el promedio también se actualice. Hacemos esto implementando los métodos `add`, `remove` y `average` en el struct, como se muestra en la Lista 17-2.

Nombre de archivo: `src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

Lista 17-2: Implementaciones de los métodos públicos `add`, `remove` y `average` en `AveragedCollection`

Los métodos públicos `add`, `remove` y `average` son las únicas maneras de acceder o modificar los datos en una instancia de `AveragedCollection`. Cuando se agrega un elemento a `list` utilizando el método `add` o se quita utilizando el método `remove`, las implementaciones de cada una llaman al método privado `update_average` que se encarga de actualizar el campo `average` también.

Dejamos los campos `list` y `average` privados para que no haya manera para el código externo de agregar o quitar elementos al campo `list` directamente; de lo contrario, el campo `average` podría quedar desincronizado cuando `list` cambia. El método `average` devuelve el valor en el campo `average`, permitiendo que el código externo lea el `average` pero no lo modifique.

Debido a que hemos encapsulado los detalles de implementación del struct `AveragedCollection`, podemos cambiar fácilmente aspectos, como la estructura de datos, en el futuro. Por ejemplo, podríamos utilizar un `HashSet<i32>` en lugar de un `Vec<i32>` para el campo `list`. Siempre y cuando las firmas de los métodos públicos `add`, `remove` y `average` se mantuvieran iguales, el código que utiliza `AveragedCollection` no tendría que cambiar. Si hiciéramos `list` público en su lugar, esto no necesariamente sería el caso: `HashSet<i32>` y `Vec<i32>` tienen métodos diferentes para agregar y quitar elementos, por lo que el código externo probablemente tendría que cambiar si estuviera modificando `list` directamente.

Si la encapsulación es un aspecto requerido para que un lenguaje sea considerado orientado a objetos, entonces Rust cumple con ese requisito. La opción de utilizar `pub` o no para diferentes partes del código permite la encapsulación de los detalles de implementación.
