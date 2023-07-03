import heapq

from src.app.huffman_node import HuffmanNode


class HuffmanAlgorithm:
    def __init__(self):
        self.codes = {}

    def build_huffman_tree(self, frequencies):
        heap = []
        for char, freq in frequencies.items():
            node = HuffmanNode(char=char, freq=freq)
            heapq.heappush(heap, node)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            parent = HuffmanNode(char=None, freq=left.freq +
                                 right.freq, left=left, right=right)
            heapq.heappush(heap, parent)

        return heap[0]

    def build_huffman_codes(self, node, code=''):
        if node.char:
            self.codes[node.char] = code
        else:
            self.build_huffman_codes(node.left, code + '0')
            self.build_huffman_codes(node.right, code + '1')

    def compress_text(self, text):
        compressed_text = ''
        for char in text:
            compressed_text += self.codes[char]
        return compressed_text

    def decompress_text(self, compressed_text, huffman_tree):
        decompressed_text = ''
        current_node = huffman_tree
        for bit in compressed_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char:
                decompressed_text += current_node.char
                current_node = huffman_tree

        return decompressed_text
