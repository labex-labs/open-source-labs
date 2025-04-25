# 画像の読み込みと前処理

まず、ギリシャのコインの画像を読み込み、処理しやすくするために前処理を行います。画像を元のサイズの 20％にリサイズし、ダウンスケーリングする前にガウシアンフィルタを適用して平滑化し、エイリアシングアーティファクトを軽減します。

```python
# load the coins as a numpy array
orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
