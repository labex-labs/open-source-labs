# 初期条件を設定して常微分方程式を積分する

次に、シミュレーションの初期条件を設定します。各振り子の初期角度と角速度、およびシミュレーションの時間間隔を設定します。その後、オイラー法を使って常微分方程式を積分し、各時刻での各振り子の位置と速度を求めます。

```python
# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate the ODE using Euler's method
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt
```
