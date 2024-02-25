import os
import bpy


def draw_earth_surface():
    """Render Earth surface by mapping material on globe."""
    tex_path = bpy.path.relpath(os.path.join(
        os.path.dirname(__file__), "textures/NASA Earth Textures/"))
    img_path = os.path.join(tex_path, "earth_color_10K.tif")
    top_path = os.path.join(tex_path, "topography_10k.png")

    img = bpy.data.images.load(
        img_path,
        check_existing=True)

    # Create a new material
    mat = bpy.data.materials.new(name="Earth Surface")
    # Use nodes
    mat.use_nodes = True

    bpy.context.active_object.data.materials.append(mat)
    bsdf = mat.node_tree.nodes["Principled BSDF"]

    img_node = mat.node_tree.nodes.new("ShaderNodeTexImage")
    img_node.image = img

    tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_image.image = bpy.data.images.load(top_path)
    tex_image.image.colorspace_settings.name = 'Non-Color'

    bump_shader = mat.node_tree.nodes.new('ShaderNodeBump')

    output = mat.node_tree.nodes["Material Output"]

    mat.node_tree.links.new(img_node.outputs["Color"], bsdf.inputs["Base Color"])
    mat.node_tree.links.new(output.inputs['Displacement'], bump_shader.outputs['Normal'])
    mat.node_tree.links.new(bump_shader.inputs['Normal'], tex_image.outputs['Color'])



def draw_earth(radius):
    """Create Earth with specified radius."""
    earth_cl = 0
    try:
        earth_cl = bpy.data.collections['Earth']
    except KeyError:
        earth_cl = bpy.data.collections.new("Earth")
        bpy.context.scene.collection.children.link(earth_cl)

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=16,
        ring_count=8,
        radius=radius,
        enter_editmode=False,
        align='WORLD',
        location=(0, 0, 0),
        scale=(1, 1, 1))
    earth_cl.objects.link(bpy.context.active_object)
    bpy.data.collections["Collection"].objects.unlink(bpy.context.active_object)
    bpy.context.active_object.name = 'Globe'

    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].quality = 6
    bpy.context.object.modifiers["Subdivision"].levels = 6
    bpy.context.object.modifiers["Subdivision"].render_levels = 6
    bpy.ops.object.modifier_apply(modifier="Subdivision")
    bpy.ops.object.shade_smooth()

    draw_earth_surface()
