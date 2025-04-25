# 创建画布框架

首先，我们将创建一个用于容纳 Matplotlib 绘图的画布框架。我们将添加一个正弦曲线绘图来演示光标的功能。

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # 创建一个 Figure 并添加一个子图
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # 绘制正弦曲线
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # 创建一个 FigureCanvas 来显示绘图
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # 绑定 motion_notify_event 以更新状态栏
        self.figure_canvas.mpl_connect(
           'motion_notify_event', self.UpdateStatusBar)

        # 绑定 enter_window 事件以更改光标
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # 创建一个尺寸器并将 FigureCanvas 添加到其中
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # 创建一个状态栏以报告光标的位置
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # 创建一个工具栏以浏览绘图
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
