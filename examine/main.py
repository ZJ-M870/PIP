import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# 加载点云数据
pcd = o3d.io.read_point_cloud("F:\\birmingham_block_2.ply")

# 预处理点云
voxel_size = 0.05
pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)

# 计算法向量
radius_normal = voxel_size * 5
pcd_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

# 应用聚类算法
labels_int_vector = pcd_down.cluster_dbscan(eps=voxel_size * 2, min_points=10, print_progress=True)
labels = np.array(labels_int_vector)  # 将 IntVector 转换为 NumPy 数组

# if labels.size == 0:
#     print("No clusters were found.")
# else:
#     # 获取点的数量
#     max_label = labels.max()
#     print(f"Point cloud has {max_label + 1} clusters.")
#
#     # 可视化聚类结果
#     colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
#     colors[labels < 0] = 0
#     pcd_down.colors = o3d.utility.Vector3dVector(colors[:, :3])

# 获取点的数量
max_label = labels.max()
print(f"Point cloud has {max_label + 1} clusters.")

# 可视化聚类结果
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
pcd_down.colors = o3d.utility.Vector3dVector(colors[:, :3])

# 创建Open3D可视化窗口
o3d.visualization.draw_geometries([pcd_down], window_name='Point Cloud with Clusters')

# 保存聚类后的点云文件
o3d.io.write_point_cloud("clustered_point_cloud.ply", pcd_down)