# Cálculo del Coeficiente Binomial

Para calcular el número de maneras de elegir `k` elementos de `n` elementos sin repetición y sin orden, puedes utilizar la siguiente función de JavaScript:

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

Para utilizar la función, abre la Terminal/SSH y escribe `node`. Luego, llama a la función con los valores deseados. Por ejemplo:

```js
binomialCoefficient(8, 2); // 28
```

Para asegurarte de que la función funcione correctamente, puedes seguir estos pasos:

1. Utiliza `Number.isNaN()` para comprobar si cualquiera de los dos valores es `NaN`.
2. Comprueba si `k` es menor que `0`, mayor o igual que `n`, igual a `1` o `n - 1` y devuelve el resultado adecuado.
3. Comprueba si `n - k` es menor que `k` y cambia sus valores en consecuencia.
4. Bucle desde `2` hasta `k` y calcula el coeficiente binomial.
5. Utiliza `Math.round()` para tener en cuenta los errores de redondeo en el cálculo.
