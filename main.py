from documento import Word
from grafico import Grafico
from datetime import datetime
from elastic import Info
from auxiliares import devolverMes

elastic = Info()
print ("Creando conexion..", end = '')
elastic.crearConexion()
print (".. Listo!")

print ("Recopilando info..", end = '')
webFilter = elastic.infoWebFilter()
topApp = elastic.infoTopApp()
flowLogs = elastic.infoFlowLogs()
print (".. Listo!")

documento = Word()

print ("Creando Word..", end = '')
informe = documento.abrirDocumento()
print (".. Listo!")

print ("Aplicando titulo..", end = '')
documento.titulo(informe, title='Reporte Mensual OSSIM', subtitle=f'{devolverMes(datetime.now().month)} {datetime.now().year}')
print (".. Listo!")

print ("Creando paginas..", end = '')
documento.creaPagina(informe, webFilter, title='Top de bloqueos de Webfilter por usuario', introduction='\nEn el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.\n', column_tags=['Users', 'Blocks'], grafico = 'Barra', filename = 'graficoDeBarra')
documento.creaPagina(informe, topApp, title='Top de aplicaciones', introduction='\nEn el siguiente gráfico se detallan las aplicaciones mas usadas.\n', column_tags=['App', 'Traffic'], grafico = 'Torta', filename = 'graficoDeTorta')
#documento.creaPagina(informe, flowLogs, title='Logs Por Tiempo', introduction='\n.\n', column_tags=['Logs', 'Cantidad'], grafico = 'Tiempo', filename = 'graficoEnElTiempo')
print (".. Listo!")

print ("Guardando informe..", end = '')
documento.guarda(informe)
print (".. Listo!")
