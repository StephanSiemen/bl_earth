
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


def draw_collector_item(self, context):
    row = self.layout.row()
    row.operator(operators.OBJECT_OT_creator_earth.bl_idname)

def register():
    bpy.utils.register_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.register_class(panels.BlEarth_UI_PT_panel)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.append(draw_collector_item)

def unregister():
    bpy.utils.unregister_class(operators.OBJECT_OT_creator_earth)
    bpy.utils.unregister_class(panels.BlEarth_UI_PT_panel)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.remove(draw_collector_item)

#
#  blender --background --python __init__.py -noaudio -E 'CYCLES' -f 1 -F 'PNG'
#
if __name__ == "__main__":
    operators.render_scene()
