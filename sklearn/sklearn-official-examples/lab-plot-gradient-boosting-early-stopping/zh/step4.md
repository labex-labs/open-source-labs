# 使用早期停止构建并训练模型

现在我们将构建并训练一个使用早期停止的梯度提升模型。我们指定一个`validation_fraction`（验证分数），它表示从整个数据集中留出用于评估模型验证损失的部分。梯度提升模型使用训练集进行训练，并使用验证集进行评估。当添加回归树的每个额外阶段时，使用验证集对模型进行评分。这个过程会一直持续，直到模型在最后`n_iter_no_change`个阶段的分数至少没有提高`tol`。在此之后，模型被认为已经收敛，并且进一步添加阶段被“提前停止”。最终模型的阶段数可以在属性`n_estimators`中获得。

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
