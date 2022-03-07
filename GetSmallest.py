from math import ceil


class getSmallest:
    inlist = []
    size = 0
    half_size = 0

    def __init__(self, input_array):
        self.inlist = input_array
        self.size = self.inlist.__len__() - 1
        self.half_size = ceil(self.inlist.__len__() / 2)

    def get(self, x):
        for i in range(self.half_size, -1, -1):
            self.heapify(i, self.size)
        for i in range(self.size, x - 1, -1):
            #print(i)
            self.exchange(i, 0)
            self.size -= 1
            self.heapify(0, self.size)
        print(self.inlist)
        return self.inlist[0]

    def heapify(self, index, size):
        left = self.index_left(index)
        right = self.index_right(index)
        largest = index
        if size > left and self.inlist[left] > self.inlist[largest]:
            largest = left
        if size > right and self.inlist[right] > self.inlist[largest]:
            largest = right
        if largest != index:
            self.exchange(index, largest)
            self.heapify(largest, size)

    def index_left(self, x):
        return x * 2 + 1

    def index_right(self, x):
        return (x + 1) * 2

    def exchange(self, in1, in2):
        temp = self.inlist[in1]
        self.inlist[in1] = self.inlist[in2]
        self.inlist[in2] = temp


# test:
l = [1, 6, 4, -5, 2, 98, 0]
print(getSmallest(l).get(int(input("num: "))))
