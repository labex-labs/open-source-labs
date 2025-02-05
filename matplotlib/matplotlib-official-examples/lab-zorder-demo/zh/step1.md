# 理解Zorder

Matplotlib 中的 `zorder` 属性是一个浮点数，用于确定艺术家对象的绘制顺序。`zorder` 值较高的艺术家对象会绘制在 `zorder` 值较低的对象之上。`zorder` 的默认值取决于艺术家对象的类型。例如，图像的默认 `zorder` 为 0，而补丁（patch）的默认 `zorder` 为 1。
