# Visualização de Tabela de Objetos

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este componente renderiza uma tabela com linhas que são criadas dinamicamente a partir de um array de objetos e uma lista de nomes de propriedades. Para conseguir isso:

- Use `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()` e `Array.prototype.reduce()` para produzir um array `filteredData` que contém todos os objetos com as chaves especificadas em `propertyNames`.
- Renderize um elemento `<table>` com um conjunto de colunas igual ao número de valores em `propertyNames`.
- Use `Array.prototype.map()` para renderizar cada valor no array `propertyNames` como um elemento `<th>`.
- Use `Array.prototype.map()` para renderizar cada objeto no array `filteredData` como um elemento `<tr>` contendo um `<td>` para cada chave no objeto.
- Observe que este componente não funciona com objetos aninhados e irá quebrar se houver objetos aninhados dentro de qualquer uma das propriedades especificadas em `propertyNames`.

Aqui está o código:

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Você pode usar o componente passando um array de objetos e uma lista de nomes de propriedades:

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
