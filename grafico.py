import numpy as np
import matplotlib.pyplot as plt
from elastic import Info
from matplotlib.collections import EventCollection

class Grafico:

    def crearGrafico(self, doc_count, key, filename, grafico):

        if (grafico == "Barra"):
            self.graficoDeBarras(key, doc_count, filename)

        if (grafico == "Torta"):
            self.graficoDeTorta(key, doc_count, filename)

        if (grafico == "Tiempo"):
            self.graficoEnElTiempo(key, doc_count, filename)




    def graficoDeBarras(self, bars, height, filename):
        # Make dataset:
        y_pos = np.arange(len(bars))

        # Create bars
        plt.barh(y_pos, height)

        # Create names on the x-axis
        plt.yticks(y_pos, bars)

        plt.savefig(f'./imagenes/{filename}', bbox_inches='tight')


    def graficoDeTorta(self, etiquetas, tamaño, filename):
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        labels = etiquetas
        data = tamaño
        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=180)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                  bbox=bbox_props, zorder=0, va="center")
        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)
        plt.savefig(f'./imagenes/{filename}', bbox_inches='tight')


    def graficoEnElTiempo(self, doc_count, key, filename):




            # Fixing random state for reproducibility
            np.random.seed(19680801)

            # create random data
            xdata1 = doc_count
            xdata2 = key

            # sort the data so it makes clean curves
            xdata1.sort()
            xdata2.sort()

            # create some y data points
            ##ydata1 = xdata1 ** 2
            ##ydata2 = 1 - xdata2 ** 3

            # plot the data
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.plot(xdata1, color='tab:blue')
            ax.plot(xdata2, color='tab:orange')

            # create the events marking the x data points
            xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
            xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

            # create the events marking the y data points
            #yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                                       orientation='vertical')
            #yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                                       orientation='vertical')

            # add the events to the axis
            ax.add_collection(xevents1)
            ax.add_collection(xevents2)
            #ax.add_collection(yevents1)
            #ax.add_collection(yevents2)

            # set the limits
            ax.set_xlim([0, 1])
            ax.set_ylim([0, 1])

            ax.set_title('line plot with data points')

            plt.savefig(f'./imagenes/{filename}', bbox_inches='tight')

            # display the plot
            #plt.show()
