import time
import threading

inters = input()

def tar(num):
    time.sleep(num)

inters = inters.split(' ')
thrs = []
for i in range(len(inters)):
    t = threading.Thread(target=tar, args = (int(inters[i]),))
    thrs.append(t)
for thr in thrs:
    thr.start()
for thr in thrs:
    thr.join()
print('42')