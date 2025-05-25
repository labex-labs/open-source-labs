# Lista de Dados

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função renderiza uma lista de itens a partir de um array de valores primitivos. Ela pode ser usada para renderizar condicionalmente uma lista ordenada ou não ordenada com base no valor da prop `isOrdered`. Para renderizar cada item do array `data`, ela usa `Array.prototype.map()` para criar um elemento `<li>` com uma `key` única para cada item.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

Aqui está um exemplo de como você pode usar este componente:

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

Neste exemplo, estamos passando um array de nomes para o componente `DataList` e renderizando-o duas vezes. Na primeira vez, estamos renderizando uma lista não ordenada, enquanto na segunda vez estamos renderizando uma lista ordenada.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
