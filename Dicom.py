import numpy as np
import glob
import matplotlib.pyplot as plt
from pathlib import Path #working with file paths
import pydicom #working with dicom files

#Loading a single Dicom file
dicom_file = pydicom.read_file('/Users/pratham/Downloads/archive (14)/dicom_dir/ID_0000_AGE_0060_CONTRAST_1_CT.dcm')
#print(dicom_file)
print(dicom_file[0x0028,0x0010])
print(dicom_file.Rows)

ct = dicom_file.pixel_array
plt.figure()
plt.imshow(ct, cmap = 'gray')

#3D volume
path_to_head_mri = Path('/Users/pratham/Downloads/03-Data-Formats/SE000001/')
#accessing all files with a glob
all_files = list(path_to_head_mri.glob("*"))
print(all_files)

mri_data = []
for path in all_files:
    data = pydicom.read_file(path)
    mri_data.append(data)

#sorting the unordered data
mri_data_sorted = sorted(mri_data, key = lambda slice: slice.SliceLocation)
#Verifying if the data is sorted
for slice in mri_data_sorted[:5]:
    print(slice.SliceLocation)

#Extracting the actual data from dicom files
full_volume = []
for slice in mri_data_sorted:
    full_volume.append(slice.pixel_array)

#Visualizing
fig,axis = plt.subplots(3,3, figsize = (10,10))
slice_counter = 0
for i in range(3):
    for j in range(3):
        axis[i][j].imshow(full_volume[slice_counter], cmap = 'gray')
        slice_counter = slice_counter + 1


#Avoiding the above to code to order files with python library
import SimpleITK as sitk
series_ids = sitk.ImageSeriesReader.GetGDCMSeriesIDs(str(path_to_head_mri))
print(series_ids)

series_files_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(str(path_to_head_mri),series_ids[0])
print(series_files_names)
