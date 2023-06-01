bl_info = {
    # required
    'name': 'fetchBTC',
    'blender': (2, 80, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 0),
    'author': 'Luca Mastrodicasa github.com/palucaville/',
    'description': 'Fetch current bitcoin price in US dollars',
}

import bpy# this is needed and usually NOT included in standard python
from mathutils import Color
import time
import random
from datetime import datetime


counter = 5 # CHANGE THIS - ow many times to fetch BTC price

def run_n_times():
    global counter
    counter -= 1
    #draw_BTC(counter)
    draw_dt(counter)
    if counter == 0:
        return None
    return 5 #  CHANGE THIS - fetch every THIS many seconds

def get_btc_current():
    try:
        btc_raw = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        btc = (btc_raw.json()['bpi']['USD']['rate'])
        return (btc)
    except requests.RequestException:
        print("Exception occurred: ")
        
def draw_BTC(k):
    btc_latest = get_btc_current()   
    font_curve = bpy.data.curves.new(type="FONT", name="btcDollar")
    font_curve.body = btc_latest 
    obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
      
      # -- Set scale and location
    obj.location = (0, k, 0.1) # move on the Z axis
    obj.scale = (0.75, 0.5, 0.5)
    bpy.context.scene.collection.objects.link(obj)  

def draw_dt(k):
    
    # Getting the current date and time
    datt = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    dt =str(datt)
    #print("Date and time is:", dt) #debug print
    font_curve2 = bpy.data.curves.new(type="FONT", name="dt")
    font_curve2.body = dt 
    obj2 = bpy.data.objects.new(name="Font Object2", object_data=font_curve2)
  
    # -- Set scale and location
    obj2.location = (0, k+0.5, 0.1) # change to a minus to go down
    obj2.scale = (0.5, 0.3, 0.3)
    bpy.context.scene.collection.objects.link(obj2)



def create_random_material():
    
    # Create a new material
    material = bpy.data.materials.new(name="Random Material")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    # Clear default nodes
    for node in nodes:
        nodes.remove(node)
    #  diffuse shader node
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    diffuse.location = (0, 0)
    output = nodes.new(type='ShaderNodeOutputMaterial')
    output.location = (200, 0)
    links = material.node_tree.links
    link = links.new(diffuse.outputs['BSDF'], output.inputs['Surface'])
    # random color for the diffuse node
    diffuse.inputs['Color'].default_value = [random.random() for _ in range(3)] + [1]  # RGBA format

    return material


# Get the active scene
scene = bpy.context.scene

bpy.app.timers.register(run_n_times)

bpy.ops.object.select_all(action='SELECT') 
# Create a random material
random_material = create_random_material()
selected_objects = bpy.context.selected_objects
# Assign the random material to all selected objects
for obj in selected_objects:
    if obj.type == 'FONT':
        if obj.data.materials:
            # If the object already has materials, replace the first one with the random material
            obj.data.materials[0] = random_material
        else:
            # If the object doesn't have any materials, create a new one and assign it
            obj.data.materials.append(random_material)
bpy.ops.transform.translate(value=(0, -1, -5))

# Update the view
bpy.context.view_layer.update()

bpy.ops.object.select_all(action='DESELECT')




