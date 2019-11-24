# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:04:52 2019

@author: Rohan
"""

''' ----- To open a zipfile ----- '''
from zipfile import ZipFile
file_name = 'data.zip'
# opening the zip file in read me mode
with ZipFile(file_name, 'r') as zip:
  print('Extracting of the files now...Please wait...') 
  zip.extractall()
  print('Done extraction of files')

# To remove the file
!rm data.zip

# To remove folder
!rm -rf semantic_segmentation/

# To list the files in the present ditectory
!ls -l

# To display the present directory
!pwd

# To clone git repository
!git clone www...... ''' git link'''

# TO install pakages
pip install -q keras

# To display the hardware being used
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

# info on cpu
!cat /proc/cpuinfo

# info of memory being used
!cat /proc/meminfo
