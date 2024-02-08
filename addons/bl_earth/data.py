import sys
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    print("Python:  ", sys.executable)
    print("  path:  ", sys.path)
    print("NumPy:   ", np.__version__)
    print("xarray:  ", xr.__version__)

    animation = dict()

    print("------------------- "+str(filename)+" ----------------")

    ds = xr.open_dataset(filename, engine="cfgrib")
    # ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time',
    #                  engine='cfgrib',backend_kwargs={'indexpath': ''})

    #a list with the variable names of your xarray.Dataset
    names = list(ds.data_vars)

    for var in names:
      print(" --------- ",var)

    #   for i in range(5):
    #    print("    ... time: "+ds.time.dt.strftime("%B %d, %Y, %r"))
    #    fig = plt.figure(frameon=False, figsize=[12,8])
    #    ax = plt.Axes(fig, [0., 0., 1., 1.])
    #    ax.set_axis_off()
    #    fig.add_axes(ax)

    #   #  print(ds[var])
    #    values = ds[var][i,:,:].values
    #    plt.imshow(values, interpolation='none')
    #   #  var.plot()

    #    outfile = "bl_earth_"+var+"_"+str(i)+".png"
    #    fig.savefig(outfile,
    #                bbox_inches='tight',
    #                transparent=True, 
    #                pad_inches=0)
    #    plt.close(fig)

    #    animation[str(i)] = [outfile,var]

    # return animation

#
#  python data.py file.grb
#
if __name__ == "__main__":
    read_data(sys.argv[1])

