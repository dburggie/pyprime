#!/usr/bin/python2
from pypng import Png
from primegen import primesByMaxValue


def run(width, height, color = [0,0,255], name = 'prime'):
    
    filename = name + '-{0}x{1}.png'.format(width, height)
    max_value = width * height
    
    print 'generating primes...'
    primes = primesByMaxValue(max_value)
    
    print 'Initializing image...'
    image = Png(width, height)
    for y in range(height):
        for x in range(width):
            image.set_pixel(x,y,[0,0,0])
    
    print 'Drawing primes...'
    for p in primes:
        y = p / width
        x = p % width
        image.set_pixel(x,y,color)
    
    print 'Writing to disk...'
    image.write(filename)
    print 'All Done!'
    
