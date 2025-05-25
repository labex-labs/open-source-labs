# Entrada de Intervalo (Range Input) Não Controlada

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um controle deslizante (slider) em React, use o componente `Slider` e passe as props `min`, `max`, `defaultValue` e `onValueChange`.

No componente `Slider`, defina o `type` do elemento `<input>` como `"range"` para criar um controle deslizante. Use a prop `defaultValue` passada do pai como o valor inicial do campo de entrada não controlado. Use o evento `onChange` para disparar o callback `onValueChange` e enviar o novo valor para o pai.

Aqui está o código para o componente `Slider`:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Para renderizar o componente `Slider`, use `ReactDOM.createRoot` e passe a função de callback `onValueChange`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
