# 总结

在本实验中，我们使用了 Scikit-learn 中的 KBinsDiscretizer 对浣熊脸的样本图像执行向量量化。我们使用 8 个灰度级来表示图像，这样可以压缩到每个像素仅使用 3 位。我们比较了均匀和 k 均值聚类策略，以将像素值映射到 8 个灰度级。我们发现 k 均值聚类策略提供了更平衡的像素值分布。我们还检查了压缩图像的内存使用情况，发现由于对压缩图像使用了 64 位浮点数表示，压缩后的图像占用的内存是原始图像的 8 倍。
