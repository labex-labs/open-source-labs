# Personalizar os Rótulos dos Eixos

Podemos personalizar os rótulos dos eixos do nosso gráfico usando também o dicionário de fontes. Definiremos o parâmetro `fontdict` das funções `xlabel()` e `ylabel()` para o nosso dicionário de fontes.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
