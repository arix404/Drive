
import heapq

def huffman(chars, freq):
    heap = []
    
    for i in range(len(chars)):
        heapq.heappush(heap, (freq[i], i, chars[i]))

    count = len(chars)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        node = (left, right)
        heapq.heappush(heap, (f1 + f2, count, node))
        count += 1

    def generate(node, code):
        if isinstance(node, str):
            print(node, ":", code)
            return

        left, right = node
        generate(left, code + "0")
        generate(right, code + "1")

    generate(heap[0][2], "")


chars = ['A', 'B', 'C', 'D', 'E']
freq = [5, 9, 12, 13, 16]

huffman(chars, freq)
