import bpy
import math
from . import earth


# Function to add text 
def add_text(text, location, size):
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.object
    text_obj.name = "Text_FrameCounter"
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.align_x = 'RIGHT'
    text_obj.data.align_y = 'TOP'
    return text_obj

def recalculate_text(scene):
    # Find the text object by name
    text_obj = bpy.data.objects.get("Text_FrameCounter")
    if text_obj and text_obj.type == 'FONT':
        # Update the text body with the current frame number
        text_obj.data.body = f'Frame: {scene.frame_current}'

def render_scene(clear, radius=10., animate_globe=True):
    """
    Create an intial scene with the Earth and the Sun.

    :param clear: Clear the scene before rendering
    :param radius: Radius of the Earth
    :param animate_globe: Animate the globe rotation
    :return: None
    """

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
    bpy.app.handlers.frame_change_post.append(recalculate_text)


def create_material(name):
    """
    Create a new material with a texture node and a principled BSDF shader.

    :param name: Name of the material
    :return: Material and texture node
    """

    # Create a new material
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
    """
    Render the layers of read data variables on top of Earth with animated textures.
    
    :param clear: Clear the scene before rendering
    :param radius: Height of layer plus radius of the Earth
    :param layers: Dictionary with layer names and texture file paths
    :return: None
    """
    variable_name = 't2m' #layers['options'][layers['variable']][0]

    try:
        var_cl = bpy.data.collections['Layers']
    except KeyError:
        var_cl = bpy.data.collections.new("Layers")
        bpy.context.scene.collection.children.link(var_cl)

    print("******************** render layers *******************")

    material, texture_node = create_material("Animated_Material_"+variable_name)

    texture_file = layers[variable_name]['000']
    print(f"---> Texture file: {texture_file}")

    try:
        # Load the texture file
        texture_node.image = bpy.data.images.load(texture_file)
        texture_node.image.source = 'SEQUENCE'
    except Exception as e:
        print(f"Error loading texture file '{texture_file}': {e}")
        return

    # Insert keyframes for texture properties
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = len(layers[variable_name])

    for frame in range(scene.frame_start, scene.frame_end + 1):
        scene.frame_set(frame)
        texture_node.image_user.frame_offset = frame - 1
        texture_node.image_user.keyframe_insert(data_path="frame_offset", frame=frame)

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=180, 
        ring_count=180, 
        radius=radius, 
        location=(0, 0, 0), 
        scale=(1, 1, 1)
    )
    obj = bpy.context.view_layer.objects.active
    var_cl.objects.link(obj)
    bpy.data.collections["Collection"].objects.unlink(obj)
    obj.name = 'Layer ' + variable_name

    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

    # enable transparency for eevee
    #bpy.context.object.active_material.blend_method  = 'BLEND'
    #bpy.context.object.active_material.shadow_method = 'CLIP'
