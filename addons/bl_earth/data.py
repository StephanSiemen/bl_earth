import sys
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    """Read data through cfgrib."""
    print("Python:  ", sys.executable)
    print("  path:  ", sys.path)
    print("NumPy:   ", np.__version__)
    print("xarray:  ", xr.__version__)

    fc_data = dict()

    print("------------------- "+str(filename)+" ----------------")

    ds = xr.open_dataset(filename, engine="cfgrib")
    # ds = xr.open_mfdataset(filename, combine='nested', concat_dim='time',
    #                  engine='cfgrib',backend_kwargs={'indexpath': ''})

    #fc_data['ds'] = ds

    #a list with the variable names of your xarray.Dataset
    names = list(ds.data_vars)

    options = []

    for var in names:
        print(" --------- ",var)
        option_tuple = (f'OPT_{var}', f"{var} - {ds[var].attrs['long_name']} in {ds[var].attrs['units']}", f"{ds[var].attrs['long_name']} in {ds[var].attrs['units']}")
        options.append(option_tuple)

        print(f"Attributes of variable '{var}':", ds[var].attrs)

    for var_name, da in ds.data_vars.items():
       steps = dict()
       if 'step' in da.dims:
            for time in da.step:
                # Extract hour values for steps (in nanoseconds)
                fc_step = str((time.values / 3600000000000.).astype(int)).zfill(3)
                data_slice = da.sel(step=time)

                # Create the plot
                fig = plt.figure(frameon=False, figsize=(10, 6))
                plt.axis('off')
                plt.title('')
                data_slice.plot(cmap=plt.cm.coolwarm, add_colorbar=False)

                # Save the plot
                filename = f"/tmp/bl_earth_{var_name}_{fc_step}.png"
                plt.savefig(filename, dpi=300, bbox_inches='tight',transparent=True, pad_inches=0)
                
                steps[fc_step] = filename

            fc_data[var_name] = steps

        #  values = ds[var][i,:,:].values
        #  plt.imshow(values, interpolation='none')
  
    fc_data["options"] = options
    # print("*********************************")
    # print(fc_data)
    del ds
    # plt.close()   ### crashes Blender UI if not commented out
    return fc_data

#
#  python data.py file.grb
#
if __name__ == "__main__":
    read_data(sys.argv[1])
