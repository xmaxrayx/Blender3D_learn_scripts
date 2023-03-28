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







class Extrude_plus_plus(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Select + +"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("my.extrude")
        pie.operator("")


def register():
    bpy.utils.register_class(Extrude_plus_plus)
    bpy.utils.register_class(MY_EXTRUDE)
    
def unregister():
    bpy.utils.unregister_class(Extrude_plus_plus)
    bpy.utils.register_class(MY_EXTRUDE)

if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="Extrude_plus_plus")
