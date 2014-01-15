from pypng import Png
from primegen import primesByMaxValue

_background = [0,0,0]
_prime = [0,0,255]
_composite = [0,0,0]


def run(width, height, spiral_size = None, name = 'ulam'):
    
    if spiral_size == None:
        spiral_size = min(width, height)
    filename = name + '-{0}x{1}.png'.format(width, height)
    max_value = 1 + spiral_size ** 2
    
    print 'Generating Primes...'
    primes = primesByMaxValue(max_value)
    
    print 'Initializing Image...'
    image = Png(width, height)
    x = 0
    y = 0
    while y < height:
        while x < width:
            image.set_pixel(x,y, _background)
            x += 1
        x = 0
        y += 1
    y = 0
    
    print 'Drawing Primes...'
    if width % 2 == 0:
        x = width / 2 - 1
    else:
        x = width / 2
    y = height / 2
    
    i = 0
    p = primes[0]
    p_index = 0
    p_final = primes[-1]
    
    dx,dy = 1,0
    sc,sm,tc = 0,1,0
    
    while i < max_value:
        i += 1
        if i == p:
            image.set_pixel(x,y, _prime)
            if p != p_final:
                p_index += 1
                p = primes[p_index]
        else:
            image.set_pixel(x,y,_composite)
        x += dx
        y += dy
        sc += 1
        if sc == sm:
            # rotate direction
            t = dx
            dx = dy
            dy = -t
            # reset step count, increment turn count
            sc = 0
            tc += 1
            # increment length of next leg if we've turned twice
            if tc == 2:
                tc = 0
                sm += 1
        
    print 'Writing to Disk...'
    image.write(filename)
    print 'All Done!'
    




