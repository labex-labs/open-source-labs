# Introducción

En este laboratorio, aprendemos sobre `HashMap` en Rust, que se utiliza para almacenar valores por clave. Las claves de `HashMap` pueden ser de varios tipos, incluyendo booleanos, enteros, cadenas o cualquier otro tipo que implemente los rasgos `Eq` y `Hash`. Los `HashMaps` pueden crecer y contraerse dinámicamente en función del número de elementos. Podemos crear un `HashMap` con una capacidad específica utilizando `HashMap::with_capacity(uint)` o utilizar `HashMap::new()` para obtener un `HashMap` con una capacidad inicial predeterminada. El ejemplo de código proporcionado demuestra el uso de `HashMap` al almacenar nombres y números de teléfono de contactos y realizar operaciones como inserción, recuperación, modificación y eliminación.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
