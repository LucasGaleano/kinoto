from documento import Word
from grafico import Grafico
from datetime import datetime
from elastic import Info

grafico = Grafico()
grafico.crearGraficoWebFilter()
response = Info().infoWebFilter()

documento = Word()
informe = documento.abrirDocumento()
documento.titulo(informe, title='Reporte Mensual OSSIM', subtitle=f'{datetime.now().month} {datetime.now().year}')
documento.webFilter(informe, response, title='Top de bloqueos de Webfilter por usuario', introduction='En el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.', column_tags=['Users', 'Blocks'])
documento.crearDocx(informe)
