# Negação (Not), Diferente de (Does-not-equal)

Isso retorna o valor logicamente oposto do que o precede. Ele transforma um `true` em um `false`, etc. Quando usado em conjunto com o operador de igualdade, o operador de negação testa se dois valores não são iguais.

Para "Negação (Not)", a expressão básica é verdadeira, mas a comparação retorna `false` porque a negamos:

```js
// Not(!)
let myVariable = 3;
!(myVariable === 3);
```

"Diferente de (Does-not-equal)" dá basicamente o mesmo resultado com uma sintaxe diferente. Aqui estamos testando "a variável `myVariable` NÃO é igual a 3". Isso retorna `false` porque `myVariable` É igual a 3:

```js
// Does-not-equal(!==)
let myVariable = 3;
myVariable !== 3;
```

Há muitos mais operadores para explorar, mas isso é suficiente por enquanto. Consulte [Expressões e operadores](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) para obter uma lista completa.

> **Observação:** Misturar tipos de dados pode levar a resultados estranhos ao realizar cálculos. Tenha cuidado para se referir às suas variáveis corretamente e obter os resultados esperados. Por exemplo, digite `'35' + '25'` no seu console. Por que você não obtém o resultado esperado? Porque as aspas transformam os números em strings, então você acabou concatenando strings em vez de somar números. Se você digitar `35 + 25`, obterá o total dos dois números.
