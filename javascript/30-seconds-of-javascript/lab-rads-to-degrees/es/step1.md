# Convertir Radianes a Grados

Para convertir un ángulo de radianes a grados, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la siguiente fórmula: `grados = radianes * (180 / Math.PI)`
3. Reemplaza `radianes` en la fórmula con el valor que quieres convertir.
4. El resultado estará en grados.

Aquí hay un ejemplo:

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

Esto convertirá `π/2` radianes a `90` grados.
