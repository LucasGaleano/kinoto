from docx import Document
from docx.enum.text import WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from datetime import datetime
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor
from auxiliares import devolverMes
from estilo import Estilos
from elastic import Info

class Word:

    def abrirDocumento(self):
        informe = Document('./template-info/template.docx')
        estilos = Estilos()
        estilos.styleTitle(informe)
        estilos.styleBodyText(informe)
        estilos.styleHeading1(informe)
        estilos.styleSubtitle(informe)


        return informe


    def crearDocx(self, informe):
        informe.save('./informe/informe.docx')

    def titulo(self, informe):
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        mesActual = devolverMes(currentMonth)
        informe.add_paragraph('Reporte Mensual OSSIM', style = 'Title')
        informe.add_paragraph(f'{mesActual} {currentYear}', style = 'Subtitle')
        informe.add_page_break()

    def webFilter(self, informe):
        informacion = Info()
        response = informacion.infoWebFilter()

        informe.add_paragraph('Top de bloqueos de Webfilter por usuario', style = 'Heading 1')
        informe.add_paragraph('En el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.', style='Body Text')
        column_tags = []
        column_tags.append('Users')
        column_tags.append('Blocks')
        self.tabla(informe, 2, column_tags, response)
        informe.add_picture('./imagenes/graficoDeBarra.png')
        informe.add_page_break()

    def tabla(self, informe, columns, column_tags, informacion):
        table = informe.add_table(rows = 1, cols = columns)
        #table.autofit = True
        table.style = "BTR Table"
        column_etiquetas = table.rows[0].cells
        index = 0
        for i in column_etiquetas:
            i.text = column_tags[index]
            index += 1

        zip_informacion = zip([i.key for i in informacion],[i.doc_count for i in informacion])
        diccionario_informacion = dict(zip_informacion)

        for key, value in diccionario_informacion.items():
            row = table.add_row().cells
            row[0].text = key
            row[1].text = str(value)
