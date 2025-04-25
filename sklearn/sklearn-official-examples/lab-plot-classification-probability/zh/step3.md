# 定义分类器

我们为数据集定义不同的分类器。

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # 用于高斯过程分类器（GPC）

# 创建不同的分类器。
classifiers = {
    "L1 逻辑回归": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 逻辑回归（多项式）": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 逻辑回归（一对多）": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "线性支持向量分类器": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "高斯过程分类器": GaussianProcessClassifier(kernel)
}
```
