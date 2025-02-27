# Concurrencia extensible con los rasgos Send y Sync

Curiosamente, el lenguaje Rust tiene _muy_ pocos rasgos de concurrencia. Casi todas las características de concurrencia que hemos mencionado hasta ahora en este capítulo son parte de la biblioteca estándar, no del lenguaje. Sus opciones para manejar la concurrencia no se limitan al lenguaje o a la biblioteca estándar; puede escribir sus propias características de concurrencia o usar las escritas por otros.

Sin embargo, dos conceptos de concurrencia están integrados en el lenguaje: los rasgos `std::marker` `Send` y `Sync`.
