# Conectar os _Sliders_ à Função de Atualização

Nesta etapa, você conectará os _sliders_ à função de atualização. Isso garantirá que o gráfico seja atualizado sempre que os valores dos _sliders_ forem alterados.

```python
sfreq.on_changed(update)
samp.on_changed(update)
```
