# 요약

이 랩에서는 Matplotlib 에서 날짜 정밀도와 에포크를 처리하는 방법을 보여줍니다. `mdates.set_epoch` 메서드를 사용하여 에포크를 이전 기본값 또는 새 기본값으로 설정할 수 있습니다. 그런 다음 `mdates.date2num` 함수를 사용하여 `datetime` 또는 `numpy.datetime64` 객체를 Matplotlib 날짜로 변환하고, `mdates.num2date` 함수를 사용하여 날짜를 왕복 변환하여 변환이 정확한지 확인할 수 있습니다. 또한 플롯의 차이점을 관찰하기 위해 서로 다른 에포크로 데이터를 플로팅할 수도 있습니다.
