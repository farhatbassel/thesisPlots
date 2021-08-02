import yt
import numpy as np
import matplotlib.pyplot as plt
from yt import YTArray

ds = yt.load("#")

def density_fluc(field,data):
	mean_rho = np.mean(data['gas','density'])
	return (data['gas','density']-mean_rho)/mean_rho

ds.add_field(("gas","density_fluctuations"),units="dimensionless",function=density_fluc,display_name=r'$D\rho =\delta \rho / \bar{\rho}$')

factor = (np.sqrt(4*np.pi))
d = YTArray([factor],'gauss')
 
def mag_field(field,data):
	mag_field = data['gas','magnetic_field_magnitude']   
	return (data['gas','magnetic_field_magnitude']/d)

ds.add_field(('gas','magnetic_field_mag'),units='dimensionless',function=mag_field,display_name=r'$v_{A,rms}/c_s$')

s = YTArray([1],'cm/s')

def vel_field(field,data):
	vel_field = data['gas','velocity_magnitude']
	return (data['gas','velocity_magnitude']/s)

ds.add_field(('gas','vel_field'),units='dimensionless',function=vel_field,display_name=r'$v_{rms}/c_s$')

ad = ds.all_data()
field ='magnetic_field_mag'
redshift ='z = 3000     \n'
slc = yt.SlicePlot(ds, 'z', field)
slc.set_log(field, False)
slc.set_xlabel("x")
slc.set_ylabel("y")
#slc.set_zlim(field, -0.5, 2)
slc.set_font({'family':'serif','size':45})
slc.set_cbar_minorticks(field,"on")
slc.annotate_timestamp(corner='upper_left', time = False, redshift=True, draw_inset_box=True, redshift_format=redshift, inset_box_args={'alpha' : 0.25})
slc.annotate_text((0.02,0.86),r"$B_{rms} = 0.84$",coord_system='axis')
slc.set_window_size(12)

plot = slc.plots[field]
ax = plot.axes
slc._setup_plots()

ax.tick_params(axis = 'both', direction= 'out', length = 10,width = 3)
ax.set_xticks([-0.5,-0.25,0,0.25,0.5])
ax.set_xticklabels(['$-L_0$','$-L_0/2$','0','$L_0/2$','$L_0$'])
ax.set_yticks([-0.5,-0.25,0,0.25,0.5])
ax.set_yticklabels(['$-L_0$',r'$-L_0/2$','0',r'$L_0/2$','$L_0$'])
