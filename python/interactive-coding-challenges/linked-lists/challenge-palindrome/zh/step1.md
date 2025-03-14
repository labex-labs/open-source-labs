# 回文

## 问题

给定一个单链表，判断它是否为回文。如果链表中元素的顺序从前往后和从后往前是相同的，那么这个链表就是一个回文。

## 要求

为了解决这个问题，我们需要考虑以下要求：

- 链表是非循环的单链表。
- 单个字符或数字不被视为回文。
- 我们已经有一个可用于此问题的链表类。
- 我们可以使用额外的数据结构。
- 链表能装入内存。

## 示例用法

以下是该函数应有的一些行为示例：

- 空链表应返回 False。
- 只有一个元素的链表应返回 False。
- 有两个或更多元素且不是回文的链表应返回 False。
- 长度为偶数的回文链表应返回 True。
- 长度为奇数的回文链表应返回 True。
