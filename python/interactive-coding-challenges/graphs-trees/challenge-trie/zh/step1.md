# 字典树（Trie）

## 问题

你的任务是实现一个具有以下方法的字典树：

- `find(word)` - 如果给定的单词在字典树中，则返回 `True`，否则返回 `False`。
- `insert(word)` - 将给定的单词插入到字典树中。
- `remove(word)` - 从字典树中删除给定的单词。
- `list_words()` - 返回字典树中所有以终止字符结尾的单词的列表。

## 要求

要完成此挑战，必须满足以下要求：

- 实现应适用于字符串。
- 假设字符串为 ASCII 编码。
- `find` 方法应仅匹配带有终止字符的精确单词。
- `list_words` 方法应仅返回带有终止字符的单词。
- 假设实现适合内存。

## 示例用法

以下示例演示了字典树方法的用法：

```txt

         根节点
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

查找

* 在空字典树中查找
* 查找不匹配的情况
* 查找匹配的情况

插入

* 插入到空字典树
* 插入以创建叶终止字符
* 插入以扩展现有的终止字符

删除

* 删除我
* 删除 mens
* 删除 a
* 删除 has

列出单词

* 列出空字典树
* 列出一般情况
```
