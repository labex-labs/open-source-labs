# Criar o RangeSlider

Agora criaremos o widget `RangeSlider`, que nos permitirá ajustar o limiar (threshold) da imagem. Criaremos um novo eixo para o slider e o adicionaremos à figura.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
