from math import floor


class getSmallest:
    arr = []
    size = 0

    def __init__(self, input_arr):
        self.arr = input_arr
        self.size = input_arr.__len__()
        for i in range(floor(self.size / 2), -1, -1):
            self.heapify(i)

    def get(self, x):
        for i in range(self.size - 1, x - 1, -1):
            self.exchange(0, i)
            self.size -= 1
            self.heapify(0)
        return self.arr[0]

    def heapify(self, index):
        left = self.left_index(index)
        right = self.right_index(index)
        largest = index

        if self.size > left and self.arr[left] > self.arr[largest]:
            largest = left
        if self.size > right and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.exchange(largest, index)
            self.heapify(largest)

    left_index = lambda self, index: index * 2 + 1

    right_index = lambda self, index: (index + 1) * 2

    def exchange(self, in1, in2):
        temp = self.arr[in1]
        self.arr[in1] = self.arr[in2]
        self.arr[in2] = temp


# test:
print(l := [1, 6, 4, -5, 2, 98, 90])
print(getSmallest(l).get(int(input("num: "))))
