import os
import sys
import pathlib
import argparse
from random import randrange, choice
import shutil

item_count = 0

def RandomFolderName():
    names = ["up", "over", "down", "left", "right", "under", "jump", "into", "East", "West", "South", "North", "Out", "Crawl", "Run"]
    return choice(names).lower()

def DropItemsInFolder(path):
    global item_count
    items = [None,None,None,None, None,None,None,None,None,None, "Gold", "Art", "Trash", "Trash", "Trash"]

    selected = choice(items)
    if selected is not None:
        item_count += 1
        f = open(os.path.join(path,f"item-{item_count}.txt"), "w")
        f.write(selected)
        f.close()

def main(arguments):
    max_depth = 10
    basedir = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'maze')
    creator_queue = [(os.path.join(basedir,RandomFolderName()), 1) for _ in range(4)]

    while(len(creator_queue) != 0):
        path, depth = creator_queue.pop()

        if not os.path.exists(path):
            os.makedirs(path)
            DropItemsInFolder(path)

            if(depth < max_depth):
                directions = [(os.path.join(path,RandomFolderName()), depth+1) for _ in range(randrange(1,5))]
                creator_queue.extend(directions)
    
    shutil.make_archive(basedir, 'zip', basedir)
    shutil.rmtree(basedir) 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))