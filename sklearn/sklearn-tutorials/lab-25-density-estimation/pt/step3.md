# Ajustar um estimador de densidade kernel

Agora, criaremos uma instância do estimador `KernelDensity` e o ajustaremos aos nossos dados. Podemos escolher o tipo de kernel e a largura de banda para o estimador. Por exemplo, podemos usar um kernel gaussiano e definir a largura de banda para 0,2.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
