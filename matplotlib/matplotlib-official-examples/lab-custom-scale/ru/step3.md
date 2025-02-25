# Реализуем класс MercatorLatitudeTransform

Внутри класса `MercatorLatitudeScale` мы определим класс `MercatorLatitudeTransform`, который на самом деле будет преобразовывать данные. Этот класс будет наследоваться от `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # Должен быть определен два члена значения.
        # ``input_dims`` и ``output_dims`` определяют количество входных
        # размерностей и выходных размерностей преобразования.
        # Они используются фреймворком преобразования для выполнения
        # некоторых проверок на ошибки и предотвращения соединения
        # несовместимых преобразований.  При определении преобразований
        # для шкалы, которые, по определению, являются разделяемыми и
        # имеют только одну размерность, эти члены должны всегда быть
        # установлены в 1.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            Это преобразование принимает numpy-массив и возвращает преобразованную копию.
            Поскольку диапазон шкалы Меркатора ограничен пользовательским
            порогом, входной массив должен быть замаскирован, чтобы
            содержать только допустимые значения. Matplotlib будет обрабатывать
            замаскированные массивы и удалять из графика данные за пределами
            допустимого диапазона.  Однако возвращаемый массив *должен* иметь
            ту же форму, что и входной массив, так как эти значения должны
            оставаться синхронизированы с значениями в другой размерности.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Переопределите этот метод, чтобы Matplotlib знал, как получить
            обратное преобразование для этого преобразования.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
