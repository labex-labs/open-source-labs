# Comprendiendo Copias y Vistas

Los arrays de NumPy constan de dos partes: el búfer de datos y los metadatos. El búfer de datos contiene los elementos de datos reales, mientras que los metadatos incluyen información como el tipo de datos y los pasos.

Al trabajar con arrays de NumPy, es importante entender la diferencia entre copias y vistas:

- Una **vista** te permite acceder al array de manera diferente cambiando ciertos metadatos sin modificar el búfer de datos. Cualquier cambio realizado en una vista se reflejará en el array original.

- Una **copia** es un nuevo array que duplica tanto el búfer de datos como los metadatos. Los cambios realizados en una copia no afectarán al array original.
