#4-4

#install
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

list2 = [[12,41,14],[35,73,86]]

#getID
myID = mc.getPlayerEntityId("NiceFlatYan")
x,y,z = mc.entity.getTilePos(myID)

startX = x

for i in list2:
    for j in i:
        
        mc.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1