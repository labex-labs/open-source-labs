# 加载并预处理图像

我们将从加载希腊硬币的图像并对其进行预处理开始，以便于后续处理。我们会将图像调整为原始大小的 20%，并在缩小尺寸之前应用高斯滤波器进行平滑处理，以减少混叠伪影。

```python
# 将硬币图像加载为 numpy 数组
orig_coins = coins()

# 将其调整为原始大小的 20% 以加快处理速度
# 在缩小尺寸之前应用高斯滤波器进行平滑处理
# 可减少混叠伪影。
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
