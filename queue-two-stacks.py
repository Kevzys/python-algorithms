
class Queue(self):
    self.s1 = []
    self.s2 = []

    def enQueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
