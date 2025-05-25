# 호출 가능한 객체를 사용한 막대 레이블 지정

마지막으로, 호출 가능한 객체 (callable) 를 사용하여 막대 레이블을 형식화하는 방법을 보여줍니다. 다양한 동물의 달리기 속도에 대한 데이터를 사용합니다.

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```
