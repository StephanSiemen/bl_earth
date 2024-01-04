#!/usr/bin/env python3
import bpy
from bpy.props import StringProperty

from bl_earth import operators



class OBJECT_OT_file_path(bpy.types.Operator):
    """Move Objects up or down by given offset"""
    bl_idname = "object.file_path"
    bl_label = "Select file"
    bl_options = {'REGISTER', 'UNDO'}

    data_file : StringProperty(
        name="Data File",
        description="Only ...",
        subtype="FILE_PATH")
    
    def execute(self, context):
        return {'FINISHED'}

class BlEarth_UI_PT_panel(bpy.types.Panel):
    bl_idname = "BLEARTH_PT_3Dview"
    bl_label = "Blender Earth"
    bl_category = "Blender Earth"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        col = self.layout.column()
        col.label(text="Base globe")
        col.operator(operators.OBJECT_OT_creator_earth.bl_idname, text="Create globe")
        col.separator()
        col.label(text="Blender overlays")
        col.operator(OBJECT_OT_file_path.bl_idname, text="Select file ...")
