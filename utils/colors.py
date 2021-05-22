from numpy import array

'''
The entire purpose of this file is to 
store the color names and values, and
retrieve them whenever required using
special methods.
'''

# Create Annonymous Class
class __:
    _ = {
        'black'     : [[180, 255,  30], [  0,   0,   0]],
        'white'     : [[180,  18, 255], [  0,   0, 231]],
        'red1'      : [[180, 255, 255], [159,  50,  70]],
        'red2'      : [[  9, 255, 255], [  0,  50,  70]],
        'green'     : [[ 89, 255, 255], [ 36,  50,  70]],
        'blue'      : [[128, 255, 255], [ 90,  50,  70]],
        'yellow'    : [[ 35, 255, 255], [ 25,  50,  70]],
        'purple'    : [[158, 255, 255], [129,  50,  70]],
        'orange'    : [[ 24, 255, 255], [ 10,  50,  70]],
        'gray'      : [[180,  18, 230], [  0,   0,  40]]
    }

    def __getitem__(self, color):
        mycolor = self._.get(color)

        if mycolor:
            mycolor = array(mycolor[0]), array(mycolor[1])

        return mycolor
    
    def __iter__(self):
        return __Iterator(self)

    def get(self, val):
        return self.__getitem__(val)
    
    def __len__(self):
        return len(self._)


# Iterator Class
class __Iterator:
    def __init__(self, __):
       self._ = __
       self._index = 0

    def __next__(self):
        if self._index < len(self._):
            res = list(self._._)[self._index]
            self._index += 1
            return res
        else:
            raise StopIteration

# Actual Usable Object
color_dict_HSV = __()
