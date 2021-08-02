import numpy as np
import matplotlib.pyplot as plt
import functions as fn

plt.style.use('/home/bassel/Documents/Paper/plot_style.txt')

file_location = '/home/bassel/Documents/datFiles/scale_inv/512_v_a_3/'
dataFile = fn.data(np.loadtxt(file_location+"mag_dens_pert_512_3_scale_inv.dat"))
redshift = np.loadtxt('/home/bassel/Desktop/z.txt')[:,1]

class MoviePlots():

    def __init__(self,F,B,Z,redshift):
        self.F = F[597:]
        self.B = np.sqrt(2*dataFile.B)[597:-1]
        self.Z = Z[597:]
        self.redshift = redshift

    
    def cut_to_z(self,index):
        self.cut_until = np.where(np.floor(self.Z)==redshift[index])[0][0]
        return self.cut_until
    
    def maximum_value(self, field):
        return str(max(field))[:5]
            
    def plot_it(self):
        fig, ax = plt.subplots(figsize = (9,6))
        ax.set_xlabel('Redshift z')
        ax.grid(ls = 'dotted', lw = 2, axis = 'y')
        ax.grid(ls= 'dashed', lw = 2, axis ='x')
        ax.set_xlim(300,4800)
        ax.set_ylim(10**-2,4)
        ax.loglog(self.cut_Z,self.cut_B,'r')
        ax.loglog(self.cut_Z,self.cut_F,'#800080')
        ax.set_xticks([300,700,1000,1500,3000,4800])
        ax.set_xticklabels(['300','700','1000','1500','3000','4800'])

    def draw_max_value(self):
        plt.figtext(x = 0.575, y = 0.75, s = r'$B_{max}$ = ' + self.maximum_value(self.cut_B))    
        plt.figtext(x = 0.575, y = 0.34, s = r'$D\rho_{max} = $' + self.maximum_value(self.cut_F))
        
    def cutting_data(self):
        for index, _ in enumerate(self.redshift):
            self.cut_Z = self.Z[:self.cut_to_z(index)]
            self.cut_F = self.F[:self.cut_to_z(index)]
            self.cut_B = self.B[:self.cut_to_z(index)]

            self.plot_it()
            self.draw_max_value()
            plt.savefig('/home/bassel/scatterFiles/sidePlots/sidePlot%02d'%index)

plot_it = MoviePlots(dataFile.F,dataFile.B,dataFile.Z,redshift)
MoviePlots.cutting_data(plot_it)

