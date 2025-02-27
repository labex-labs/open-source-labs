# Generar datos sintéticos

Generaremos datos sintéticos para un problema de regresión aplicando la función a entradas aleatorias muestreadas uniformemente. Para que el problema sea interesante, generamos las observaciones de la variable objetivo y como la suma de un término determinista calculado por la función f y un término de ruido aleatorio que sigue una distribución log-normal centrada. La distribución log-normal no es simétrica y tiene una cola larga: es probable observar valores atípicos grandes, pero es imposible observar valores atípicos pequeños.
