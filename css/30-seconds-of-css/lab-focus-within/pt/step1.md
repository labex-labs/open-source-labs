# Focus Within (Em Foco Dentro)

`index.html` e `style.css` já foram fornecidos na VM (Máquina Virtual).

Para alterar a aparência de um formulário quando qualquer um de seus elementos filhos estiver em foco, use a pseudo-classe `:focus-within` para aplicar estilos ao elemento pai. Por exemplo, no código HTML fornecido, se algum dos campos de entrada estiver em foco, o elemento `form` terá um fundo verde. Para aplicar estilos aos elementos filhos, use seletores CSS apropriados como `label` e `input`.

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Por favor, clique em 'Go Live' (Iniciar) no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
