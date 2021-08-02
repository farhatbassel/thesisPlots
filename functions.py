import numpy as np

#  THIS CLASS IS MADE FOR THE DATA PLOTS
class data:
    
    def __init__(self, data):
        self.data = data                              # Data should be outputed as np.loadtxt
        self.T = data[:, 0]                           # Time 
        self.M = data[:, 1]                           # Mass
        self.V_X = data[:, 2]                         # Velocity in the x direction 
        self.V_Y = data[:, 3]                         # Velocity in the y direction 
        self.V_Z = data[:, 4]                         # Velocity in the z direction 
        self.E_tot = data[:, 5]                       # Total energy
        self.E_K = data[:, 6]                         # Kinetic Energy
        self.B = data[:, 8]                           # Mag energy
        self.F = data[:, 10]                          # Density Fluctuations ** 2
        self.F = np.sqrt(self.F)                      # Density Fluctuations
        self.scaleFactor = data[:, 11]                # Scale Factor
        self.Z = 1 /self.scaleFactor + 1              # Redshift
        self.A_D = data[:, 12]                        # Drag Force
        self.X_e = data[:, 13]                        # X_e
        self.E_TH = self.E_tot - self.E_K - self.B    # Thermal energy 
        self.V_rms = np.sqrt(2*self.E_K/self.M)       # Calculating Vrms via E_K

    
