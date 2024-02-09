from maze import Maze
from img import maze_to_img

size =  0
gen_img = ""

while(size <= 0):
  try:
    size = int(input("Enter maze size (n*n): "))
  except:
    continue

maze = Maze(size)

while(len(gen_img) <= 0 or gen_img.lower()[0] != "y" and gen_img.lower()[0] != "n"):
    gen_img = input("Generate image (Y/n)? ")
    
    if(len(gen_img) == 0):
      gen_img = "y"
      break

if(gen_img.lower()[0] == "y"):
    block_size = 0

    while block_size <= 0:
        block_size = int(input("Enter block size >=1: "))

    maze_img = maze_to_img(maze, block_size=block_size)
else:
    print(maze)