# 使用新类型模式实现类型安全与抽象

> 注意：本节假设你已阅读前文“使用新类型模式实现外部 trait”。

新类型模式在我们目前讨论的任务之外也很有用，包括静态确保值不会混淆以及指明值的单位。你在清单 19-15 中看到了使用新类型指明单位的示例：回忆一下，`Millimeters` 和 `Meters` 结构体将 `u32` 值包装在一个新类型中。如果我们编写一个带有 `Millimeters` 类型参数的函数，那么当意外尝试使用 `Meters` 类型的值或普通 `u32` 值调用该函数时，程序将无法编译。

我们还可以使用新类型模式来抽象类型的一些实现细节：新类型可以公开一个与私有内部类型的 API 不同的公共 API。

新类型还可以隐藏内部实现。例如，我们可以提供一个 `People` 类型来包装一个 `HashMap<i32, String>`，该 `HashMap` 存储与人员姓名相关联的人员 ID。使用 `People` 的代码只会与我们提供的公共 API 进行交互，比如向 `People` 集合中添加姓名字符串的方法；该代码无需知道我们在内部为姓名分配了一个 `i32` ID。新类型模式是一种实现封装以隐藏实现细节的轻量级方法，我们在“隐藏实现细节的封装”中讨论过这一点。
