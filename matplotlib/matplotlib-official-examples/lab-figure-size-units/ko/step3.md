# 센티미터 단위의 그림 크기

그림 크기를 센티미터 (cm) 단위로 지정할 수도 있습니다. 이렇게 하려면 센티미터 기반 숫자를 인치로 변환해야 합니다. cm 에서 인치로의 변환 계수인 1/2.54 를 센티미터 값에 곱하여 변환할 수 있습니다. 그런 다음 이 값을 subplots 함수의 figsize 매개변수로 사용할 수 있습니다. 아래 코드는 15cm x 5cm 크기의 그림을 만드는 방법을 보여줍니다.

```python
cm = 1/2.54  # centimeters in inches
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
