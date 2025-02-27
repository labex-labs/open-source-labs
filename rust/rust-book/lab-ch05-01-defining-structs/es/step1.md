# Definiendo e Instanciando Estructuras

Las estructuras son similares a las tuplas, discutidas en "El Tipo Tupla", en el sentido de que ambas almacenan múltiples valores relacionados. Al igual que las tuplas, las partes de una estructura pueden ser de diferentes tipos. A diferencia de las tuplas, en una estructura se le asignará un nombre a cada parte de datos para que quede claro qué significan los valores. Agregar estos nombres significa que las estructuras son más flexibles que las tuplas: no tienes que depender del orden de los datos para especificar o acceder a los valores de una instancia.

Para definir una estructura, ingresamos la palabra clave `struct` y nombramos toda la estructura. El nombre de una estructura debe describir la importancia de las piezas de datos que se agrupan. Luego, dentro de llaves, definimos los nombres y tipos de las piezas de datos, que llamamos _campos_. Por ejemplo, la Lista 5-1 muestra una estructura que almacena información sobre una cuenta de usuario.

Nombre del archivo: `src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

Lista 5-1: Definición de una estructura `User`

Para usar una estructura después de haberla definido, creamos una _instancia_ de esa estructura especificando valores concretos para cada uno de los campos. Creamos una instancia indicando el nombre de la estructura y luego agregamos llaves que contienen pares clave: valor, donde las claves son los nombres de los campos y los valores son los datos que queremos almacenar en esos campos. No tenemos que especificar los campos en el mismo orden en que los declaramos en la estructura. En otras palabras, la definición de la estructura es como una plantilla general para el tipo, y las instancias llenan esa plantilla con datos particulares para crear valores del tipo. Por ejemplo, podemos declarar un usuario en particular como se muestra en la Lista 5-2.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

Lista 5-2: Creación de una instancia de la estructura `User`

Para obtener un valor específico de una estructura, usamos la notación de punto. Por ejemplo, para acceder a la dirección de correo electrónico de este usuario, usamos `user1.email`. Si la instancia es mutable, podemos cambiar un valor usando la notación de punto y asignando a un campo particular. La Lista 5-3 muestra cómo cambiar el valor en el campo `email` de una instancia mutable de `User`.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

Lista 5-3: Cambiando el valor en el campo `email` de una instancia de `User`

Tenga en cuenta que toda la instancia debe ser mutable; Rust no nos permite marcar solo ciertos campos como mutables. Al igual que con cualquier expresión, podemos construir una nueva instancia de la estructura como la última expresión en el cuerpo de la función para devolver implícitamente esa nueva instancia.

La Lista 5-4 muestra una función `build_user` que devuelve una instancia de `User` con el correo electrónico y nombre de usuario dados. El campo `active` obtiene el valor de `true`, y el `sign_in_count` obtiene un valor de `1`.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

Lista 5-4: Una función `build_user` que toma un correo electrónico y nombre de usuario y devuelve una instancia de `User`

Tiene sentido nombrar los parámetros de la función con el mismo nombre que los campos de la estructura, pero tener que repetir los nombres de los campos `email` y `username` y las variables es un poco tedioso. Si la estructura tuviera más campos, repetir cada nombre sería aún más molesto. Por suerte, hay un atajo práctico.
