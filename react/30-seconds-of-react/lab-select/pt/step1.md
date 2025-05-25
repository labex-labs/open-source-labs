# Elemento Select Não Controlado (Uncontrolled Select Element)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este é um componente que renderiza um elemento `<select>` não controlado. O componente aceita um array de valores e uma função de callback para passar o valor selecionado ao seu componente pai. Aqui estão os passos para usar este componente:

- Use a prop `selectedValue` para definir o valor inicial do elemento `<select>`.
- Use a prop `onValueChange` para especificar a função de callback que deve ser chamada quando o valor do elemento `<select>` mudar.
- Use `Array.prototype.map()` no array `values` para criar um elemento `<option>` para cada valor passado.
- Cada item em `values` deve ser um array de 2 elementos, onde o primeiro elemento é o `value` do item e o segundo é o texto exibido para ele.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Aqui está um exemplo de como usar este componente:

```jsx
const choices = [
  ["grapefruit", "Grapefruit"],
  ["lime", "Lime"],
  ["coconut", "Coconut"],
  ["mango", "Mango"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
