# Criando o sinal

Criaremos um sinal usando NumPy. Criaremos um array `xdata` usando a função `linspace` com `start=16`, `stop=365` e `num= (365-16)*4`. Criaremos um array `ydata` usando as funções `sin` e `cos`.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
