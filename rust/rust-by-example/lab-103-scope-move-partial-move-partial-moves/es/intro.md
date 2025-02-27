# Introducción

En este laboratorio, aprendemos sobre los movimientos parciales dentro de la desestructuración de una variable única, donde se pueden utilizar simultáneamente los enlaces de patrón `by-move` y `by-reference`. Esto da lugar a un movimiento parcial de la variable, lo que permite que algunas partes se muevan mientras que otras todavía se pueden referenciar. Si una variable padre se mueve parcialmente, no se puede utilizar como un todo después, pero las partes que solo se refieren y no se mueven todavía se pueden utilizar.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede utilizar cualquier nombre de archivo que desee. Por ejemplo, puede utilizar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
