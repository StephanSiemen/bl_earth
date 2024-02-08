#!/usr/bin/env python3
import bpy
from bpy.props import StringProperty

from bl_earth import operators
from bl_earth import data



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
        col.label(text="Select data set")
        col.operator(operators.OBJECT_OT_file_path.bl_idname, text="Select file ...")
