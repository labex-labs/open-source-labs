# Сравнить с эквивалентным кодом на MATLAB

Можем сравнить предыдущий код с эквивалентным кодом на MATLAB для выполнения того же действия:

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
