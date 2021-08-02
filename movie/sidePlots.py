import numpy as np
import matplotlib.pyplot as plt
import functions as fn

plt.style.use('#/plot_style.txt')                   # Publication style we chose

file_location = '#'
data_file = fn.data(np.loadtxt(file_location+"#file"))
redshift = np.loadtxt('#')[:,1]

class MoviePlots():

    def __init__(self,F,B,Z,redshift):
        self.F = F[597:]                            # Removing early noise
        self.B = np.sqrt(2*dataFile.B)[597:]        # Mostly due to the ring-in phase
        self.Z = Z[597:]
        self.redshift = redshift

    
    def cut_to_z(self,index):                                                    # Cutting the data
        self.cut_until = np.where(np.floor(self.Z)==redshift[index])[0][0]       # Showing the evolution to a certain point 
        return self.cut_until                                                    # in redshift           
    
    def maximum_value(self, field):
        return str(max(field))[:5]
    
    def rms_value(self,field,index):
        return str(field[self.cut_to_z(index)])[:5]
            
    def plot_it(self):                                                           # Plotting the data using 
        fig, ax = plt.subplots(figsize = (9,6))                                  # the publication style
        ax.set_xlabel('Redshift z')
        ax.grid(ls = 'dotted', lw = 2, axis = 'y')
        ax.grid(ls= 'dashed', lw = 2, axis ='x')
        ax.set_xlim(300,4800)
        ax.set_ylim(10**-2,4)
        ax.loglog(self.cut_Z,self.cut_B,'r')
        ax.loglog(self.cut_Z,self.cut_F,'#800080')
        ax.set_xticks([300,700,1000,1500,3000,4800])
        ax.set_xticklabels(['300','700','1000','1500','3000','4800'])

    def draw_max_value(self,index):
        plt.figtext(x = 0.13, y = 0.82, c= 'r', s = r'$B_{max}$ = ' + self.rms_value(self.cut_B,index))          # Getting the maximum value
        plt.figtext(x = 0.13, y = 0.72, c='#800080', s = r'$D\rho_{max} = $' + self.rms_value(self.cut_F,index))      # until the redshift we reached
        
    def cutting_data(self):
        for index, _ in enumerate(self.redshift):
            self.cut_Z = self.Z[:self.cut_to_z(index)]
            self.cut_F = self.F[:self.cut_to_z(index)]
            self.cut_B = self.B[:self.cut_to_z(index)]

            self.plot_it()
            self.draw_max_value(index)
            plt.savefig('#/sidePlot%02d'%index)           #Saving the files so that we can add them to the movie

plot_it = MoviePlots(dataFile.F,dataFile.B,dataFile.Z,redshift)
MoviePlots.cutting_data(plot_it)

