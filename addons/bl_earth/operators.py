#!/usr/bin/env python3
import bpy
from bpy_extras.io_utils import ImportHelper
from bl_earth import data
from bl_earth import render

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
                        default=10.)


    @classmethod
    def poll(cls, context):
        return True
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        render.render_scene(self.clear_scene,self.radius)
        return {'FINISHED'}

class OBJECT_OT_create_layer(bpy.types.Operator):
    """Create data overlays on the globe"""
    bl_idname = "object.bl_earth_layer"
    bl_label = "Create layer"

    clear_scene: bpy.props.BoolProperty(
                        name="Clear current layers?",
                        default=False)
    radius: bpy.props.FloatProperty(
                        name="Height",
                        min=0.,  # prevent negative values
                        default=10.)


    @classmethod
    def poll(cls, context):
        return True
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        render.render_layers(self.clear_scene, self.radius)
        return {'FINISHED'}



class OBJECT_OT_file_path(bpy.types.Operator, ImportHelper):
    bl_idname = "blearth.invoke_file_chooser"
    bl_label = "Select file"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        data.read_data(self.filepath)
        return {'FINISHED'}
