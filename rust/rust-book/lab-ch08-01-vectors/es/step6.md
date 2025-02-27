# Usar un enum para almacenar múltiples tipos

Los vectores solo pueden almacenar valores del mismo tipo. Esto puede resultar inconveniente; definitivamente hay casos de uso en los que es necesario almacenar una lista de elementos de diferentes tipos. Afortunadamente, las variantes de un enum se definen bajo el mismo tipo de enum, por lo que cuando necesitamos que un tipo represente elementos de diferentes tipos, ¡podemos definir y usar un enum!

Por ejemplo, digamos que queremos obtener valores de una fila en una hoja de cálculo en la que algunas de las columnas de la fila contienen enteros, algunos números de punto flotante y algunas cadenas. Podemos definir un enum cuyas variantes contendrán los diferentes tipos de valores, y todas las variantes del enum se considerarán del mismo tipo: el del enum. Luego podemos crear un vector para almacenar ese enum y, en última instancia, almacenar diferentes tipos. Lo hemos demostrado en la Lista 8-9.

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

Lista 8-9: Definir un `enum` para almacenar valores de diferentes tipos en un solo vector

Rust necesita saber qué tipos estarán en el vector en tiempo de compilación para saber exactamente cuánta memoria en el montón se necesitará para almacenar cada elemento. También debemos ser explícitos sobre qué tipos están permitidos en este vector. Si Rust permitiera que un vector almacenara cualquier tipo, habría una posibilidad de que uno o más de los tipos causaran errores con las operaciones realizadas en los elementos del vector. Usar un enum más una expresión `match` significa que Rust asegurará en tiempo de compilación que se maneje cada caso posible, como se discutió en el Capítulo 6.

Si no conoces el conjunto exhaustivo de tipos que un programa recibirá en tiempo de ejecución para almacenar en un vector, la técnica del enum no funcionará. En su lugar, puedes usar un objeto de tramo (trait object), que cubriremos en el Capítulo 17.

Ahora que hemos discutido algunas de las maneras más comunes de usar vectores, asegúrate de revisar la documentación de la API de todos los muchos métodos útiles definidos en `Vec<T>` por la biblioteca estándar. Por ejemplo, además de `push`, el método `pop` elimina y devuelve el último elemento.
