# 동등한 MATLAB 코드와 비교

이전 코드를 동일한 작업을 수행하는 동등한 MATLAB 코드와 비교할 수 있습니다.

```python
dt = 0.01;
t = [0:dt:10];
nse = randn(size(t));
r = exp(-t/0.05);
cnse = conv(nse, r)*dt;
cnse = cnse(1:length(t));
s = 0.1*sin(2*pi*t) + cnse;

subplot(211)
plot(t, s)
subplot(212)
psd(s, 512, 1/dt)
```
