# 요약

이 튜토리얼에서는 Matplotlib 을 사용하여 이미지를 안티앨리어싱 (antialiasing) 하여 고주파 데이터의 서브샘플링 (subsampling) 으로 인한 모아레 패턴을 줄이는 방법을 배웠습니다. 우리는 다양한 주파수 콘텐츠를 가진 450x450 픽셀 이미지를 생성하고, 'nearest' 및 'antialiased' 보간법을 사용하여 이미지를 450 데이터 픽셀에서 125 픽셀 또는 250 픽셀로 서브샘플링했습니다. 또한 'nearest' 보간법을 사용하여 이미지를 업샘플링하는 경우에도 모아레 패턴이 발생할 수 있지만, 더 나은 안티앨리어싱 알고리즘을 사용하면 이러한 영향을 줄일 수 있음을 보여주었습니다.
