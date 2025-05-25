# Carregar e pré-processar a imagem

Começaremos carregando a imagem das moedas gregas e pré-processando-a para facilitar o trabalho. Redimensionaremos a imagem para 20% do tamanho original e aplicaremos um filtro Gaussiano para suavização antes da redução de escala, a fim de reduzir artefactos de aliasing.

```python
# carregar as moedas como um array numpy
orig_coins = coins()

# Redimensioná-la para 20% do tamanho original para acelerar o processamento
# Aplicar um filtro Gaussiano para suavização antes da redução de escala
# reduz artefactos de aliasing.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
