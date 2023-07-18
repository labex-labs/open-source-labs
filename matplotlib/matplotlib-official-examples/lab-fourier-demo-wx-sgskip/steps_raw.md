# Matplotlib Tutorial: Fourier Demo

## Introduction

In this lab, you will learn how to create a simple GUI using Matplotlib in Python. Specifically, you will create a Fourier Demo that displays two waveforms in the frequency and time domains. You will be able to adjust the frequency and amplitude of the waveforms by clicking and dragging on the plot.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We will be using Matplotlib, wxPython, and NumPy. Matplotlib is a plotting library for Python, wxPython is a GUI toolkit for Python, and NumPy is a library for numerical computing with Python.

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```

### Step 2: Define Knob and Param Classes

The next step is to define the Knob and Param classes. These classes will be used to control the frequency and amplitude of the waveforms in the GUI.

```python
class Knob:
    """
    Knob - simple class with a "setKnob" method.
    A Knob instance is attached to a Param instance, e.g., param.attach(knob)
    Base class is for documentation purposes.
    """

    def setKnob(self, value):
        pass


class Param:
    """
    The idea of the "Param" class is that some parameter in the GUI may have
    several knobs that both control it and reflect the parameter's state, e.g.
    a slider, text, and dragging can all change the value of the frequency in
    the waveform of this example.
    The class allows a cleaner way to update/"feedback" to the other knobs when
    one is being changed.  Also, this class handles min/max constraints for all
    the knobs.
    Idea - knob list - in "set" method, knob object is passed as well
      - the other knobs in the knob list have a "set" method which gets
        called for the others.
    """

    def __init__(self, initialValue=None, minimum=0., maximum=1.):
        self.minimum = minimum
        self.maximum = maximum
        if initialValue != self.constrain(initialValue):
            raise ValueError('illegal initial value')
        self.value = initialValue
        self.knobs = []

    def attach(self, knob):
        self.knobs += [knob]

    def set(self, value, knob=None):
        self.value = value
        self.value = self.constrain(value)
        for feedbackKnob in self.knobs:
            if feedbackKnob != knob:
                feedbackKnob.setKnob(self.value)
        return self.value

    def constrain(self, value):
        if value <= self.minimum:
            value = self.minimum
        if value >= self.maximum:
            value = self.maximum
        return value
```

### Step 3: Define SliderGroup Class

The SliderGroup class will create a slider and text field in the GUI for adjusting the frequency and amplitude of the waveforms.

```python
class SliderGroup(Knob):
    def __init__(self, parent, label, param):
        self.sliderLabel = wx.StaticText(parent, label=label)
        self.sliderText = wx.TextCtrl(parent, -1, style=wx.TE_PROCESS_ENTER)
        self.slider = wx.Slider(parent, -1)
        self.slider.SetRange(0, int(param.maximum * 1000))
        self.setKnob(param.value)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.sliderLabel, 0,
                  wx.EXPAND | wx.ALL,
                  border=2)
        sizer.Add(self.sliderText, 0,
                  wx.EXPAND | wx.ALL,
                  border=2)
        sizer.Add(self.slider, 1, wx.EXPAND)
        self.sizer = sizer

        self.slider.Bind(wx.EVT_SLIDER, self.sliderHandler)
        self.sliderText.Bind(wx.EVT_TEXT_ENTER, self.sliderTextHandler)

        self.param = param
        self.param.attach(self)

    def sliderHandler(self, event):
        value = event.GetInt() / 1000.
        self.param.set(value)

    def sliderTextHandler(self, event):
        value = float(self.sliderText.GetValue())
        self.param.set(value)

    def setKnob(self, value):
        self.sliderText.SetValue(f'{value:g}')
        self.slider.SetValue(int(value * 1000))
```

### Step 4: Define FourierDemoFrame Class

The FourierDemoFrame class will create the GUI using wxPython and Matplotlib.

```python
class FourierDemoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        panel = wx.Panel(self)

        # create the GUI elements
        self.createCanvas(panel)
        self.createSliders(panel)

        # place them in a sizer for the Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.frequencySliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.amplitudeSliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(sizer)

    def createCanvas(self, parent):
        self.lines = []
        self.figure = Figure()
        self.canvas = FigureCanvas(parent, -1, self.figure)
        self.canvas.callbacks.connect('button_press_event', self.mouseDown)
        self.canvas.callbacks.connect('motion_notify_event', self.mouseMotion)
        self.canvas.callbacks.connect('button_release_event', self.mouseUp)
        self.state = ''
        self.mouseInfo = (None, None, None, None)
        self.f0 = Param(2., minimum=0., maximum=6.)
        self.A = Param(1., minimum=0.01, maximum=2.)
        self.createPlots()

        self.f0.attach(self)
        self.A.attach(self)

    def createSliders(self, panel):
        self.frequencySliderGroup = SliderGroup(
            panel,
            label='Frequency f0:',
            param=self.f0)
        self.amplitudeSliderGroup = SliderGroup(panel, label=' Amplitude a:',
                                                param=self.A)

    def mouseDown(self, event):
        if self.lines[0].contains(event)[0]:
            self.state = 'frequency'
        elif self.lines[1].contains(event)[0]:
            self.state = 'time'
        else:
            self.state = ''
        self.mouseInfo = (event.xdata, event.ydata,
                          max(self.f0.value, .1),
                          self.A.value)

    def mouseMotion(self, event):
        if self.state == '':
            return
        x, y = event.xdata, event.ydata
        if x is None:  # outside the axes
            return
        x0, y0, f0Init, AInit = self.mouseInfo
        self.A.set(AInit + (AInit * (y - y0) / y0), self)
        if self.state == 'frequency':
            self.f0.set(f0Init + (f0Init * (x - x0) / x0))
        elif self.state == 'time':
            if (x - x0) / x0 != -1.:
                self.f0.set(1. / (1. / f0Init + (1. / f0Init * (x - x0) / x0)))

    def mouseUp(self, event):
        self.state = ''

    def createPlots(self):
        self.subplot1, self.subplot2 = self.figure.subplots(2)
        x1, y1, x2, y2 = self.compute(self.f0.value, self.A.value)
        color = (1., 0., 0.)
        self.lines += self.subplot1.plot(x1, y1, color=color, linewidth=2)
        self.lines += self.subplot2.plot(x2, y2, color=color, linewidth=2)
        self.subplot1.set_title(
            "Click and drag waveforms to change frequency and amplitude",
            fontsize=12)
        self.subplot1.set_ylabel("Frequency Domain Waveform X(f)", fontsize=8)
        self.subplot1.set_xlabel("frequency f", fontsize=8)
        self.subplot2.set_ylabel("Time Domain Waveform x(t)", fontsize=8)
        self.subplot2.set_xlabel("time t", fontsize=8)
        self.subplot1.set_xlim([-6, 6])
        self.subplot1.set_ylim([0, 1])
        self.subplot2.set_xlim([-2, 2])
        self.subplot2.set_ylim([-2, 2])
        self.subplot1.text(0.05, .95,
                           r'$X(f) = \mathcal{F}\{x(t)\}$',
                           verticalalignment='top',
                           transform=self.subplot1.transAxes)
        self.subplot2.text(0.05, .95,
                           r'$x(t) = a \cdot \cos(2\pi f_0 t) e^{-\pi t^2}$',
                           verticalalignment='top',
                           transform=self.subplot2.transAxes)

    def compute(self, f0, A):
        f = np.arange(-6., 6., 0.02)
        t = np.arange(-2., 2., 0.01)
        x = A * np.cos(2 * np.pi * f0 * t) * np.exp(-np.pi * t ** 2)
        X = A / 2 * \
            (np.exp(-np.pi * (f - f0) ** 2) + np.exp(-np.pi * (f + f0) ** 2))
        return f, X, t, x

    def setKnob(self, value):
        x1, y1, x2, y2 = self.compute(self.f0.value, self.A.value)
        self.lines[0].set(xdata=x1, ydata=y1)
        self.lines[1].set(xdata=x2, ydata=y2)
        self.canvas.draw()
```

### Step 5: Define App Class

The App class will create the application and display the GUI.

```python
class App(wx.App):
    def OnInit(self):
        self.frame1 = FourierDemoFrame(parent=None, title="Fourier Demo",
                                       size=(640, 480))
        self.frame1.Show()
        return True
```

### Step 6: Run the Application

The final step is to run the application.

```python
if __name__ == "__main__":
    app = App()
    app.MainLoop()
```

## Summary

In this lab, you learned how to create a simple GUI using Matplotlib in Python. You created a Fourier Demo that displays two waveforms in the frequency and time domains. You were able to adjust the frequency and amplitude of the waveforms by clicking and dragging on the plot.
