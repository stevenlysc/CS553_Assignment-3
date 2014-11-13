
# coding: utf-8

import random

#character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#            '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=',
#            '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
             ]
filename = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
iteration_1 = [100, 100, 100, 100, 10, 1] #411 files
iteration_2 = [10, 100, 1000, 10000, 100000, 1000000] #file sizes: 1KB, 10 KB, 100KB, 1MB, 10MB, 100MB
for r in range(0, 6):
    for i in range(0, iteration_1[r]):
        a = str(random.choice(filename))
        for i in range(0, 9):
            a = a + str(random.choice(filename))
        a = a + '.txt'
        f = open('/Users/WayneHu/Desktop/gen_file/gen_file_1KB/'+ a, 'a')
        for i in range(0, iteration_2[r]):
            for i in range(0, 100):
                f.write(str(random.choice(character)))
            f.write('\n')
        f.close()
    f.close()
print "generation complete !"