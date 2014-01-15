from pyprime import ulam
import time
import cProfile

print '\n\nTimestamp', time.time()
print '\n'

def run():
    ulam.run(1000,1000)

cProfile.run('run()')
