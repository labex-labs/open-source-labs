# 练习8.3：向程序添加日志记录

要向应用程序添加日志记录，你需要有某种机制在主模块中初始化日志记录模块。一种方法是包含一些如下所示的设置代码：

    # 此文件设置日志记录模块的基本配置。
    # 根据需要在此处更改设置以调整日志输出。
    import logging
    logging.basicConfig(
        filename = 'app.log',            # 日志文件的名称（省略则使用stderr）
        filemode = 'w',                  # 文件模式（使用'a'进行追加）
        level    = logging.WARNING,      # 日志记录级别（DEBUG、INFO、WARNING、ERROR或CRITICAL）
    )

同样，你需要将此代码放在程序启动步骤中的某个位置。例如，在你的`report.py`程序中，你会把它放在哪里呢？
