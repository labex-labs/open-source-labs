# Tabela de Dados

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Crie um elemento de tabela com duas colunas, `ID` e `Valor`, onde cada linha é gerada dinamicamente a partir de um array de valores primitivos.

Para realizar isso, use o método `Array.prototype.map()` para criar um novo array de elementos JSX representando cada item no array de entrada `data` como um elemento `<tr>` com uma `key` apropriada. Dentro de cada `<tr>`, adicione dois elementos `<td>` para exibir o índice e o valor da linha, respectivamente.

Aqui está um exemplo de implementação:

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Para usar este componente com um array de nomes de pessoas, por exemplo, você pode chamá-lo da seguinte forma:

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
