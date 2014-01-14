from pypng import Png
from primegen import primesByMaxValue

def run(width, height, name = 'cprime'):
    
    filename = name + '-{0}x{1}.png'.format(width, height)
    max_value = width * height
    
    print 'generating primes...'
    primes = primesByMaxValue(max_value)
    
    print 'Initializing image...'
    image = Png(width, height)
    for y in range(height):
        for x in range(width):
            image.set_pixel(x,y,[0,0,0])
    
    a = [[1,0,-1],[-1,1,0],[0,-1,1]]
    print 'Drawing primes...'
    for p in primes:
        y = p / width
        x = p % width
        
        d = int( (x * x + y * y) ** 0.5 )
        i = (d / 256) % 3
        
        r = (a[i][0] * d) % 256
        g = (a[i][1] * d) % 256
        b = (a[i][2] * d) % 256
        image.set_pixel(x,y,[r,g,b])
    
    print 'Writing to disk...'
    image.write(filename)
    print 'All Done!'
    
