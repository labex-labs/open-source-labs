# 简介

在本实验中，代码示例中模块的文件层次结构如下所示：有一个名为“my”的目录，其中包含两个文件，“inaccessible.rs”和“nested.rs”。此外，还有一个名为“my.rs”的文件和一个名为“split.rs”的文件。“split.rs”文件包含在“my.rs”文件中定义的模块“my”，而“my.rs”文件分别包含在“inaccessible.rs”和“nested.rs”文件中定义的模块“inaccessible”和“nested”。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用`main.rs`，并通过`rustc main.rs &&./main`进行编译和运行。
