
bl_info = {
    "name": "Blender Earth for model data",
    "author": "Stephan Siemen",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "description": "Blender addon to create a globe and overlay model data on it for animation",
    "location": "View3D",
    "warning": "Early version",
    "category": "Science",
    "License": "Apache",
    "doc_url": "https://bl_earh.readthedocs.io/en/docs/",
    "tracker_url": "https://github.com/StephanSiemen/bl_earth/issues/",
}

#import os
import bpy

import sys, site

user_site_pkgs = site.getusersitepackages()
if user_site_pkgs not in sys.path:
    sys.path.append(user_site_pkgs)

from bl_earth import earth
from bl_earth import panels
from bl_earth import operators
from bl_earth import render

def register():
    bpy.utils.register_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.register_class(operators.OBJECT_OT_file_path)
    bpy.utils.register_class(operators.OBJECT_OT_create_layer)
    bpy.utils.register_class(panels.BlEarth_UI_PT_panel)
    bpy.app.handlers.frame_change_post.append(render.recalculate_text)
    
def unregister():
    bpy.utils.unregister_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.unregister_class(operators.OBJECT_OT_file_path)
    bpy.utils.unregister_class(operators.OBJECT_OT_create_layer)
    bpy.utils.unregister_class(panels.BlEarth_UI_PT_panel)
    bpy.app.handlers.frame_change_post.remove(render.recalculate_text)

def run(filename):
    render.render_scene(True)
    # render.render_layers(False, 12, filename)

#
#  blender --background --python __init__.py -noaudio -E 'CYCLES' -f 1 -F 'PNG' -- data.grib
#
if __name__ == "__main__":
    run(sys.argv[-1])
