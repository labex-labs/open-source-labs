# Convertendo Graus para Radianos

Para converter um ângulo de graus para radianos, siga estes passos:

1.  Abra o Terminal/SSH.
2.  Digite `node` para começar a codificar.
3.  Use a fórmula de graus para radianos juntamente com `Math.PI`.
4.  Aplique a fórmula ao ângulo em graus para obter o ângulo em radianos.

Aqui está a fórmula em JavaScript:

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

Por exemplo, se você deseja converter 90 graus para radianos, pode usar a função `degreesToRads` desta forma:

```js
degreesToRads(90.0); // ~1.5708
```
