# Resumo

Este laboratório demonstra como lidar com a precisão de datas e épocas no Matplotlib. Podemos definir a época para o padrão antigo ou o novo padrão usando o método `mdates.set_epoch`. Em seguida, podemos converter objetos `datetime` ou `numpy.datetime64` para datas Matplotlib usando a função `mdates.date2num` e fazer a conversão de ida e volta das datas usando a função `mdates.num2date` para garantir que a conversão seja precisa. Também podemos plotar dados com diferentes épocas para observar as diferenças no gráfico.
