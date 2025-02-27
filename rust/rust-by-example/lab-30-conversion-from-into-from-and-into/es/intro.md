# Introducción

En este laboratorio, exploramos los conceptos de los tratos `From` e `Into` en Rust, que se utilizan para convertir entre diferentes tipos. Estos tratos están inherentemente vinculados, con `Into` siendo el recíproco de `From`. El trato `From` permite que un tipo defina cómo crear sí mismo a partir de otro tipo, lo que facilita la conversión entre tipos. El trato `Into` llama automáticamente a la implementación de `From` cuando sea necesario. Ambos tratos se pueden implementar para tipos personalizados, lo que proporciona flexibilidad en las conversiones de tipos.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
