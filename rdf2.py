import numpy as np
import pandas as pd

water_df = pd.read_fwf('water.xyz', header=None, keep_default_na=False, names=['resname','x','y','z'])
na_df = pd.read_fwf('sodium.xyz', header=None, keep_default_na=False, names=['resname','x','y','z'])
cl_df = pd.read_fwf('clor.xyz', header=None, keep_default_na=False, names=['resname','x','y','z'])

#Creem un index per escollir els oxígens
water_df['resname'] = water_df['resname'].astype('category')
index = pd.CategoricalIndex(water_df['resname'])
pos_o = water_df[water_df.resname=='OW']

pos_w = water_df[['x','y','z']]
pos_na = na_df[['x','y','z']]
pos_cl = cl_df[['x','y','z']]
pos_o = pos_o[['x','y','z']]

np.savetxt('pos_w.txt',pos_w.values, fmt='%f', delimiter='\t', header='x\ty\tz')
np.savetxt('pos_na.txt',pos_na.values, fmt='%f', delimiter='\t', header='x\ty\tz')
np.savetxt('pos_cl.txt',pos_cl.values, fmt='%f', delimiter='\t', header='x\ty\tz')
np.savetxt('pos_o.txt',pos_o.values, fmt='%f', delimiter='\t', header='x\ty\tz')

print(pos_o.shape[0])
