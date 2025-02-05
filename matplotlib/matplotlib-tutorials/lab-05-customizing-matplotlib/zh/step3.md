# 更改matplotlibrc文件

`matplotlibrc` 文件是一个配置文件，它允许你自定义Matplotlib中的各种属性。它控制着诸如图形大小、线宽、颜色、字体等属性的默认设置。你可以根据自己的喜好修改 `matplotlibrc` 文件来自定义Matplotlib。该文件可能位于系统中的不同位置，Matplotlib会按特定顺序查找它。一旦找到 `matplotlibrc` 文件，它将优先于其他设置。你可以使用 `matplotlib.matplotlib_fname()` 函数来显示当前活动的 `matplotlibrc` 文件的路径。
