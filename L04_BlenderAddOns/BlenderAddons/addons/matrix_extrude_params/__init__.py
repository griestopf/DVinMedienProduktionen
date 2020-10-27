bl_info = {
    "name": "Advanced Matrix Extrude Add-on",
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

    
class MatrixExtrudeParams(bpy.types.Operator):
    bl_idname = "mesh.matrix_extrude_params"
    bl_label = "Matrix Extrude selected faces according to user settings"
    bl_options = {'REGISTER', 'UNDO'}


    segment_count = bpy.props.IntProperty(
        name="Segments",
        description="Number of segments to extrude",
        default=5,
        min=0,
        soft_max=30,
        )

    scale = bpy.props.FloatProperty(
        name="Scale",
        description="Scale value applied to the extruded face during each iteration",
        default=0.8,
        min=0.01,
        soft_max=2,       
    )

    angle = bpy.props.FloatProperty(
        name="Angle",
        description="Angle in degrees to rotate each face during each iteration",
        default=10,
        min=-80,
        max=80,       
    )

    def execute(self, context):
        for i in range(self.segment_count):
            bpy.ops.mesh.extrude_region_shrink_fatten(
                MESH_OT_extrude_region={"mirror":False},
                TRANSFORM_OT_shrink_fatten={
                    "value":0.5,
                    "use_even_offset":False,
                    "mirror":False} )
            bpy.ops.transform.resize(
                value=(self.scale, self.scale, self.scale), 
                orient_type='LOCAL')
            bpy.ops.transform.rotate(
                value=self.angle*3.141592/180.0,
                orient_axis='Z',
                orient_type='LOCAL')

        return {'FINISHED'}

def register():
    print("Registering Matrix Extrude")
    bpy.utils.register_class(MatrixExtrudeParams)

def unregister():
    print("Unregistering Matrix Extrude")
    bpy.utils.unregister_class(MatrixExtrudeParams)