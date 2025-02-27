# Introducción

En este laboratorio, exploraremos el concepto de cadenas en Rust. Rust tiene dos tipos de cadenas: `String` y `&str`.

Una `String` es una cadena asignada en el montón y crecible que está garantizada para ser una secuencia UTF-8 válida. Por otro lado, `&str` es una porción que apunta a una secuencia UTF-8 válida y se puede utilizar para ver dentro de una `String`.

En Rust, los literales de cadena se pueden escribir de diferentes maneras, incluyendo el uso de escapes para representar caracteres especiales. Por ejemplo, `\x3F` representa el carácter de interrogación y `\u{211D}` representa un punto de código Unicode. También se pueden utilizar literales de cadena sin procesar si se desea escribir una cadena tal cual sin escapes.

Si es necesario trabajar con cadenas de bytes, Rust proporciona literales de cadena de bytes utilizando el prefijo `b`. Las cadenas de bytes pueden tener escapes de bytes, pero no escapes Unicode. Las cadenas de bytes sin procesar también se pueden utilizar de manera similar a los literales de cadena sin procesar.

Es importante tener en cuenta que `str` y `String` deben siempre ser secuencias UTF-8 válidas. Si es necesario trabajar con cadenas en diferentes codificaciones, se pueden utilizar cajas externas como `encoding` para realizar conversiones entre codificaciones de caracteres.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
