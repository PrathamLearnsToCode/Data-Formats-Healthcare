import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib

brain_mri = nib.load("/Users/pratham/Downloads/03-Data-Formats/03-Preprocessing/IXI662-Guys-1120-T1.nii.gz")
brain_mri_data = brain_mri.get_fdata()
affine = brain_mri.affine
shape = brain_mri.shape
print(affine)
print(shape)
print(brain_mri.header.get_zooms()) #axial, coronal and sagittal
print(nib.aff2axcodes(affine))
#P - anterior to posterior(front to back) - Coronal
#S - Inferior to superior (bottom to top) - Axial
#R - Left to Right - Sagittal
fig, axis = plt.subplots(1,2)
axis[0].imshow(brain_mri_data[:, 30, :], cmap = "gray")
axis[1].imshow(brain_mri_data[:, 200, :], cmap = "gray")
#for Sagittal
fig, axis = plt.subplots(1,2)
axis[0].imshow(brain_mri_data[:,:, 20], cmap = "gray")
axis[1].imshow(brain_mri_data[:, :, 45], cmap = "gray")

#Voxel into physical coord first method
voxel_coordinates = np.array((0,0,0,1))
physical_coordinates = affine * voxel_coordinates
print(physical_coordinates)

#second method
voxel_coordinates_manual = np.array((0,0,0))
physical_coordinates_manual = affine[:3,:3] * voxel_coordinates_manual
physical_coordinates_manual = affine[:3,3] + physical_coordinates_manual
print(physical_coordinates_manual)

#Physical into voxel by inverse matrix
physical_coord = [-90.67985535, 102.82944489, -114.82378387, 1.]
inverse = (np.linalg.inv(affine) * physical_coord).round()
print(inverse)