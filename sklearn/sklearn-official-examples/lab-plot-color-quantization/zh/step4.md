# 使用随机码本预测颜色索引

我们将使用随机码本预测整个图像的颜色索引。

```python
# 获取一个随机码本
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# 使用随机码本预测整个图像的颜色索引
print("预测整个图像的颜色索引 (随机)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"完成于 {time() - t0:0.3f} 秒。")
```
