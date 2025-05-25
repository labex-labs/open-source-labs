# Função para Retornar a Diferença de Dois Arrays por Mapeamento

Para começar a codificar, abra seu Terminal/SSH e digite `node`.

Esta função recebe dois arrays e aplica a função fornecida a cada elemento em ambos os arrays para retornar sua diferença.

Para fazer isso:

- Crie um `Set` aplicando a função (`fn`) a cada elemento no segundo array (`b`).
- Use `Array.prototype.map()` para aplicar a função (`fn`) a cada elemento no primeiro array (`a`).
- Use `Array.prototype.filter()` em combinação com a função (`fn`) no primeiro array (`a`) para manter apenas os valores que não estão contidos no segundo array (`b`), usando `Set.prototype.has()`.

Aqui está o código para a função:

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

Aqui estão alguns exemplos de como usar a função:

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
