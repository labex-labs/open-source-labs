# Alternância (Toggle)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para renderizar um componente de alternância, siga estas etapas:

1. Use o hook `useState()` para inicializar a variável de estado `isToggledOn` para `defaultToggled`.
2. Renderize um elemento `<input>` e vincule seu evento `onClick` para atualizar a variável de estado `isToggledOn`. Aplique a `className` apropriada ao elemento `<label>` que o envolve.
3. Use o seguinte CSS para estilizar o componente de alternância:

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Aqui está o código:

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
