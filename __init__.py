
# Blender Earth Extension for model data visualization
# Extension metadata is now in blender_manifest.toml

import bpy
import sys
import site

# Ensure user site packages are available
user_site_pkgs = site.getusersitepackages()
if user_site_pkgs not in sys.path:
    sys.path.append(user_site_pkgs)

# Import modules from the extension directory
from . import earth
from . import panels
from . import operators
from . import render
from . import data

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
    layers = data.read_data(filename)
    render.render_layers(False, 12, layers)

#
#  blender --background --python __init__.py -noaudio -E 'CYCLES' -f 1 -F 'PNG' -- data.grib
#
if __name__ == "__main__":
    run(sys.argv[-1])
