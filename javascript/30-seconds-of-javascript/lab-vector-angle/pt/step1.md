# Cálculo do Ângulo Vetorial

Para calcular o ângulo (theta) entre dois vetores, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()`, `Math.pow()` e `Math.sqrt()` para calcular a magnitude de cada vetor e o produto escalar dos dois vetores.
3.  Use `Math.acos()` para calcular o arco cosseno e obter o valor de theta.

Aqui está um trecho de código de exemplo:

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

Esta função recebe dois arrays (`x` e `y`) como argumentos e retorna o ângulo (em radianos) entre eles.
