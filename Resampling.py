import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import nibabel.processing

brain_mri = nib.load("/Users/pratham/Downloads/03-Data-Formats/03-Preprocessing/IXI662-Guys-1120-T1.nii.gz")
brain_mri_data = brain_mri.get_fdata()
print(brain_mri.shape)
print(brain_mri.header.get_zooms())

voxel_size = (2,2,2)
brain_mri_resized = nibabel.processing.conform(brain_mri,(128,128,100),voxel_size, orientation = "PSR")
brain_mri_resized_data = brain_mri_resized.get_fdata()
print(brain_mri_resized.shape)
print(brain_mri_resized.header.get_zooms())

fig,axis = plt.subplots(1,2)
axis[0].imshow(brain_mri_data[:,:,50], cmap = "gray")
axis[1].imshow(brain_mri_resized_data[:,:,50], cmap = "gray")

lung_ct = nib.load("/Users/pratham/Downloads/03-Data-Formats/03-Preprocessing/lung_043.nii.gz")
lung_ct_data = lung_ct.get_fdata()
lung_ct_data_standardized = lung_ct_data/3071

plt.figure()
plt.imshow(np.rot90(lung_ct_data_standardized[:,:,50]),cmap= "gray")

lung_ct_lung_window = np.clip(lung_ct_data, -1000, -500)
plt.figure()
plt.imshow(np.rot90(lung_ct_lung_window[:,:,50]),cmap = "bone")

lung_ct_soft_tissue_window = np.clip(lung_ct_data, -250, 250)
plt.figure()
plt.imshow(np.rot90(lung_ct_soft_tissue_window[:,:,50]),cmap = "bone")


cardiac_mri = nib.load("/Users/pratham/Downloads/03-Data-Formats/03-Preprocessing/la_003.nii.gz")
cardiac_mri_data = cardiac_mri.get_fdata()
mean, std = np.mean(cardiac_mri_data), np.std(cardiac_mri_data)
cardiac_mri_norm = (cardiac_mri_data - mean)/std
cardiac_mri_standard = (cardiac_mri_norm - np.min(cardiac_mri_norm))/(np.max(cardiac_mri_norm)- np.min(cardiac_mri_norm))
print(np.mean(cardiac_mri_standard))
print(np.min(cardiac_mri_standard))
print(np.max(cardiac_mri_standard))

plt.figure()
plt.imshow(cardiac_mri_standard[:,:,30], cmap = "gray")