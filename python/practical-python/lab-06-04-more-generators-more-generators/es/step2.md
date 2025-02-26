# ¿Por qué Generadores?

- Muchos problemas se expresan con mucha más claridad en términos de iteración.
  - Bucle sobre una colección de elementos y realizar algún tipo de operación (buscar, reemplazar, modificar, etc.).
  - Las tuberías de procesamiento se pueden aplicar a una amplia variedad de problemas de procesamiento de datos.
- Mejora en la eficiencia de memoria.
  - Solo producen valores cuando se necesitan.
  - En contraste con la construcción de listas enormes.
  - Pueden operar sobre datos en streaming
- Los generadores fomentan la reutilización de código
  - Separa la _iteración_ del código que utiliza la iteración
  - Puedes construir una caja de herramientas de funciones de iteración interesantes y _mezclarlas y combinarlas_.
