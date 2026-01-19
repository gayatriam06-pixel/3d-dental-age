import trimesh
import numpy as np

def extract_features(stl_path):
    mesh = trimesh.load(stl_path)

    if not mesh.is_watertight:
        mesh = mesh.convex_hull

    volume = mesh.volume
    surface_area = mesh.area
    bbox_mean = mesh.bounding_box.extents.mean()
    face_count = len(mesh.faces)
    vertex_count = len(mesh.vertices)

    return np.array([
        volume,
        surface_area,
        bbox_mean,
        face_count,
        vertex_count
    ])