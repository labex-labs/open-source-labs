# Ferramentas de Teste de Terceiros (Third Party Test Tools)

O módulo `unittest` embutido tem a vantagem de estar disponível em todos os lugares - ele faz parte do Python. No entanto, muitos programadores também o consideram bastante verboso. Uma alternativa popular é o [pytest](https://docs.pytest.org/en/latest/). Com o pytest, seu arquivo de teste se simplifica para algo como o seguinte:

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

Para executar um teste, basta digitar um comando como `python -m pytest`. Ele então encontrará e executará todos os testes. O módulo pode ser instalado usando `pip install pytest`.

Há muito mais no `pytest` do que este exemplo, mas geralmente é bem fácil começar caso você decida experimentá-lo.

Neste exercício, você explorará a mecânica básica do uso do módulo `unittest` do Python.

Em exercícios anteriores, você escreveu um arquivo `stock.py` que continha uma classe `Stock`. Para este exercício, presume-se que você está usando o código escrito para o Exercício 7.9, envolvendo propriedades tipadas (typed-properties). Se, por alguma razão, isso não estiver funcionando, você pode querer copiar a solução de `Solutions/7_9` para o seu diretório de trabalho.
