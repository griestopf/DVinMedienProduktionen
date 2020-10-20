import bpy

for i in range(5):
    bpy.ops.mesh.extrude_region_shrink_fatten(
        MESH_OT_extrude_region={"mirror":False},
        TRANSFORM_OT_shrink_fatten={
            "value":0.5,
            "use_even_offset":False,
            "mirror":False} )
    bpy.ops.transform.resize(
        value=(0.777742, 0.777742, 0.777742), 
        orient_type='LOCAL')
    bpy.ops.transform.rotate(
        value=0.220425,
        orient_axis='Z',
        orient_type='LOCAL')
