# Leer elementos de vectores

Hay dos maneras de referirse a un valor almacenado en un vector: a través de la indexación o mediante el uso del método `get`. En los siguientes ejemplos, hemos anotado los tipos de los valores que se devuelven de estas funciones para mayor claridad.

La Lista 8-4 muestra ambos métodos de acceder a un valor en un vector, con la sintaxis de indexación y el método `get`.

```rust
let v = vec![1, 2, 3, 4, 5];

1 let third: &i32 = &v[2];
println!("The third element is {third}");

2 let third: Option<&i32> = v.get(2);
match third  {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

Lista 8-4: Usar la sintaxis de indexación y el método `get` para acceder a un elemento en un vector

Tenga en cuenta algunos detalles aquí. Usamos el valor de índice de `2` para obtener el tercer elemento \[1\] porque los vectores se indexan por número, comenzando en cero. Usar `&` y `[]` nos da una referencia al elemento en el valor de índice. Cuando usamos el método `get` con el índice pasado como argumento \[2\], obtenemos un `Option<&T>` que podemos usar con `match`.

Rust proporciona estas dos maneras de referirse a un elemento para que puedas elegir cómo se comporta el programa cuando intentas usar un valor de índice fuera del rango de los elementos existentes. Como ejemplo, veamos qué pasa cuando tenemos un vector de cinco elementos y luego intentamos acceder a un elemento en el índice 100 con cada técnica, como se muestra en la Lista 8-5.

```rust
let v = vec![1, 2, 3, 4, 5];

let does_not_exist = &v[100];
let does_not_exist = v.get(100);
```

Lista 8-5: Intentar acceder al elemento en el índice 100 en un vector que contiene cinco elementos

Cuando ejecutamos este código, el primer método `[]` hará que el programa se detenga con un error porque hace referencia a un elemento que no existe. Este método es mejor usado cuando quieres que tu programa se detenga si hay un intento de acceder a un elemento más allá del final del vector.

Cuando se pasa un índice fuera del vector al método `get`, devuelve `None` sin detenerse con un error. Usarías este método si es posible que ocasionalmente se acceda a un elemento más allá del rango del vector en circunstancias normales. Tu código tendrá entonces la lógica para manejar tener ya sea `Some(&element)` o `None`, como se discutió en el Capítulo 6. Por ejemplo, el índice podría venir de una persona que ingresa un número. Si accidentalmente ingresan un número demasiado grande y el programa obtiene un valor `None`, podrías decirle al usuario cuántos elementos hay en el vector actual y darles otra oportunidad para ingresar un valor válido. Eso sería más amigable para el usuario que detener el programa debido a un error tipográfico.

Cuando el programa tiene una referencia válida, el verificador de préstamos (préstamo checker) fuerza las reglas de propiedad y préstamo (que se cubren en el Capítulo 4) para garantizar que esta referencia y cualquier otra referencia al contenido del vector sigan siendo válidas. Recuerda la regla que establece que no puedes tener referencias mutables e inmutables en el mismo ámbito. Esa regla se aplica en la Lista 8-6, donde mantenemos una referencia inmutable al primer elemento en un vector y tratamos de agregar un elemento al final. Este programa no funcionará si también intentamos referirnos a ese elemento más adelante en la función.

```rust
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);

println!("The first element is: {first}");
```

Lista 8-6: Intentar agregar un elemento a un vector mientras se tiene una referencia a un elemento

Compilar este código resultará en este error:

```bash
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:5
  |
4 |     let first = &v[0];
  |                  - immutable borrow occurs here
5 |
6 |     v.push(6);
  |     ^^^^^^^^^ mutable borrow occurs here
7 |
8 |     println!("The first element is: {first}");
  |                                      ----- immutable borrow later used here
```

El código en la Lista 8-6 puede parecer que debería funcionar: ¿por qué una referencia al primer elemento debería importarse por los cambios al final del vector? Este error se debe a la forma en que funcionan los vectores: dado que los vectores colocan los valores uno al lado del otro en la memoria, agregar un nuevo elemento al final del vector podría requerir asignar nueva memoria y copiar los elementos antiguos al nuevo espacio, si no hay suficiente espacio para poner todos los elementos uno al lado del otro donde se almacena actualmente el vector. En ese caso, la referencia al primer elemento estaría apuntando a memoria desasignada. Las reglas de préstamo evitan que los programas terminen en esa situación.

> Nota: Para obtener más detalles sobre la implementación del tipo `Vec<T>`, consulte "The Rustonomicon" en *https://doc.rust-lang.org/nomicon/vec/vec.html*.
