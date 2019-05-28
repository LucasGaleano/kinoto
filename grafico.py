import numpy as np
import matplotlib.pyplot as plt
from elastic import Info

class Grafico:

    def crearGraficoWebFilter(self):
        informacion = Info()
        response = informacion.infoWebFilter()
        # Make dataset:
        height = [x['doc_count'] for x in response]
        bars = [x['key'] for x in response]
        y_pos = np.arange(len(bars))

        # Create bars
        plt.barh(y_pos, height)

        # Create names on the x-axis
        plt.yticks(y_pos, bars)

        plt.savefig('./imagenes/graficoDeBarra.png', bbox_inches='tight')
