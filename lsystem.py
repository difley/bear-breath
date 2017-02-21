import argparse
import math

def apply_rules(rules, initial_string, iterations):
    for iteration in range(iterations):
        initial_string = ''.join([rules[symbol] for symbol in initial_string])
    return initial_string

def str_to_coords(plotstr, angle,scale=1., angle0=0.):
    stack = []
    origin = [0., 0.]
    x,y = origin
    print('{x} {y}'.format(x=float(x), y=float(y)))
    for symbol in plotstr:
        if symbol == 'w':
            x += scale*math.cos(angle0)
            y += scale*math.sin(angle0)
            print('{x} {y}'.format(x=float(x), y=float(y)))
        elif symbol == "+":
            angle0 += angle
        elif symbol == "-":
            angle0 -= angle
        elif symbol == "[":
            stack.append([x, y, angle0])
            print('{x} {y}'.format(x=float(x), y=float(y)))
        elif symbol == "]":
            x, y, angle0 = stack.pop()
    return [x, y], angle0

def sierpinski(depth=12):
    angle = math.pi/3.
    rules = {'-': '-', '+': '+', 'a': 'b-a-b', 'b': 'a+b+a'}
    plotstr = apply_rules(rules, "a", depth)
    plotstr = plotstr.replace('a', 'w')
    plotstr = plotstr.replace('b', 'w')
    str_to_coords(plotstr, angle)

def dragon(depth=15):
    angle = math.pi/2.
    rules = {'x': 'x+yw+', 'y': '-wx-y', '+': '+', '-': '-', 'w': 'w'}
    plotstr = apply_rules(rules, 'x', depth)
    str_to_coords(plotstr, angle)

def island(depth=5):
    angle = math.pi/2.
    rules = {'w': 'w+w-w-www+w+w-w', '+': '+', '-': '-'}
    plotstr = apply_rules(rules, 'w+w+w+w', depth)
    str_to_coords(plotstr, angle)

def hilbert(depth=7):
    angle = math.pi/2.
    rules = {'x': '-yw+xwx+wy-', 'y': '+xw-ywy-wx+', 'w': 'w', '+': '+', '-': '-'}
    plotstr = apply_rules(rules, 'x', depth)
    str_to_coords(plotstr, angle)

def plant(depth=8):
    angle = 25.*math.pi/180.
    rules = {'x': 'w-[[x]+x]+w[+wx]-x', '-': '-', '+': '+', 'w': 'ww', '[': '[',
    ']': ']'}
    plotstr = apply_rules(rules, 'x', depth)
    str_to_coords(plotstr, angle, 1., math.pi/2.)

def carpet(depth=6):
    angle = math.pi/2.
    rules = {'w': 'ww+w+w+w+ww', '+': '+'}
    plotstr = apply_rules(rules, 'w+w+w+w', depth)
    str_to_coords(plotstr, angle)

def experiment(depth=15):
    angle = math.pi/2.
    rules = {'x': 'x+yw+', 'y': '-wy-x', 'w': 'w', '+': '+', '-': '-'}
    plotstr = apply_rules(rules, 'x', depth)
    str_to_coords(plotstr, angle)

def starstruck(depth=6, n=6):
    angle = math.pi/float(2)
    rules = {'w': 'w+w-w', '+': '+'.join('w'*n), '-': '-'.join('w'*n)}
    plotstr = apply_rules(rules, '+', depth)
    str_to_coords(plotstr, angle)

if __name__ == '__main__':
    fractal_dict = {
                    'starstruck': starstruck,
                    'experiment': experiment,
                    'carpet': carpet,
                    'plant': plant,
                    'hilbert': hilbert,
                    'island': island,
                    'dragon': dragon,
                    'sierpinski': sierpinski
                   }
    parser = argparse.ArgumentParser(description='Generate coordinates for specified fractals.')
    parser.add_argument('--fractal_name',
                        default='plant',
                        help='name of fractal',
                        choices=fractal_dict.keys())
    parser.add_argument('--depth', default=0, type=int, help='depth of fractal')
    args = parser.parse_args()
    if args.depth:
        fractal_dict[args.fractal_name](args.depth)
    else:
        fractal_dict[args.fractal_name]()
