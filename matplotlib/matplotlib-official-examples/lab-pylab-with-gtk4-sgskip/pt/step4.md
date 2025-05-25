# Adicionar um botão à barra de ferramentas

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

Criamos um botão com um rótulo e uma dica de ferramenta (tooltip), e o conectamos a uma função que imprime uma mensagem no console. Adicionamos o botão à barra de ferramentas.
