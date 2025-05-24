# Contador (Counter)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um contador de lista personalizado que contabilize elementos de lista aninhados, siga estes passos:

1.  Use `counter-reset` para inicializar uma variável de contador (padrão `0`), sendo o nome o valor do atributo (por exemplo, `counter`).
2.  Use `counter-increment` na variável de contador para cada elemento contável (por exemplo, cada `<li>`).
3.  Use `counters()` para exibir o valor de cada variável de contador como parte do `content` do pseudo-elemento `::before` para cada elemento contável (por exemplo, cada `<li>`). O segundo valor passado para ele (`'.'`) atua como o delimitador para contadores aninhados.

Aqui está um exemplo de código HTML:

```html
<ul>
  <li>List item</li>
  <li>List item</li>
  <li>
    List item
    <ul>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
  </li>
</ul>
```

E aqui está o código CSS para aplicar o contador de lista personalizado:

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
