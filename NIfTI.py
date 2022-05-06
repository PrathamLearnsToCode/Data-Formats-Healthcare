import dicom2nifti
import nibabel as nib
import matplotlib.pyplot as plt

path_to_dicom = '/Users/pratham/Downloads/03-Data-Formats/SE000001/'
dicom2nifti.convert_directory(path_to_dicom,".")
nifti = nib.load('201_t2w_tse.nii.gz')
print(nifti)
print(nifti.header["qoffset_x"])
print(nifti.shape)

image_array = nifti.get_fdata()

fig, axis = plt.subplots(3,3, figsize = (10,10))
slice_counter = 0
for i in range(3):
    for j in range(3):
        axis[i][j].imshow(image_array[:,:,slice_counter],cmap = "gray")
        slice_counter = slice_counter + 1

image_array_processed = image_array * (image_array>300)

plt.figure()
plt.imshow(image_array[:,:,13], cmap = "gray")
plt.figure()
plt.imshow(image_array_processed[:,:,13], cmap = "gray")
