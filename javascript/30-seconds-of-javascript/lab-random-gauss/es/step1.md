# Generando números aleatorios gaussianos utilizando la transformada de Box-Muller

Para generar números aleatorios gaussianos (con distribución normal) utilizando la transformada de Box-Muller, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el fragmento de código proporcionado que utiliza la transformada de Box-Muller para generar números aleatorios con una distribución gaussiana.
3. La función `randomGauss()` proporcionada en el fragmento de código genera un número aleatorio con una distribución gaussiana.
4. La salida de la función `randomGauss()` es un número entre 0 y 1.
5. La salida se puede utilizar para diversas aplicaciones, como simulaciones estadísticas, análisis de datos y aprendizaje automático.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

Uso de ejemplo:

```js
randomGauss(); // 0.5
```
