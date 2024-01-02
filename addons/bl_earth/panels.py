#!/usr/bin/env python3
import bpy
from bl_earth import operators

class BlEarth_UI_PT_panel(bpy.types.Panel):
    bl_idname = "BLEARTH_PT_3Dview"
    bl_label = "Blender Earth"
    bl_category = "BlEarth"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        col = self.layout.column()
        col.label(text="Blender Earth options", icon="INFO")
        col.operator(bpy.ops.object.delete.idname(), text='Burn baby ...')
        col.operator(operators.OBJECT_OT_creator_earth.bl_idname)
