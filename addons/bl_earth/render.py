import bpy
import math
from bl_earth import earth


# Function to add text 
def add_text(text, location, size):
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.object
    text_obj.name = "Frame_Text"
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.align_x = 'RIGHT'
    text_obj.data.align_y = 'TOP'
    return text_obj

def recalculate_text(scene):
    # Find the text object by name
    text_obj = bpy.data.objects.get("Frame_Text")
    if text_obj and text_obj.type == 'FONT':
        # Update the text body with the current frame number
        text_obj.data.body = f'Frame: {scene.frame_current}'

def render_scene(clear, radius=10., animate_globe=True):

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


def create_material(name):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()

    tex_node = nodes.new(type='ShaderNodeTexImage')
    bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    output_node = nodes.new(type='ShaderNodeOutputMaterial')

    links = mat.node_tree.links
    links.new(tex_node.outputs['Color'], bsdf_node.inputs['Base Color'])
    links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

    return mat, tex_node


def render_layers(clear, radius, layers):
    print("******************** render layers *******************")

    material, texture_node = create_material("Animated_Material")

    for n, step in enumerate(layers['t2m']):
        print("---> Step: ", step, " Frame: ", n*5)
        print("---> Texture file: ", layers['t2m'][step])

        frame = n*5

        texture_node.image = bpy.data.images.load(layers['t2m'][step])
        texture_node.image_user.frame_duration = 1
        texture_node.image_user.frame_start = frame
        texture_node.image_user.frame_offset = 0
        texture_node.image_user.use_auto_refresh = True
        texture_node.image_user.keyframe_insert("frame_offset", frame=frame)


    overlay = bpy.ops.mesh.primitive_uv_sphere_add(segments=180, ring_count=180, radius=radius)
    obj = bpy.context.view_layer.objects.active

    # Assign it to object
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

    # enable transparency for eevee
    # bpy.context.object.active_material.blend_method  = 'BLEND'
    # bpy.context.object.active_material.shadow_method = 'CLIP'
