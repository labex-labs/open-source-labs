# Animação de Encolhimento de Botão

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de encolhimento ao passar o mouse (hover) sobre um elemento, você pode usar uma propriedade `transition` apropriada para animar as mudanças e a pseudo-classe `:hover` para acionar a animação. Por exemplo, se você deseja encolher um botão com a classe `button-shrink` quando um usuário passa o mouse sobre ele, você pode adicionar o seguinte CSS:

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

Isso aplicará um efeito de transição a todas as propriedades do botão quando houver uma mudança, e quando o usuário passar o mouse sobre ele, o botão encolherá para 80% de seu tamanho original. O código HTML para o botão é o seguinte:

```html
<button class="button-shrink">Submit</button>
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
