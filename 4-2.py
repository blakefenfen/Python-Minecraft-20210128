#4-2

#install
from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

#getPos 
x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1,7)
    
    if r == 1 :
        mc.setBlocks(x,y,z,x,y,z+4, 41)
        z = z+4
    if r == 2:
        mc.setBlocks(x,y,z,x,y,z-4, 41)
        z = z-4
    if r == 3 :
        mc.setBlocks(x,y,z,x+4,y,z, 41)
        x = x+4
    if r == 4 :
        mc.setBlocks(x,y,z,x-4,y,z, 41)
        x = x-4
    if r == 5 :
        mc.setBlocks(x,y,z,x,y+4,z, 41)
        y = y+4
    if r == 6 :
        mc.setBlocks(x,y,z,x,y-4,z, 41)
        y = y-4