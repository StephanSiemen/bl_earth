#!/usr/bin/env python3
import bpy
from bpy_extras.io_utils import ImportHelper
from bl_earth import data
from bl_earth import render

class OBJECT_OT_creator_earth(bpy.types.Operator):
    """Create collections based on objects types"""
    bl_idname = "object.bl_earth_creator"
    bl_label = "Create globe"
    bl_options = {'REGISTER', 'UNDO'}

    clear_scene: bpy.props.BoolProperty(
                        name="Clear current scene?",
                        default=True)
    animate_globe : bpy.props.BoolProperty(
                        name="Rotate the globe?",
                        default=True) # type: ignore
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
        render.render_scene(self.clear_scene,self.radius,self.animate_globe)
        return {'FINISHED'}


#####################################################

variables = []

# def get_collections(self, context):
#     global variables
#     print("*********>>>>>>>>>>>>>>>>>>>>>" + str(variables))
#     return variables

class OBJECT_OT_create_layer(bpy.types.Operator):
    """Create data overlays on the globe"""
    bl_idname = "object.bl_earth_layer"
    bl_label = "Create layer"
    bl_options = {'REGISTER', 'UNDO'}
    
    clear_scene: bpy.props.BoolProperty(
                        name="Clear current layers?",
                        default=False)
    radius: bpy.props.FloatProperty(
                        name="Height",
                        min=0.,  # prevent negative values
                        default=10.)
    variable: bpy.props.EnumProperty(
                        name="Variable",
                        description="Choose a variable",
                        items=lambda self, context: variables['options']
                        # items={
                        #     ('OPT_tp', 'tp - Total precipitation in m', 'Total precipitation in m'),
                        #     ('OPT_t2m', 't2m - 2 metre temperature in K', '2 metre temperature in K')}
                            )

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        self.report({'INFO'}, f"bl_earth - Variable selected: {self.variable}")
        render.render_layers(self.clear_scene, self.radius, variables)
        return {'FINISHED'}


#####################################################

class OBJECT_OT_file_path(bpy.types.Operator, ImportHelper):
    bl_idname = "blearth.invoke_file_chooser"
    bl_label = "Select file"
    #bl_options = {'REGISTER', 'UNDO'}

    filter_glob:  bpy.props.StringProperty(
        default='*.grib;*.grb;*.grib2;*.nc',
        options={'HIDDEN'} )

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        global variables 
        variables = data.read_data(self.filepath)
        print(">>>>>>>>>>>" + self.filepath)
        print("*********************^^^^^^^^^^^^^^^^^^^^*22222" + str(variables))
        return {'FINISHED'}
