import bpy
import math
from bl_earth import earth

frame_text = None

# Function to add text 
def add_text(text, location, size):
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.object
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.align_x = 'RIGHT'
    text_obj.data.align_y = 'TOP'
    text_obj.data.body = 'Frame: 1'
    return text_obj

def recalculate_text(scene):
    global frame_text
    frame_text.data.body = 'Frame: ' + str(scene.frame_current)
    # print(scene.frame_current)

def render_scene(clear, radius=10., animate_globe=True):

    global frame_text

    #clean scene
    if(clear):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

    # Add Earth - in separate source file
    earth.draw_earth(radius)

    if animate_globe:
        bpy.context.object.rotation_euler = 0.0, 0.0, 0.0
        bpy.context.object.keyframe_insert('rotation_euler', frame=1)
        bpy.context.object.rotation_euler = 0.0, 0.0, -math.radians(360.0)
        bpy.context.object.keyframe_insert('rotation_euler', frame=250)

    # Add the Sun
    bpy.ops.object.light_add(
        type='SUN',
        radius=1,
        align='WORLD',
        location=(50, -10, 50),
        rotation=(math.radians(70.0), math.radians(7.0), math.radians(100.0)),
        scale=(1, 1, 1))
    bpy.context.object.data.energy = 8
    bpy.context.object.data.angle = 0

    # Add the camera
    bpy.ops.object.camera_add(
        enter_editmode=False,
        align='VIEW',
        location=(60, 0, 22),
        rotation=(math.radians(70.), 0, math.radians(90.)),
        scale=(1, 1, 1))
    bpy.context.scene.camera = bpy.context.object
    cam = bpy.context.object

    frame_text = add_text("Frame: 1", (-2., 2., -10.), 0.3)
    frame_text.parent = cam

    # bpy.context.space_data.shading.type = 'MATERIAL'

    bpy.app.handlers.frame_change_post.append(recalculate_text)




def render_layers(clear, radius, filename=None):
    texture_file = "/tmp/bl_earth_t2m_0.png"

    overlay = bpy.ops.mesh.primitive_uv_sphere_add(segments=180, ring_count=180, radius=radius)

    mat2 = bpy.data.materials.new(name="overlay")
    mat2.use_nodes = True

    bsdf2 = mat2.node_tree.nodes["Principled BSDF"]
    texImage2 = mat2.node_tree.nodes.new('ShaderNodeTexImage')
    texImage2.image = bpy.data.images.load(texture_file)
    mat2.node_tree.links.new(bsdf2.inputs['Base Color'], texImage2.outputs['Color'])
    mat2.node_tree.links.new(bsdf2.inputs['Alpha'], texImage2.outputs['Alpha'])

    ob2 = bpy.context.view_layer.objects.active

    # Assign it to object
    if ob2.data.materials:
        ob2.data.materials[0] = mat2
    else:
        ob2.data.materials.append(mat2)

    # enable transparency for eevee
    bpy.context.object.active_material.blend_method  = 'BLEND'
    bpy.context.object.active_material.shadow_method = 'CLIP'
