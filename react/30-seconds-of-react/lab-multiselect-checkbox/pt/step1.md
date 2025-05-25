# _Checkbox_ com Estado e Seleção Múltipla

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código renderiza uma lista de _checkboxes_ e envia o(s) valor(es) selecionado(s) para o componente pai usando uma função _callback_. Aqui estão os passos para criá-lo:

1.  Use o _hook_ `useState()` para inicializar a variável de estado `data` com a _prop_ `options`.
2.  Crie uma função `toggle` que atualiza a variável de estado `data` com a(s) opção(ões) selecionada(s) e chama a função _callback_ `onChange` com elas.
3.  Mapeie a variável de estado `data` para gerar _checkboxes_ individuais e seus rótulos. Associe a função `toggle` ao _handler_ `onClick` de cada _checkbox_.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Aqui está um exemplo de como usá-lo:

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
