class myHeap:
    def __init__(self):
        self.heap=[]
    def heappush(self,val):
        if len(self.heap) == 0:
            self.heap.append(val)
        else:
            self.heap.append(val)
            self.heapup()

    def heappop(self,val):
        if len(self.heap) == 0:
            return -1
        else:
            val=self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapdown()
            return val

    def parentid(self,currentid):
        return (currentid-1) //2 if currentid >= 1 else -1
    def leftchild(self,currentid):
        return 2*currentid + 1 if 2*currentid + 1 < len(self.heap) else -1
    def rightchild(self,currentid):
        return 2*currentid + 2 if 2*currentid + 2 < len(self.heap) else -1

    def heapup(self,currentid):
        #move the last item up
        parentid = len()
        pid = self.parentid(currentid)
        if pid > 0 and self.heap[pid] > self.heap[currentid]:
            self.heap[pid],self.heap[currentid] = self.heap[currentid],self.heap[pid]
            self.heapup(pid)

    def heapdown(self,currentid):
        sid = self.leftchild(currentid)
        rid = self.rightchild(currentid)
        if self.h

