# Definir a função de retorno de chamada (callback) de seleção

A função de retorno de chamada (callback) de seleção será chamada toda vez que o usuário selecionar um retângulo ou elipse. A função receberá os eventos de clique e liberação como argumentos e imprimirá as coordenadas do retângulo ou elipse.

```python
def select_callback(eclick, erelease):
    """
    Função de retorno de chamada para seleção de linha.

    *eclick* e *erelease* são os eventos de pressionar e soltar.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
