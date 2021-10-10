import sys, itertools, time
from AlipThreading import*

def RuinsAnimated():
    for c in itertools.cycle(["ᛞ","ᚫ","ᛉ","ᚵ","ᛒ","ᛍ","ᛣ","ᛤ","ᛄ"]):
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t1 = thread_with_trace(target=RuinsAnimated)
t1.start()
time.sleep(5)
t1.kill()
t1.join()
