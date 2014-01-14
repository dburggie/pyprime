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
    
    print 'Generating Coordinates of Primes...'
    prime_index = 0
    dx = 1
    dy = 0
    stepmax = 1
    stepcount = 0
    turncount = 0
    
    if width % 2 == 0:
        x = width / 2 - 1
    else:
        x = width / 2
    y = height / 2
    
    coordinates = [(0,0), (x,y)]
    
    i = 2
    while i < max_value:
        
        x += dx
        y += dy
        coordinates.append( (x,y) )
        
        # rotate direction?
        stepcount += 1
        if stepcount == stepmax:
            stepcount = 0
            turncount += 1
            if turncount == 2:
                turncount = 0
                stepmax += 1
            t = dx
            dx = dy
            dy = -t
        
        i += 1
    
    
    
    print 'Drawing Primes...'
    prime_index = 0
    next_prime = primes[prime_index]
    final_prime = primes[-1]
    i = 1
    while i < max_value:
        c = coordinates[i]
        x = c[0]
        y = c[1]
        if i == next_prime:
            if not next_prime == final_prime:
                prime_index += 1
                next_prime = primes[prime_index]
            image.set_pixel(x,y,_prime)
        else:
            image.set_pixel(x,y,_composite)
        i += 1
    
    print 'Writing to Disk...'
    image.write(filename)
    print 'All Done!'
    




