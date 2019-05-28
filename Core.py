####### photodiode.py ######

# Import packages
import numpy as np
import nptdms as tdms
import pandas as pd
import matplotlib.pyplot as plt
import pickle


#def tdms_import(name_to_file,td_path,group_names=True):
    #name_to_file = tdms.TdmsFile(td_path)
    #print("file",name_to_file," loaded")
    #food_groups = food_tdms.groups()
    #print(food_groups)


photod_path = "Y:\\swc\\branco\\Sarah\\Analysis\\Mini-dataset\\TDMS\\photod.tdms"
photod_tdms = tdms.TdmsFile(photod_path,memmap_dir=None)
print("file loaded")
photo_groups=photod_tdms.groups()
print(photo_groups)



#Create dataframe
photvar = photod_tdms.group_channels("Photodiode")
print(photvar)
phot = photod_tdms.object('Photodiode', '0')
photreal = phot.data
print(photreal)
data=pd.DataFrame(photreal,columns = ['photodiode'])
print(data)


# Save in docs folder
with open("docs\photreal"+ ".pkl", "wb") as f:
    pickle._dump(photreal, f)


#make miniature plot
#data.iloc[17815000:17825000].plot()
#plt.savefig('output.png')

# C:/Users/olesens/PycharmProjects/Opto_analysis/docs/


######### arduino.py ###########
import nptdms as tdms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


ard_path = "Y:\\swc\\branco\\Sarah\\Analysis\\Mini-dataset\\TDMS\\ard.tdms"
ard_tdms = tdms.TdmsFile(ard_path,memmap_dir=None)
print("file loaded")
ard_groups=ard_tdms.groups()
print(ard_groups)


# Create dataframe
ardvar = ard_tdms.group_channels("Arduino_trigger_IN")
print(ardvar)
ard = ard_tdms.object('Arduino_trigger_IN', '0')
ardreal = ard.data
print(ardreal)
data=pd.DataFrame(ardreal,columns = ['laser'])
print(data)


# Save in docs folder
np.save('ardreal',ardreal)
#with open(r'docs\ardreal'+ ".pkl", "wb") as f:
   # pickle._dump(ardreal, f)


########### laser. py #############

import nptdms as tdms
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

laser_path = "Y:\\swc\\branco\\Sarah\\Analysis\\Mini-dataset\\TDMS\\laser.tdms"
laser_tdms = tdms.TdmsFile(laser_path,memmap_dir=None)
print("file loaded")
laser_groups=laser_tdms.groups()
print(laser_groups)


# Create dataframe
laservar = laser_tdms.group_channels("Laser_trigger_IN")
print(laservar)
las = laser_tdms.object('Laser_trigger_IN', '0')
lasreal = las.data
print(lasreal)
data=pd.DataFrame(lasreal,columns = ['laser'])
print(data)

store = HDFStore('store.h5')

store['data'] = df  # save it
store['df']  # load it

# Save in docs folder
np.save('docs\lasreal',lasreal)
#with open("docs\lasreal"+ ".pkl", "wb") as f:
#    pickle._dump(lasreal, f)



########### tdms.py ##########
laser_path = "Y:\\swc\\branco\\Sarah\\Analysis\\Mini-dataset\\TDMS\\laser.tdms"
laser_tdms = tdms.TdmsFile(laser_path,memmap_dir=None)
print("file loaded")
laser_groups=laser_tdms.groups()
print(laser_groups)

ard_path = "Y:\\swc\\branco\\Sarah\\Analysis\\Mini-dataset\\TDMS\\ard.tdms"
ard_tdms = tdms.TdmsFile(ard_path,memmap_dir=None)
print("file loaded")
ard_groups=ard_tdms.groups()
print(ard_groups)

####### dateframe.py ########
import pickle
import numpy as np

photodiode = open('docs/photreal.pkl', 'rb')
pho=pickle.load(photodiode)
print(pho)




laser = np.load('lasreal.npy')
arduino = np.load('ardreal.npy', allow_pickle=False)


#arduino = open('docs/ardreal.pkl', 'rb')
#ard=pickle.load(arduino)
#print(ard)