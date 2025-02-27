# Definiendo un Trato para el Comportamiento Común

Para implementar el comportamiento que queremos que tenga `gui`, definiremos un trato llamado `Draw` que tendrá un método llamado `draw`. Luego podemos definir un vector que toma un _objeto de trato_. Un objeto de trato apunta tanto a una instancia de un tipo que implementa nuestro trato especificado como a una tabla utilizada para buscar métodos de trato en ese tipo en tiempo de ejecución. Creamos un objeto de trato especificando algún tipo de puntero, como una referencia `&` o un puntero inteligente `Box<T>`, luego la palabra clave `dyn`, y luego especificando el trato relevante. (Hablaremos de la razón por la cual los objetos de trato deben usar un puntero en "Tipos de Tamaño Dinámico y el Trato Sized".) Podemos usar objetos de trato en lugar de un tipo genérico o concreto. Dondequiera que usemos un objeto de trato, el sistema de tipos de Rust asegurará en tiempo de compilación que cualquier valor utilizado en ese contexto implementará el trato del objeto de trato. En consecuencia, no necesitamos conocer todos los posibles tipos en tiempo de compilación.

Hemos mencionado que, en Rust, evitamos llamar a structs y enums "objetos" para distinguirlos de los objetos de otros lenguajes. En un struct o enum, los datos en los campos del struct y el comportamiento en los bloques `impl` están separados, mientras que en otros lenguajes, los datos y el comportamiento combinados en un solo concepto a menudo se etiquetan como objeto. Sin embargo, los objetos de trato _son_ más parecidos a los objetos en otros lenguajes en el sentido de que combinan datos y comportamiento. Pero los objetos de trato difieren de los objetos tradicionales en que no podemos agregar datos a un objeto de trato. Los objetos de trato no son tan útil en general como los objetos en otros lenguajes: su propósito específico es permitir la abstracción a través del comportamiento común.

La Lista 17-3 muestra cómo definir un trato llamado `Draw` con un método llamado `draw`.

Nombre de archivo: `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Lista 17-3: Definición del trato `Draw`

Esta sintaxis debería sonar familiar a partir de nuestras discusiones sobre cómo definir tratados en el Capítulo 10. A continuación viene una sintaxis nueva: la Lista 17-4 define un struct llamado `Screen` que contiene un vector llamado `components`. Este vector es del tipo `Box<dyn Draw>`, que es un objeto de trato; es un sustituto para cualquier tipo dentro de un `Box` que implemente el trato `Draw`.

Nombre de archivo: `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Lista 17-4: Definición del struct `Screen` con un campo `components` que contiene un vector de objetos de trato que implementan el trato `Draw`

En el struct `Screen`, definiremos un método llamado `run` que llamará al método `draw` en cada uno de sus `components`, como se muestra en la Lista 17-5.

Nombre de archivo: `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Lista 17-5: Un método `run` en `Screen` que llama al método `draw` en cada componente

Esto funciona de manera diferente a la definición de un struct que utiliza un parámetro de tipo genérico con límites de trato. Un parámetro de tipo genérico solo puede ser sustituido por un tipo concreto a la vez, mientras que los objetos de trato permiten que múltiples tipos concretos llenen el objeto de trato en tiempo de ejecución. Por ejemplo, podríamos haber definido el struct `Screen` utilizando un tipo genérico y un límite de trato, como en la Lista 17-6.

Nombre de archivo: `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Lista 17-6: Una implementación alternativa del struct `Screen` y su método `run` utilizando genéricos y límites de trato

Esto nos restringe a una instancia de `Screen` que tiene una lista de componentes todos del tipo `Button` o todos del tipo `TextField`. Si solo tendrás colecciones homogéneas, es preferible utilizar genéricos y límites de trato porque las definiciones se monomorfizarán en tiempo de compilación para utilizar los tipos concretos.

Por otro lado, con el método que utiliza objetos de trato, una instancia de `Screen` puede contener un `Vec<T>` que contiene un `Box<Button>` así como un `Box<TextField>`. Veamos cómo funciona esto, y luego hablaremos de las implicaciones de rendimiento en tiempo de ejecución.
