# Escribiendo código para que la prueba pase

Actualmente, nuestra prueba está fallando porque siempre devolvemos un vector vacío. Para solucionar eso e implementar `search`, nuestro programa debe seguir estos pasos:

1.  Itera a través de cada línea del contenido.
2.  Verifica si la línea contiene la cadena de consulta.
3.  Si es así, agréguela a la lista de valores que estamos devolviendo.
4.  Si no es así, no hagas nada.
5.  Devuelve la lista de resultados que coinciden.

Vamos a trabajar en cada paso, comenzando por iterar a través de las líneas.
