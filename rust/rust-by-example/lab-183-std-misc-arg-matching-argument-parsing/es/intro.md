# Introducción

En este laboratorio, tenemos un ejemplo de análisis de argumentos utilizando coincidencia de patrones en Rust. El programa toma argumentos de línea de comandos y realiza diferentes operaciones según el número y el tipo de argumentos pasados. Si no se pasan argumentos, imprime un mensaje. Si se pasa un solo argumento y se puede analizar como el entero 42, imprime "This is the answer!". Si se pasan un comando y un argumento entero, realiza una operación de aumento o disminución en el entero. Si se pasan cualquier otro número de argumentos, muestra un mensaje de ayuda que explica el uso correcto del programa.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
