from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()


Grass2 = load_texture('grass2.png')
Rock = load_texture('rock.png')
Wall = load_texture('wall.png')
block = 1
count = 0
grid = []

for z in range(20):
    grid.append([])
    for x in range(20):
        chance = random.randint(0, 10)
        if chance < 8:
            grid[z].append(1)
        else:
            grid[z].append(0)


def get_cell_value(z, x):
    if z >= 0 and z < 19 and x >= 0 and x < 19:
        return grid[z][x]
    else:
        return 0


def run_rules():
    global grid
    temp = []
    for z in range(20):
        for x in range(20):
            cell_sum = sum([get_cell_value(z - 1, x),
                            get_cell_value(z - 1, x - 1),
                            get_cell_value(z, x - 1),
                            get_cell_value(z + 1, x - 1),
                            get_cell_value(z + 1, x),
                            get_cell_value(z + 1, x + 1),
                            get_cell_value(z, x + 1),
                            get_cell_value(z - 1, x + 1)])
            if grid[z][x] == 1:
                voxel = Voxel((x, 0, z), Grass2)
                voxel = Voxel((x, -1, z), Grass2)
            else:
                voxel = Voxel((x, -1, z), Grass2)
    grid = temp


def rock_rules():
    global grid
    temp = []
    for z in range(20):
        for x in range(20):
            cell_sum = sum([get_cell_value(z - 1, x),
                            get_cell_value(z - 1, x - 1),
                            get_cell_value(z, x - 1),
                            get_cell_value(z + 1, x - 1),
                            get_cell_value(z + 1, x),
                            get_cell_value(z + 1, x + 1),
                            get_cell_value(z, x + 1),
                            get_cell_value(z - 1, x + 1)])
            if grid[z][x] == 1:
                voxel = Voxel((x, 0, z), Grass2)
                voxel = Voxel((x, -1, z), Grass2)
            else:
                voxel = Voxel((x, -1, z), Grass2)
    grid = temp


def update():
    global block
    if held_keys['1']:
        block = 1
    if held_keys['2']:
        block = 2
    if held_keys['3']:
        block = 3


class Voxel(Button):
    def __init__(self, position=(-10, 0, -10), texture=Grass2):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxel = Voxel(self.position + mouse.normal, Grass2)
                if block == 2:
                    voxel = Voxel(self.position + mouse.normal, Wall)
                if block == 3:
                    voxel = Voxel(self.position + mouse.normal, Rock)
                # normal is the direction a surface is facing
            if key == 'left mouse down':
                destroy(self)


count = count + 1
if count < 3:
    run_rules()


player = FirstPersonController()


app.run()
