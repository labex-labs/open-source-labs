# FeatureUnion - 複合特徴空間

`FeatureUnion` クラスは、複数のトランスフォーマーオブジェクトを結合して、それらの出力を組み合わせた新しいトランスフォーマーを作成するために使用されます。これは、データの異なる特徴に対して異なる変換を適用したい場合に便利です。たとえば、テキスト、浮動小数点数、日付をそれぞれ別々に前処理する場合などです。トランスフォーマーは並列に適用され、それらが出力する特徴行列は横並びに連結されてより大きな行列になります。以下は例です：

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
