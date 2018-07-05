 
from atomsel import *
from molecule import *
import sys


wout=open('water.xyz', 'w')
nout=open('sodium.xyz', 'w')
cout=open('clor.xyz', 'w')
param=open('param.txt', 'w')
  
mol=load('gro','prd.gro')  # gro file
traject = 'traj.trr' #trajectory

read(mol,'trr',traject,waitfor=-1)
tot = atomsel('all')
water = atomsel('water')
sodium = atomsel('name NA')
clor = atomsel('name CL')
###oxygen = atomsel('resname OW')

Nframes = numframes(mol)

#SELECTION OF WATER
for n in range(Nframes):
  #wout.write("%i \n %i\n"%(len(water), n))
  water.frame=n
#  water.update()  if this line is not commented it updates the selection every frame. 
  xW = water.get('x')
  yW = water.get('y')
  zW = water.get('z')
  nameW = water.get('name')
	  
  for k in range(len(water)):
	wout.write("%s   %16.4f%16.4f%16.4f\n"%(nameW[k], xW[k], yW[k], zW[k]))

#SELECTION OF SODIUM
for n in range(Nframes):
  #nout.write("%i \n %i\n"%(len(sodium), n))
  sodium.frame=n
#  sodium.update()  if this line is not commented it updates the selection every frame. 
  xW = sodium.get('x')
  yW = sodium.get('y')
  zW = sodium.get('z')
  nameW = sodium.get('name')
	  
  for k in range(len(sodium)):
	nout.write("%s   %16.4f%16.4f%16.4f\n"%(nameW[k], xW[k], yW[k], zW[k]))

#SELECTION OF CLORHIDE
for n in range(Nframes):
  #cout.write("%i \n %i\n"%(len(clor), n))
  clor.frame=n
#  clor.update()  if this line is not commented it updates the selection every frame. 
  xW = clor.get('x')
  yW = clor.get('y')
  zW = clor.get('z')
  nameW = clor.get('name')
	  
  for k in range(len(clor)):
	cout.write("%s   %16.4f%16.4f%16.4f\n"%(nameW[k], xW[k], yW[k], zW[k]))

param.write('%i\n%i\n%i\n%i\n%i'%(Nframes, len(tot),len(water), len(sodium), len(clor)))

wout.close()
nout.close()
cout.close()
param.close()

sys.exit()
