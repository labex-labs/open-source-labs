# Create Main App Class

We will create a main app class that inherits from `wx.App`. In the `OnInit` method, we will load the XRC file, create a panel, and create a plot container.

```python
class MyApp(wx.App):
    def OnInit(self):
        xrcfile = cbook.get_sample_data('embedding_in_wx3.xrc', asfileobj=False)
        self.res = xrc.XmlResource(xrcfile)

        self.frame = self.res.LoadFrame(None, "MainFrame")
        self.panel = xrc.XRCCTRL(self.frame, "MainPanel")

        plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.plotpanel = PlotPanel(plot_container)
        self.plotpanel.init_plot_data()

        sizer.Add(self.plotpanel, 1, wx.EXPAND)
        plot_container.SetSizer(sizer)

        whiz_button = xrc.XRCCTRL(self.frame, "whiz_button")
        whiz_button.Bind(wx.EVT_BUTTON, self.plotpanel.OnWhiz)

        bang_button = xrc.XRCCTRL(self.frame, "bang_button")
        bang_button.Bind(wx.EVT_BUTTON, self.OnBang)

        self.frame.Show()
        self.SetTopWindow(self.frame)

        return True
```
