from Objects.Plants.StreetLamp import StreetLamp
from Objects.Animals.Hoomin import Hoomin
from Objects.Ground.Concrete import Concrete

import sys
import cv2
import numpy as np

if __name__ == '__main__':
    # create world objects
    animal = Hoomin()
    plant = StreetLamp()
    ground = Concrete()

    # create paths to object images
    animal_img = cv2.imread("img/" + animal.get_name() + ".png", cv2.IMREAD_ANYCOLOR)
    plant_img = cv2.imread("img/" + plant.get_name() + ".png", cv2.IMREAD_ANYCOLOR)
    ground_img = cv2.imread("img/" + ground.get_name() + ".png", cv2.IMREAD_ANYCOLOR)

    # scale object images
    animal_img = cv2.resize(animal_img, (300, 300), interpolation=cv2.INTER_AREA)
    plant_img = cv2.resize(plant_img, (300, 300), interpolation=cv2.INTER_AREA)
    ground_img = cv2.resize(ground_img, (300, 300), interpolation=cv2.INTER_AREA)

    # join the different object images
    top_img = np.concatenate((plant_img, plant_img, animal_img, plant_img, plant_img), axis=1)
    bottom_img = np.concatenate((ground_img, ground_img, ground_img, ground_img, ground_img), axis=1)
    complete_img = np.concatenate((top_img, bottom_img), axis=0)

    # display world
    while True:
        cv2.imshow("skrrrrrt", complete_img)
        cv2.waitKey(0)
        sys.exit()

    cv2.destroyAllWindows()

