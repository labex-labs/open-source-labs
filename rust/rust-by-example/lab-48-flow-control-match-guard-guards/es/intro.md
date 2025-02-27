# Introducción

En este laboratorio, aprendemos a usar los filtros de coincidencia (`match guards`) en Rust para filtrar los brazos (`arms`) basados en condiciones. El filtro de coincidencia se agrega después del patrón y está representado por la palabra clave `if` seguida de una condición. La condición del filtro nos permite refinar aún más la coincidencia de patrones y realizar comprobaciones adicionales antes de ejecutar el brazo correspondiente de la expresión `match`. Sin embargo, es importante tener en cuenta que el compilador no considera las condiciones de filtro al comprobar la cobertura de patrones, por lo que es necesario asegurarse de que todos los patrones sigan estando cubiertos por la expresión `match`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
