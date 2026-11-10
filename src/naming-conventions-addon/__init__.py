'''
License:
Copyright:
'''

bl_info = {
    "name": "naming-conventions"
    "blender": (5, 2, 3),
    "category": "Pipeline", "User Interface"
}

# Import modules
import bpy
import bpy.app.handlers
from bpy.app.handlers import persistent

# Define the persistent functions needed for extension
@persistent
def foo_startup_function():
def foo_preferences_functions():

# Needed for creating functions in __init__.py
# Define the register function
def register():
    print("Loading extension functions!")

# Define the unregister function
def unregister():
    print("Unloading extension functions!")
