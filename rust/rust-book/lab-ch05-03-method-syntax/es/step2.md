# Definiendo Métodos

Vamos a cambiar la función `area` que tiene una instancia de `Rectangle` como parámetro y, en lugar de eso, crear un método `area` definido en el struct `Rectangle`, como se muestra en la Lista 5-13.

Nombre de archivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

1 impl Rectangle {
  2 fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
      3 rect1.area()
    );
}
```

Lista 5-13: Definiendo un método `area` en el struct `Rectangle`

Para definir la función dentro del contexto de `Rectangle`, comenzamos un bloque `impl` (implementación) para `Rectangle` \[1\]. Todo lo que esté dentro de este bloque `impl` estará asociado con el tipo `Rectangle`. Luego movemos la función `area` dentro de los corchetes `impl` \[2\] y cambiamos el primer (y en este caso, único) parámetro para que sea `self` en la firma y en todos los lugares dentro del cuerpo. En `main`, donde llamamos a la función `area` y pasamos `rect1` como argumento, en lugar de eso podemos usar la _sintaxis de método_ para llamar al método `area` en nuestra instancia de `Rectangle` \[3\]. La sintaxis de método va después de una instancia: agregamos un punto seguido del nombre del método, paréntesis y cualquier argumento.

En la firma de `area`, usamos `&self` en lugar de `rectangle: &Rectangle`. El `&self` es en realidad una abreviatura de `self: &Self`. Dentro de un bloque `impl`, el tipo `Self` es un alias para el tipo al que pertenece el bloque `impl`. Los métodos deben tener un parámetro llamado `self` del tipo `Self` como su primer parámetro, por lo que Rust te permite abreviarlo solo con el nombre `self` en el primer lugar del parámetro. Tenga en cuenta que todavía necesitamos usar el `&` delante de la abreviatura `self` para indicar que este método presta la instancia de `Self`, al igual que lo hicimos en `rectangle: &Rectangle`. Los métodos pueden tomar posesión de `self`, prestar `self` inmutablemente, como hicimos aquí, o prestar `self` mutablemente, al igual que pueden cualquier otro parámetro.

Elegimos `&self` aquí por la misma razón por la que usamos `&Rectangle` en la versión de función: no queremos tomar posesión y solo queremos leer los datos en el struct, no escribirlos. Si quisiéramos cambiar la instancia en la que se ha llamado al método como parte de lo que hace el método, usaríamos `&mut self` como primer parámetro. Tener un método que toma posesión de la instancia usando solo `self` como primer parámetro es poco común; esta técnica generalmente se utiliza cuando el método transforma `self` en algo más y se desea evitar que el llamador use la instancia original después de la transformación.

La principal razón para usar métodos en lugar de funciones, además de proporcionar la sintaxis de método y no tener que repetir el tipo de `self` en la firma de cada método, es por organización. Hemos puesto todas las cosas que podemos hacer con una instancia de un tipo en un bloque `impl` en lugar de hacer que los futuros usuarios de nuestro código busquen las capacidades de `Rectangle` en varios lugares de la biblioteca que proporcionamos.

Tenga en cuenta que podemos optar por dar a un método el mismo nombre que uno de los campos del struct. Por ejemplo, podemos definir un método en `Rectangle` que también se llame `width`:

Nombre de archivo: `src/main.rs`

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!(
            "The rectangle has a nonzero width; it is {}",
            rect1.width
        );
    }
}
```

Aquí, estamos eligiendo hacer que el método `width` devuelva `true` si el valor en el campo `width` de la instancia es mayor que `0` y `false` si el valor es `0`: podemos usar un campo dentro de un método con el mismo nombre para cualquier propósito. En `main`, cuando seguimos `rect1.width` con paréntesis, Rust sabe que nos referimos al método `width`. Cuando no usamos paréntesis, Rust sabe que nos referimos al campo `width`.

A menudo, pero no siempre, cuando damos a los métodos el mismo nombre que un campo, queremos que solo devuelva el valor en el campo y no haga nada más. Métodos como este se llaman _getters_, y Rust no los implementa automáticamente para los campos de struct como lo hacen algunos otros lenguajes. Los getters son útiles porque se puede hacer que el campo sea privado pero el método sea público, y así habilitar el acceso de solo lectura a ese campo como parte de la API pública del tipo. Discutiremos lo que es público y privado y cómo designar un campo o método como público o privado en el Capítulo 7.

> **¿Dónde está el operador -\>?**
>
> En C y C++, se usan dos operadores diferentes para llamar a métodos: se usa `.` si se está llamando a un método en el objeto directamente y `->` si se está llamando al método en un puntero al objeto y se necesita desreferenciar el puntero primero. En otras palabras, si `object` es un puntero, `object->`algo`()` es similar a `(*object).`algo`()`.
>
> Rust no tiene un equivalente al operador `->`; en cambio, Rust tiene una característica llamada _referenciación y desreferenciación automática_. Llamar a métodos es uno de los pocos lugares en Rust que tiene este comportamiento.
>
> Aquí está cómo funciona: cuando se llama a un método con `object.`algo`()`, Rust automáticamente agrega `&`, `&mut` o `*` para que `object` coincida con la firma del método. En otras palabras, lo siguiente es lo mismo:
>
>     p1.distance(&p2);
>     (&p1).distance(&p2);
>
> El primero se ve mucho más limpio. Este comportamiento de referenciación automática funciona porque los métodos tienen un receptor claro: el tipo de `self`. Dado el receptor y el nombre de un método, Rust puede determinar con certeza si el método está leyendo (`&self`), mutando (`&mut self`) o consumiendo (`self`). El hecho de que Rust haga la referencia implícita para los receptores de métodos es una gran parte de lo que hace que la posesión sea ergonomica en la práctica.
