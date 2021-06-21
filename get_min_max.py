import numpy as np
import math as m
import os
from stl import mesh

# get [min_x, max_x], [min_y, max_y], [min_z, max_z]
def get_min_max(test_mesh):
    points = np.concatenate((test_mesh.v0, test_mesh.v1, test_mesh.v2))
    min_x, max_x = min(points[:, 0]), max(points[:, 0])
    min_y, max_y = min(points[:, 1]), max(points[:, 1])
    min_z, max_z = min(points[:, 2]), max(points[:, 2])
    # print("x:", min_x, max_x)
    # print("y:", min_y, max_y)
    # print("z:", min_z, max_z)
    return min_x, max_x, min_y, max_y, min_z, max_z

def main():
    stl_dir = 'object_sample'
    stl_files = os.listdir(stl_dir)
    # print(stl_files)

    for stl_file in stl_files:
        stl_mesh = mesh.Mesh.from_file(os.path.join(stl_dir, stl_file))
        m = get_min_max(stl_mesh)
        print("{}| x:[{}, {}], y:[{}, {}], z:[{}, {}]".format(stl_file, m[0], m[1], m[2], m[3], m[4], m[5]))

if __name__ == '__main__':
    main()