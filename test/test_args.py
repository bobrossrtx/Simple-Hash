import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('radius', type=int, help='Radius of Cylinder')
parser.add_argument('height', type=int, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) *  (radius ** 2) * (height)
    return vol

if __name__ == '__main__':
    print(cylinder_volume(args.radius, args.height))