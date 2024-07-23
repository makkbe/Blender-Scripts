"""
Blender Batch OBJ Export Script

Author: Marcus Bengtsson
Version: 1.0
Copyright (c) 2024 Marcus Bengtsson

Description:
This script will iterate over all meshes in a Blender project and export each as an OBJ file,
using the name of the mesh as the name for the OBJ file. Has been tested with Blender 3.6.14
but may be both forwards and backwards compatible.

Usage:
Open or create a Blender project and go to the Scripting tab. Click the Open button, and locate the script.
Once you press the Run button, the script will put all OBJs inside a subdirectory called "objs" relative
to the directory where the Blender project file is saved.

Disclaimer:
This software is provided "as is", without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a particular
purpose and noninfringement. In no event shall the authors or copyright holders be liable
for any claim, damages or other liability, whether in an action of contract, tort or
otherwise, arising from, out of or in connection with the software or the use or other
dealings in the software.

Dependencies:
Blender. Duh.
"""
import bpy
import os

output_directory = bpy.path.abspath("//objs")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

bpy.ops.object.select_all(action='DESELECT')

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        filepath = os.path.join(output_directory, f"{obj.name}.obj")

        bpy.ops.export_scene.obj(
            filepath=filepath,
            use_selection=True,
            axis_forward='-Z',  # Adjust axis settings if needed
            axis_up='Y',
            use_materials=False
        )
        
        obj.select_set(False)

print("Export complete!")
