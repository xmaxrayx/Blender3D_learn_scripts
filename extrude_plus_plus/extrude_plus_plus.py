bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Menu, Operator

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)
# Idname should small
###############################################################################################
#extrude start
class MY_EXTRUDE(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "my.extrude"
    bl_label = "Extrude"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_move_normal()
        return {'FINISHED'}
#extrude end    

##################################################################################################
#extrude individual start
class MY_EXTRUDE_INDIVIDUAL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myextrude.individual"
    bl_label = "Extrude Individualy"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        #bpy.ops.mesh.extrude_faces_move()
        #bpy.ops.view3d.edit.mesh.extrude_faces_move()
        #bpy.ops.view3d.edit_mesh_extrude_manifold_normal()
        #bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten()
        return {'FINISHED'}
#extrude individual end

################################################################################################
#extrude along_normals start
class MY_EXTRUDE_ALONG_NORMALS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myextrude.along"
    bl_label = "Extrude Along Nromals"

    
    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten()
        return {'FINISHED'}
#extrude along_normals end

################################################################################################

#extrude manifold start                        @{

class MY_EXTRUDE_MANIFOLD(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myextrude.manifold"
    bl_label = "Extrude Manifold"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_manifold_normal()
        return {'FINISHED'}
#                                                            }@extrude manifold end

############################################################################################################

class Extrude_plus_plus(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Extrude + +"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("my.extrude")
        pie.operator("myextrude.individual")
        pie.operator("myextrude.manifold")
        pie.operator("myextrude.along")


def register():
    bpy.utils.register_class(Extrude_plus_plus)
    bpy.utils.register_class(MY_EXTRUDE)
    bpy.utils.register_class(MY_EXTRUDE_INDIVIDUAL)
    bpy.utils.register_class(MY_EXTRUDE_MANIFOLD)
    bpy.utils.register_class(MY_EXTRUDE_ALONG_NORMALS)
    
    
def unregister():
    bpy.utils.unregister_class(Extrude_plus_plus)
    bpy.utils.unregister_class(MY_EXTRUDE)
    bpy.utils.unregister_class(MY_EXTRUDE_INDIVIDUAL)
    bpy.utils.unregister_class(MY_EXTRUDE_MANIFOLD)
    bpy.utils.unregister_class(MY_EXTRUDE_ALONG_NORMALS)

if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="Extrude_plus_plus")
