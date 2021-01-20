import numpy as np
import matplotlib.pyplot as plt
import os


def increase_image_size(img_path, factor=64):
	backup_path = img_path[:-4] + "_backup.png"
	if os.path.isfile(backup_path):
		old_img = np.asarray(plt.imread(backup_path))
	else:
		old_img = np.asarray(plt.imread(img_path))
		plt.imsave(backup_path, old_img)
	old_img_size = old_img.shape
	new_img_size = np.array(old_img_size, dtype=int)
	new_img_size[:2] = factor*new_img_size[:2]
	new_img = np.zeros(new_img_size)
	for i in range(old_img_size[0]):
		for j in range(old_img_size[1]):
			for k in range(factor):
				for l in range(factor):
					new_img[i*factor+k, j*factor+l, :] = old_img[i, j, :]
	plt.imsave(img_path, new_img)
	

for tag_id in range(128):
	tag_id_str = str(tag_id)
	tag_model_dir_name = "tag36_11_" + (5-len(tag_id_str))*'0' + tag_id_str
	tag_png_file_name = tag_model_dir_name + ".png"
	png_file_path = os.path.abspath(os.path.join("..", "models", tag_model_dir_name, "materials", "textures", tag_png_file_name))
	if os.path.isfile(png_file_path):
		increase_image_size(png_file_path)
	


