bl_info = {
    "name": "Simple Matrix Extrude Add-on",
    "author" : "Prof. M.",
    "version" : (1, 0, 0),
    "blender" : (2, 90, 0),
    "description" : "Repeatedly extrude, move, scale and rotate selected faces",    
    "category": "Mesh",
    "support": "TESTING",
    "location" : "View 3D > Edit Mode > Mesh",
}

import bpy
import ptvsd
ptvsd.enable_attach()

    
class MatrixExtrudeSimple(bpy.types.Operator):
    bl_idname = "mesh.matrix_extrude_simple"
    bl_label = "Matrix Extrude selected faces five times"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
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

        return {'FINISHED'}

def register():
    print("Registering Matrix Extrude")
    bpy.utils.register_class(MatrixExtrudeSimple)

def unregister():
    print("Unregistering Matrix Extrude")
    bpy.utils.unregister_class(MatrixExtrudeSimple)