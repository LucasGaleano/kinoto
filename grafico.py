import numpy as np
import matplotlib.pyplot as plt
from elastic import Info

class Grafico:

    def crearGrafico(self, height, bars, filename):

        # Make dataset:
        y_pos = np.arange(len(bars))

        # Create bars
        plt.barh(y_pos, height)

        # Create names on the x-axis
        plt.yticks(y_pos, bars)

        plt.savefig(f'./imagenes/{filename}', bbox_inches='tight')
