# 更新哈希映射

虽然键值对的数量是可以增长的，但每个唯一的键在同一时间只能与一个值相关联（反之则不然：例如，蓝色队伍和黄色队伍都可以在 `scores` 哈希映射中存储值 `10`）。

当你想要更改哈希映射中的数据时，你必须决定如何处理键已经有值的情况。你可以用新值替换旧值，完全忽略旧值。你可以保留旧值并忽略新值，只有在键还没有值时才添加新值。或者你可以将旧值和新值合并。让我们看看如何实现这些操作！
