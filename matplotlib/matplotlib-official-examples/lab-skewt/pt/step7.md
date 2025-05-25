# Preparar os Dados

Prepararemos os dados para o nosso diagrama SkewT-logP. Usaremos o módulo StringIO para ler os dados de uma string e o NumPy para carregá-los em arrays.

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
        ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```
