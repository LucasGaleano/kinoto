from documento import Word
from grafico import Grafico

grafico = Grafico()
grafico.crearGraficoWebFilter()

documento = Word()
informe = documento.abrirDocumento()
#documento.titulo(informe)
documento.webFilter(informe)
documento.crearDocx(informe)
