# Resumen

Se sabe que Lasso recupera datos dispersos de manera efectiva, pero no funciona bien con características altamente correlacionadas. De hecho, si varias características correlacionadas contribuyen al objetivo, Lasso terminaría seleccionando solo una de ellas. En el caso de características dispersas pero no correlacionadas, un modelo Lasso sería más adecuado.

ElasticNet introduce cierta esparsidad en los coeficientes y los reduce a cero. Por lo tanto, en presencia de características correlacionadas que contribuyen al objetivo, el modelo todavía es capaz de reducir sus pesos sin establecirlos exactamente en cero. Esto da como resultado un modelo menos disperso que un Lasso puro y puede capturar también características no predictivas.

ARDRegression es mejor cuando se trata de manejar ruido gaussiano, pero todavía no es capaz de manejar características correlacionadas y requiere una cantidad mayor de tiempo debido a la adaptación de una distribución a priori.
