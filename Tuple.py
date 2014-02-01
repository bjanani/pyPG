#A program to implement List using Queue#
import deque
queue = deque(["pendrive", "memory", "usb"])
queue.append("computer")           
queue.append("laptop")          
queue.popleft()         
'pendrive'
queue.popleft()                 
'memory'
queue                         
deque(['computer', 'laptop'])
print()

#A program to implement Dict using Queue#
class PriorityQueue():
 pq = PriorityQueue()
  firstDict = {'boy':'short', 'girl':'tall'}
  secondDict = {'man':'tall', 'woman':'short'}
  pq.put(secondDict,2)
  pq.put(firstDict, 1)
 while not pq.empty():
  print(dict['2'])
   for i in dict:
    print(i)

#A program to implement Tuple using Queue#
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()
q = Queue()
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()
for item in source():
    q.put(item)
q.join()   
