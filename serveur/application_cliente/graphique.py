import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from donnees import getTemp

class Graphique:
    def __init__(self, tempLondre, tempParis):
        self.tempLondre = tempLondre
        self.tempParis = tempParis
    
    def dessiner(self):
        
        n_groups = 12

        means_men = self.tempLondre


        means_women = self.tempParis
    

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, means_men, bar_width,
                        alpha=opacity, color='b',
                        #yerr=std_men, error_kw=error_config,
                        label='Londres')

        rects2 = ax.bar(index + bar_width, means_women, bar_width,
                        alpha=opacity, color='r',
                        #yerr=std_women, error_kw=error_config,
                        label='Paris')

        ax.set_xlabel('relevé')
        ax.set_ylabel('Température')
        ax.set_title('Temperature par ville')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('', '', '', '', ''))
        ax.legend()

        fig.tight_layout()
        plt.show()


data = getTemp()
GraphiqueTemp = Graphique(data["Londres"], data["Paris"])
GraphiqueTemp.dessiner()

