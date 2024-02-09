from PIL import Image
from datetime import datetime
import numpy as np

def maze_to_img(maze, path='./', name=None, outline=0, line=255, block_size=10):
    if(name is None):
        name = "maze-" + str(datetime.now()).replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
        
    lateral_length = block_size
    vertical_length = block_size

    img_arr = np.empty(shape=(maze.size * 3 * lateral_length, maze.size * 3 * vertical_length))

    for j in range(0, maze.size * 3, 3):
        layer1 = []
        layer2 = []
        layer3 = []

        for i in range(0, len(maze.maze)):
            if(not maze.maze[i][j // 3].connections['up']):
                layer1 += [outline, outline, outline] * lateral_length
            else:
                layer1 += [outline] * lateral_length + [line] * lateral_length + [outline] * lateral_length 

            if(not maze.maze[i][j // 3].connections['left']):
                layer2 += [outline] * lateral_length
            else:
                layer2 += [line] * lateral_length

            layer2 += [line] * lateral_length

            if(not maze.maze[i][j // 3].connections['right']):
                layer2 += [outline] * lateral_length
            else:
                layer2 += [line] * lateral_length

            if(not maze.maze[i][j // 3].connections['down']):
                layer3 += [outline, outline, outline] * lateral_length
            else:
                layer3 += [outline] * lateral_length + [line] * lateral_length + [outline] * lateral_length
        
        for k in range(j * vertical_length, min(j * vertical_length * 3, len(img_arr[0]))):
            img_arr[k] = layer1
        
        for k in range((j + 1) * vertical_length, min((j + 1) * vertical_length * 3, len(img_arr[0]))):
            img_arr[k] = layer2
        
        for k in range((j + 2) * vertical_length, min((j + 2) * vertical_length * 3, len(img_arr[0]))):
            img_arr[k] = layer3

    img = Image.fromarray(img_arr)

    if(img.mode != "RGB"):
        img = img.convert("RGB")

    img.save("./img/" + name + ".png")
    print("Image saved at ./img/" + name + ".png")

    return img_arr