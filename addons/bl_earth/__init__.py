
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

from bl_earth import earth
from bl_earth import panels
from bl_earth import operators
from bl_earth import render

def register():
    bpy.utils.register_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.register_class(operators.OBJECT_OT_file_path)
    bpy.utils.register_class(operators.OBJECT_OT_create_layer)
    bpy.utils.register_class(panels.BlEarth_UI_PT_panel)
    
def unregister():
    bpy.utils.unregister_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.unregister_class(operators.OBJECT_OT_file_path)
    bpy.utils.unregister_class(operators.OBJECT_OT_create_layer)
    bpy.utils.unregister_class(panels.BlEarth_UI_PT_panel)

def run(filename):
    render.render_scene(True)
    render.render_layers(False, 12, filename)

#
#  blender --background --python __init__.py -noaudio -E 'CYCLES' -f 1 -F 'PNG'
#
if __name__ == "__main__":
    run(sys.argv[-1])
