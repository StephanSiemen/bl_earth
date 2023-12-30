
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

class OBJECT_OT_creator_earth(bpy.types.Operator):
    """Create collections based on objects types"""
    bl_idname = "object.bl_earth_creator"
    bl_label = "Create globe with overlay"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        render_scene()

        return {'FINISHED'}

def render_scene():
    #clean scene
    #if(True):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Add Earth - in separate source file
    earth.draw_earth()

    # Add the Sun
    bpy.ops.object.light_add(
        type='SUN',
        radius=1,
        align='WORLD',
        location=(0, 60, 50),
        rotation=(1.0472, 1.5708, 2.61799),
        scale=(1, 1, 1))
    bpy.context.object.data.energy = 8
    bpy.context.object.data.angle = 0

    # Add the camera
    bpy.ops.object.camera_add(
        enter_editmode=False,
        align='VIEW',
        location=(100, 10, 10),
        rotation=(1.61169, -0.0422343, 1.71535),
        scale=(1, 1, 1))
    bpy.context.scene.camera = bpy.context.object


def draw_collector_item(self, context):
    row = self.layout.row()
    row.operator(OBJECT_OT_creator_earth.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_creator_earth)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.append(draw_collector_item)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_creator_earth)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.remove(draw_collector_item)

#
#  blender --background --python __init__.py -noaudio -E 'CYCLES' -f 1 -F 'PNG'
#
if __name__ == "__main__":
    render_scene()
