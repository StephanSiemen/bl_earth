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

To use **bl_earth** you need to install not only the addon but also some third-party Python packages with the Blender Python interpretor. The latter is slightly more complicated, as you need to call the Blender's python command. To do so you need to know where Blender is installed (depends on your operating system and Blender version). One way to find out is to call this command if you have blender in your PATH:

``` bash
   blender -b --python-expr "import sys; print(sys.executable)"
```

When you know where your python interprtor is located (here an example on MacOS) you can install Python community packgages with

``` bash
   /Applications/Blender.app/Contents/Resources/4.0/python/bin/python3.10 -m pip install xarray
```

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

---

#### Authors
[@stephansiemen](https://github.com/stephansiemen)


#### Contributors
