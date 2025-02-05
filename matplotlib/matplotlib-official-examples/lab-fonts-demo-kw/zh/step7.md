# 展示粗体斜体

作为额外内容，我们还可以展示同时具有粗体和斜体样式的文本。我们将使用`fig.text()`方法来展示具有适当样式、粗细和大小的文本。

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```
