import numpy as np
import math as m
from stl import mesh

# scale [sx, sy, sz]
def scale(mesh, sxyz, file_name="scale_test.stl"):
    mesh.v0 *= np.array(sxyz)
    mesh.v1 *= np.array(sxyz)
    mesh.v2 *= np.array(sxyz)
    new_file_name = file_name[:-4] + '_s'+ str(sxyz[0]) + file_name[-4:]
    mesh.save(new_file_name)

# translate [dx, dy, dz]
def translate(mesh, dxyz, file_name="translate_test.stl"):
    mesh.translate(dxyz)

    distance = ''
    if dxyz[0] != 0:
        distance += '_dx'+str(dxyz[0])
    if dxyz[1] != 0:
        distance += '_dy'+str(dxyz[1])
    if dxyz[2] != 0:
        distance += '_dz'+str(dxyz[2])
    new_file_name = file_name[:-4] + distance + file_name[-4:]

    mesh.save(new_file_name)

# rotate th with [rx, ry, rz]
def rotate(mesh, rxyz, angle, file_name="rotate_test.stl"):
    mesh.rotate(rxyz, m.radians(angle))

    if rxyz[0] != 0:
        rotation = '_rx_'
    elif rxyz[1] != 0:
        rotation = '_ry_'
    elif rxyz[2] != 0:
        rotation = '_rz_'
    else:
        rotation = ''
    rotation += str(angle)
    new_file_name = file_name[:-4] + rotation + file_name[-4:]

    mesh.save(new_file_name)

def main():
    file_name = 'mayonnaise.stl'
    my_mesh = mesh.Mesh.from_file(file_name)
    scale(my_mesh, [0.5, 0.5, 0.5], file_name)
    translate(my_mesh, [0, 0, 0.1], file_name)
    rotate(my_mesh, [0, 0, 1], 90, file_name)

if __name__ == '__main__':
    main()
