#!/usr/bin/env python3
import bpy
from bpy_extras.io_utils import ImportHelper
from bl_earth import earth
from bl_earth import data

class OBJECT_OT_creator_earth(bpy.types.Operator):
    """Create collections based on objects types"""
    bl_idname = "object.bl_earth_creator"
    bl_label = "Create globe"

    clear_scene: bpy.props.BoolProperty(
                        name="Clear current scene?",
                        default=True)
    radius: bpy.props.FloatProperty(
                        name="Radius",
                        min=0.,  # prevent negative values
                        default=1000.)


    @classmethod
    def poll(cls, context):
        return True
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        render_scene(self.clear_scene)
        return {'FINISHED'}



class OBJECT_OT_file_path(bpy.types.Operator, ImportHelper):
    bl_idname = "blearth.invoke_file_chooser"
    bl_label = "Select file"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        data.read_data(self.filepath)
        return {'FINISHED'}



def render_scene(clear, filename=None):

    #clean scene
    if(clear):
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
