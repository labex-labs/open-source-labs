# Input com Prefixo

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma entrada com um prefixo visual e não editável, siga estes passos:

1.  Use `display: flex` para criar um elemento container com a classe `.input-box`.
2.  Remova a borda e o contorno do campo `<input>` e aplique-os ao elemento pai em vez disso, para que ele se pareça com uma caixa de entrada.
3.  Use o seletor de pseudo-classe `:focus-within` para estilizar o elemento pai de acordo quando o usuário interage com o campo `<input>`.

Aqui está o código HTML:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

E aqui está o código CSS:

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box .prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
