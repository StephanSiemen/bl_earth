# bl_earth
Blender add-on to overlay model data on the globe

**bl_earth** is a [**Blender**](https://www.blender.org) Python addon to visualize global model data on top of a three-dimensional globe. Model data will be handle through **zarr** and theerfore can come in various formats, such as **netCDF** and **grib**.

#### Why bl_earth?

There have been many packages providing starting points to visualise model data in Blender. For example, BlenderNC already allowed the loading of NetCDF and GRIB data using xarray, but it still requires a bit of manual work. Also there are limited options to use the power of xarray and therfore a new approach was necessary ... 


Documentation
-------------

Learn more about *bl_earth* in the official documentation at ... COMING SOON!

Installation
------------

**bl_earth** is now a Blender extension! There are several ways to install it:

### Option 1: Install from Extension Platform (Recommended)
1. Open Blender 4.2 or later
2. Go to Edit > Preferences > Extensions
3. Search for "bl_earth" and install directly

### Option 2: Install from ZIP file
1. Download the latest release from GitHub
2. In Blender, go to Edit > Preferences > Extensions
3. Click "Install from Disk" and select the ZIP file
4. Enable the extension

### Option 3: Install from Source
Clone the repository and install dependencies:

``` bash
   git clone https://github.com/StephanSiemen/bl_earth
   cd bl_earth
```

Find your Blender Python executable:
``` bash
   blender -b --python-expr "import sys; print(sys.executable)"
   export BLENDER_PYTHON=<output path from above>
```

Install dependencies:
``` bash
   $BLENDER_PYTHON install_dependencies.py
```

Then in Blender:
1. Go to Edit > Preferences > Extensions
2. Click "Install from Disk" and navigate to the bl_earth directory
3. Enable the extension

Running bl_earth
----------------

- **Interactivly in Blender**

  After installing and enabling the **bl_earth** add-on, go to the Layout workspace (should be default) and activate the side menu in the main 3D view Editor by pressing 'N'. You should see a tab called "Blender Earth". If not please, please restep the add-on installation.

  After installing the extension, you can find the **bl_earth** menu on the sidebar by pressing 'N' in the 3D viewport:
  ![screenshot on blearth menu](docs/images/bl_earth_menu.png)

- **Command line and batch**

  Clone the [**bl_earth**](https://github.com/StephanSiemen/bl_earth) repo to where you want to run it, install the third-aprty dependencies and excute something like this 
  ``` bash
    blender --background --python bl_earth.py -noaudio -E 'CYCLES' -f 1 -F 'PNG' -- data/ecmwf_forecast.grib2 
  ```
  Where $BLENDER_PYTHON is pointing to the Python interpretor which comes with Blender (see above). To retrieve the example data set, run '$BLENDER_PYTHON retrieve_ecmwf_fc.py' in the 'data' folder.

Development
-----------

### Building the Extension
To create a distributable extension package:

``` bash
   python3 build_extension.py
```

This creates `dist/bl_earth-extension.zip` which can be installed in Blender.

### Migration from Add-on to Extension
This project has been migrated from a Blender add-on to a Blender extension. Key changes:

- **Manifest**: Uses `blender_manifest.toml` instead of `bl_info`
- **Structure**: Flattened directory structure (no more `addons/` subdirectory)
- **Installation**: Installed via Extensions preference panel
- **Dependencies**: Handled via separate installation script

Contributing
------------

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome. More information about contributing to bl_earth can be found at our [Contribution page](https://bl_earth.readthedocs.io/en/latest/contribute.html).

Use Github to:
- report bugs,
- suggest features,
- provide examples

Inspiration
-----------

This modeule was inspired by many other projects like 

- [blendernc](https://blendernc.readthedocs.io)


Acknowledgement
---------------

The used texture and topolgies orginate from NASA's Visible Earth and used according to [their usage policy](https://visibleearth.nasa.gov/image-use-policy). The files itself were provided as part of [this Blender Guru's YouTube tutorial](https://www.youtube.com/watch?v=0YZzHn0iz8U).

---

#### Authors
[@stephansiemen](https://github.com/stephansiemen)


#### Contributors
