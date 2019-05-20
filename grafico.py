from client import plt

class Grafico:

    def crearGraficoBarra(self):
        figura = plt.gcf()
        figura.savefig('./grafico.png', bbox_inches='tight')


