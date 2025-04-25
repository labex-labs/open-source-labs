# 独立成分分析（ICA）

#### 用于盲源分离的 ICA

独立成分分析（ICA）用于将混合信号分离为其原始源成分。它假设这些成分在统计上是独立的，并且可以通过线性解混过程提取出来。可以使用 scikit-learn 中的`FastICA`类来实现 ICA。

```python
from sklearn.decomposition import FastICA

# 创建一个 ICA 对象，n_components 为所需的成分数量
ica = FastICA(n_components=2)

# 将 ICA 模型拟合到混合信号上
ica.fit(mixed_signals)

# 将混合信号分离为原始源成分
source_components = ica.transform(mixed_signals)
```
