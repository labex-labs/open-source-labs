# Verificando Valores Primitivos

Para praticar a codificação, abra o Terminal ou SSH e digite `node`. Depois de fazer isso, você pode verificar se um valor é primitivo ou não, seguindo estas etapas:

1.  Crie um objeto a partir do valor que você deseja verificar usando `Object(val)`.
2.  Compare o objeto criado com o valor original usando o operador de desigualdade estrita `!==`.
3.  Se os dois valores não forem iguais, o valor original é primitivo.

Aqui está o código para a função `isPrimitive`:

```js
const isPrimitive = (val) => Object(val) !== val;
```

Você pode testar esta função com os seguintes valores:

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

Se o valor que você deseja verificar for primitivo, a função retornará `true`. Caso contrário, retornará `false`.
