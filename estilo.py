from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor

class Estilos:

    def definirEstilo(self, documento):
        styles = documento.styles
        self.estiloBTR(styles,'Title', 26, True, 255, 255, 255)
        self.estiloBTR(styles, 'Subtitle', 24, True, 255, 255, 255)
        self.estiloBTR(styles, 'Heading 1',20, False, 223,125, 14)
        self.estiloBTR(styles, 'Body Text', 14, False, 41, 39, 39)

    def estiloBTR (self, styles,nombreEstilo, pt, bold, r, g, b):
        try:
            styles[nombreEstilo].delete()
        except:
            pass
        finally:
            style = styles.add_style(nombreEstilo, WD_STYLE_TYPE.PARAGRAPH)
            font = style.font
            font.name = 'Lato Light'
            font.size = Pt(pt)
            font.bold = bold
            color = font.color
            color.rgb = RGBColor(r,g,b)
