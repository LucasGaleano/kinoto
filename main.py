from documento import Word
from grafico import Grafico
from datetime import datetime
from elastic import Info
from auxiliares import devolverMes

response = Info().infoWebFilter()

documento = Word()
informe = documento.abrirDocumento()
documento.titulo(informe, title='Reporte Mensual OSSIM', subtitle=f'{devolverMes(datetime.now().month)} {datetime.now().year}')
documento.creaPagina(informe, response, title='Top de bloqueos de Webfilter por usuario', introduction='\nEn el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.\n', column_tags=['Users', 'Blocks'])
documento.guarda(informe)
