# 加权平均数

## 问题

编写一个函数 `weighted_average(nums, weights)`，它接受两个长度相等的列表：`nums` 和 `weights`。该函数应返回 `nums` 中数字的加权平均数，其中每个数字乘以其在 `weights` 中对应的权重。加权平均数的计算方法是将每个数字与其权重的乘积之和除以权重之和。

## 示例

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```

解释：

```
(1 * 0.6 + 2 * 0.2 + 3 * 0.3) / (0.6 + 0.2 + 0.3) = 1.72727
```
