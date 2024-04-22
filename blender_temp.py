RES_X = 25
RES_Y = 25
NAME = 'cube'


import os
import bpy
from math import *
from mathutils import Vector
from mathutils import noise

def get_rot(loc):
    loc = loc.normalized()
    x = loc[0]
    y = loc[1]
    z = loc[2]
    x_ang = pi / 2 - atan2(z, sqrt(x ** 2 + y ** 2))
    z_ang = pi / 2 + atan2(y, x)
    return Vector([x_ang, 0, z_ang])


def set_loc_rot(obj, loc):
    obj.location = loc
    obj.rotation_euler = get_rot(loc)


def create_and_save_examples(N=1):
    cam = bpy.context.scene.camera
    csv_text = ''
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.resolution_x = RES_X
    bpy.context.scene.render.resolution_y = RES_Y
    dirpath = f'{os.path.dirname(bpy.data.filepath)}/{NAME}_{RES_X}x{RES_Y}'

    for i in range(N):
        v = noise.random_unit_vector()
        v[2] = abs(v[2])
        x, y, z = v
        set_loc_rot(cam, 10 * v)
        bpy.ops.render.render()
        filepath = f'{dirpath}/{i}.png'
        csv_text += f'{v[0]},{v[1]},{v[2]}\n'
        bpy.data.images['Render Result'].save_render(filepath)

    with open(f'{dirpath}/coords.csv', 'w') as file:
        file.write(csv_text)

create_and_save_examples(100)