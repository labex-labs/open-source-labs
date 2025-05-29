# Pilha de Fontes do Sistema (System Font Stack)

`index.html` e `style.css` já foram fornecidos na VM.

Para obter uma sensação de aplicativo nativo, use a fonte nativa do sistema operacional. Defina uma lista de fontes usando `font-family`. O navegador procura cada fonte sucessiva, preferindo a primeira, se possível, e recorre à próxima se não conseguir encontrar a fonte (no sistema ou definida em CSS). Use `-apple-system` para San Francisco no iOS e macOS (não Chrome), e `BlinkMacSystemFont` para San Francisco no macOS Chrome. Para Windows 10, use `'Segoe UI'`, para Android use `Roboto`, para Linux com KDE use `Oxygen-Sans`, para Ubuntu (todas as variantes) use `Ubuntu`, e para Linux com GNOME Shell use `Cantarell`. Para macOS 10.10 e anteriores, use `'Helvetica Neue'` e `Helvetica`. Para uma fonte sans serif de fallback que é amplamente suportada por todos os sistemas operacionais, use `Arial`. Para aplicar a fonte do sistema a um texto específico, use o seguinte HTML e CSS:

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
