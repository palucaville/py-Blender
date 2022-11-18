
import bpy
import requests
import time
from datetime import datetime

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
    
    mat = newShader("Shader2", "diffuse", 0.1, 0.1, 0.1)
    obj.data.materials.append(mat)
    bpy.context.scene.collection.objects.link(obj)  

def draw_dt(k):
    
     # Getting the current date and time
    datt = datetime.now()
    dt =str(datt)
    print("Date and time is:", dt)
    font_curve2 = bpy.data.curves.new(type="FONT", name="dt")
    font_curve2.body = dt 
    obj2 = bpy.data.objects.new(name="Font Object2", object_data=font_curve2)
      
      # -- Set scale and location
    obj2.location = (0, k+0.5, 0.1) 
    obj2.scale = (0.5, 0.3, 0.3)
    
    bpy.context.scene.collection.objects.link(obj2)
    
def newMaterial(id):

    mat = bpy.data.materials.get(id)
    if mat is None:
        mat = bpy.data.materials.new(name=id)
    mat.use_nodes = True
    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()
    return mat

def newShader(id, type, r, g, b):

    mat = newMaterial(id)
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')
    if type == "diffuse":
        shader = nodes.new(type='ShaderNodeBsdfDiffuse')
        nodes["Diffuse BSDF"].inputs[0].default_value = (r, g, b, 1)
    elif type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 1
    elif type == "glossy":
        shader = nodes.new(type='ShaderNodeBsdfGlossy')
        nodes["Glossy BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glossy BSDF"].inputs[1].default_value = 0

    links.new(shader.outputs[0], output.inputs[0])

    return mat

#bpy.ops.object.delete(use_global=False)

#for k in range(4):

#k = 0   
#draw_BTC(k)
#draw_dt(k)


counter = 0

def run_10_times():
    global counter
    counter += 1
    draw_BTC(counter)
    draw_dt(counter)
    
    if counter == 10:
        return None
    return 10 #seconds

bpy.app.timers.register(run_10_times)



