# 测试驱动开发

既然我们已经将逻辑提取到了 `src/lib.rs` 中，并将参数收集和错误处理留在了 `src/main.rs` 中，那么为代码的核心功能编写测试就容易多了。我们可以直接用各种参数调用函数并检查返回值，而不必从命令行调用我们的二进制文件。

在本节中，我们将使用测试驱动开发（TDD）流程为 `minigrep` 程序添加搜索逻辑，步骤如下：

1. 编写一个会失败的测试，并运行它以确保它因你预期的原因而失败。
2. 编写或修改足够的代码以使新测试通过。
3. 重构你刚刚添加或更改的代码，并确保测试继续通过。
4. 从步骤 1 开始重复！

虽然这只是编写软件的众多方法之一，但 TDD 有助于推动代码设计。在编写使测试通过的代码之前编写测试有助于在整个过程中保持较高的测试覆盖率。

我们将通过测试驱动来实现实际在文件内容中搜索查询字符串并生成匹配查询的行列表的功能。我们将在一个名为 `search` 的函数中添加此功能。
