# Escribir Comentarios de Documentación Útiles

Documentar con precisión tus paquetes ayudará a otros usuarios a saber cómo y cuándo utilizarlos, por lo que vale la pena invertir el tiempo en escribir documentación. En el Capítulo 3, discutimos cómo comentar el código de Rust utilizando dos barras, `//`. Rust también tiene un tipo particular de comentario para la documentación, conocido convenientemente como _comentario de documentación_, que generará documentación HTML. La documentación HTML muestra el contenido de los comentarios de documentación para los elementos de la API pública destinados a los programadores interesados en saber cómo _utilizar_ tu caja en lugar de cómo tu caja está _implementada_.

Los comentarios de documentación utilizan tres barras, `///`, en lugar de dos y admiten la notación Markdown para formatear el texto. Coloca los comentarios de documentación justo antes del elemento que estás documentando. La Lista 14-1 muestra comentarios de documentación para una función `add_one` en una caja llamada `my_crate`.

Nombre del archivo: `src/lib.rs`

````rust
/// Suma uno al número dado.
///
/// # Ejemplos
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
````

Lista 14-1: Un comentario de documentación para una función

Aquí, damos una descripción de lo que hace la función `add_one`, comenzamos una sección con el título `Ejemplos` y luego proporcionamos código que demuestra cómo utilizar la función `add_one`. Podemos generar la documentación HTML a partir de este comentario de documentación ejecutando `cargo doc`. Este comando ejecuta la herramienta `rustdoc` distribuida con Rust y coloca la documentación HTML generada en el directorio `target/doc`.

Para mayor comodidad, ejecutar `cargo doc --open` construirá el HTML para la documentación de tu caja actual (además de la documentación de todas las dependencias de tu caja) y abrirá el resultado en un navegador web. Navega hasta la función `add_one` y verás cómo se muestra el texto de los comentarios de documentación, como se muestra en la Figura 14-1.

Figura 14-1: Documentación HTML para la función `add_one`
