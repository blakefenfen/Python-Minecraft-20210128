#4-3

#install
from mcpi.minecraft import Minecraft
from random import randrange
from time import sleep
mc = Minecraft.create()

#build
for i in range(10):
    #getPos
    x,y,z = mc.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        mc.setBlock(x,y,z,35,color)
        
#game-system

mc.postToChat("§f§l遊戲介紹:")
mc.postToChat("§f§l請用一把劍在平台上砍")
mc.postToChat("§f§l直到找到你的獵物!!") 

mc.player.setTilePos(x-5,y+2,z-5)

answer = randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = mc.getBlockWithData(h.pos)
        data = block.data
        
        if data == answer:
            mc.postToChat("§e§l恭喜你找到啦!")
            mc.postToChat("§a§l遊戲結束!!")
            mc.postToChat("§c§l場地將於10秒後清除!!")
            mc.setBlock(h.pos,57)
            sleep(10)
            mc.setBlocks(x,y,z,x-10,y,z-10,0)
            break
        
        elif data > answer:
            mc.postToChat("§c§l找錯了!!! 提示:正確答案的方塊ID比這個更小!")
        
        elif data < answer:
            mc.postToChat("§c§l找錯了!!! 提示:正確答案的方塊ID比這個更大!")