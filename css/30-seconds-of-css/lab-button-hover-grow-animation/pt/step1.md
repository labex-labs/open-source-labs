# Animação de Crescimento do Botão

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de crescimento ao passar o mouse (hover), você pode usar uma `transition` apropriada para animar as mudanças no elemento. Use a pseudo-classe `:hover` para alterar a propriedade `transform` para `scale(1.1)`. Isso fará com que o elemento cresça quando o usuário passar o mouse sobre ele.

Aqui está um trecho de código de exemplo que você pode usar:

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
