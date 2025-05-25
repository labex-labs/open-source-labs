# Adicionar uma Barra de Ferramentas

Adicione uma barra de ferramentas à aplicação que permite ao utilizador aumentar e diminuir o zoom, deslocar (pan) e guardar o gráfico como uma imagem. Esta barra de ferramentas é adicionada à parte inferior do frame.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
