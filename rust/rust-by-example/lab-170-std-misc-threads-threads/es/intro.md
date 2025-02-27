# Introducción

En este laboratorio, tenemos un fragmento de código en Rust que demuestra cómo crear hilos nativos del sistema operativo utilizando la función `spawn` y una clausura móvil. El código crea un vector para almacenar los hilos creados, itera a través de un rango de números para crear múltiples hilos y muestra un mensaje que identifica el número de cada hilo. Finalmente, el hilo principal espera a que cada hilo creado termine utilizando la función `join`.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
