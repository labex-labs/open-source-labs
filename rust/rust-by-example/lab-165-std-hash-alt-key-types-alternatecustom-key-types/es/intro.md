# Introducción

En este laboratorio, exploramos el uso de tipos de claves alternativas/personalizadas en el `HashMap` de Rust, que pueden incluir tipos que implementen los tratos `Eq` y `Hash`, como `bool`, `int`, `uint`, `String` y `&str`. Además, podemos implementar estos tratos para tipos personalizados mediante el atributo `#[derive(PartialEq, Eq, Hash)]`, lo que les permite ser utilizados como claves en un `HashMap`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
