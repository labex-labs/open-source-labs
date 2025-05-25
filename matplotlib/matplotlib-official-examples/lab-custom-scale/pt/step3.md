# Implementar a classe MercatorLatitudeTransform

Dentro da classe `MercatorLatitudeScale`, definiremos a classe `MercatorLatitudeTransform` que realmente transformará os dados. Esta classe herdará de `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # Existem dois membros de valor que devem ser definidos.
        # ``input_dims`` e ``output_dims`` especificam o número de dimensões de entrada
        # e dimensões de saída para a transformação.
        # Estes são usados pelo framework de transformação para fazer algumas
        # verificações de erros e evitar que transformações incompatíveis sejam
        # conectadas. Ao definir transformações para uma
        # escala, que são, por definição, separáveis e têm apenas uma
        # dimensão, esses membros devem sempre ser definidos como 1.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            Esta transformação recebe um array numpy e retorna uma cópia transformada.
            Como a faixa da escala de Mercator é limitada pelo
            limite especificado pelo usuário, o array de entrada deve ser mascarado para
            conter apenas valores válidos. Matplotlib lidará com arrays mascarados
            e removerá os dados fora da faixa do gráfico. No entanto, o
            array retornado *deve* ter a mesma forma do array de entrada, uma vez que
            esses valores precisam permanecer sincronizados com os valores na outra
            dimensão.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Substitua este método para que o Matplotlib saiba como obter a
            transformação inversa para esta transformação.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
