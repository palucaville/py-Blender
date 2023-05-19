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

import bpy
import requests # this is needed and usually NOT included in standard python
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
    bpy.context.scene.collection.objects.link(obj)  

def draw_dt(k):
    
# Getting the current date and time
    datt = datetime.now()
    dt =str(datt)
    #print("Date and time is:", dt) #debug print
    font_curve2 = bpy.data.curves.new(type="FONT", name="dt")
    font_curve2.body = dt 
    obj2 = bpy.data.objects.new(name="Font Object2", object_data=font_curve2)
  
# -- Set scale and location
    obj2.location = (0, k+0.5, 0.1) 
    obj2.scale = (0.5, 0.3, 0.3)
    bpy.context.scene.collection.objects.link(obj2)

counter = 5 # how many times to fetch

def run_n_times():
    global counter
    counter -= 1
    draw_BTC(counter)
    draw_dt(counter)
    
    if counter == 0:
        return None
    return 17 # fetch every this many seconds

bpy.app.timers.register(run_n_times)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.transform.translate(value=(7.1068, 0, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.object.select_all(action='DESELECT')




