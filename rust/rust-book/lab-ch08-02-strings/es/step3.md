# Creando una nueva cadena

Muchas de las mismas operaciones disponibles con `Vec<T>` también están disponibles con `String` porque `String` se implementa en realidad como un envoltorio alrededor de un vector de bytes con algunas garantías, restricciones y capacidades adicionales. Un ejemplo de una función que funciona de la misma manera con `Vec<T>` y `String` es la función `new` para crear una instancia, como se muestra en la Lista 8-11.

```rust
let mut s = String::new();
```

Lista 8-11: Creando una nueva cadena vacía

Esta línea crea una nueva cadena vacía llamada `s`, en la que luego podemos cargar datos. A menudo, tendremos algunos datos iniciales con los que queremos comenzar la cadena. Para eso, usamos el método `to_string`, que está disponible en cualquier tipo que implemente el trato `Display`, como lo hacen las literales de cadena. La Lista 8-12 muestra dos ejemplos.

```rust
let data = "initial contents";

let s = data.to_string();

// el método también funciona directamente en una literal:
let s = "initial contents".to_string();
```

Lista 8-12: Usando el método `to_string` para crear una `String` a partir de una literal de cadena

Este código crea una cadena que contiene `initial contents`.

También podemos usar la función `String::from` para crear una `String` a partir de una literal de cadena. El código de la Lista 8-13 es equivalente al código de la Lista 8-12 que usa `to_string`.

```rust
let s = String::from("initial contents");
```

Lista 8-13: Usando la función `String::from` para crear una `String` a partir de una literal de cadena

Debido a que las cadenas se usan para muchas cosas, podemos usar muchas diferentes API genéricas para cadenas, lo que nos proporciona muchas opciones. Algunas de ellas pueden parecer redundantes, pero todas tienen su lugar. En este caso, `String::from` y `to_string` hacen lo mismo, por lo que elegir cualquiera de ellos es una cuestión de estilo y legibilidad.

Recuerda que las cadenas están codificadas en UTF-8, por lo que podemos incluir cualquier dato codificado correctamente en ellas, como se muestra en la Lista 8-14.

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Lista 8-14: Almacenando saludos en diferentes idiomas en cadenas

Todas estas son valores válidos de `String`.
