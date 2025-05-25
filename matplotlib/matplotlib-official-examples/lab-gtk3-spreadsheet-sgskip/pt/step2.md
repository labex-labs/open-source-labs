# Criar a Janela do Gerenciador de Dados

Nesta etapa, criaremos a classe `DataManager` que estende a classe `Gtk.Window`. Essa classe será responsável por gerenciar os dados que queremos plotar.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
