# 列表删除

你可以通过元素值或索引来删除列表中的元素：

```python
# 使用值
names.remove('Curtis')

# 使用索引
del names[1]
```

删除一个元素不会留下空洞。其他元素会向下移动以填补腾出的空间。如果元素出现不止一次，`remove()` 只会删除第一次出现的元素。
