import cv2
from math import ceil

DEBUG = True

char_size = {
    'a': [18, 24], 'b': [19, 24], 'c': [18, 24], 
    'd': [18, 24], 'e': [18, 24], 'f': [12, 24], 
    'g': [18, 24], 'h': [18, 24], 'i': [ 8, 24], 
    'j': [11, 24], 'k': [18, 24], 'l': [ 8, 24], 
    'm': [30, 24], 'n': [19, 24], 'o': [19, 24], 
    'p': [19, 24], 'q': [19, 24], 'r': [15, 24], 
    's': [17, 24], 't': [13, 24], 'u': [19, 24], 
    'v': [17, 24], 'w': [22, 24], 'x': [17, 24],
    'y': [16, 24], 'z': [17, 24], 'A': [18, 24],
    'B': [21, 24], 'C': [21, 24], 'D': [22, 24], 
    'E': [21, 24], 'F': [21, 24], 'G': [21, 24], 
    'H': [22, 24], 'I': [ 8, 24], 'J': [14, 24], 
    'K': [21, 24], 'L': [19, 24], 'M': [24, 24], 
    'N': [22, 24], 'O': [22, 24], 'P': [22, 24],
    'Q': [22, 24], 'R': [22, 24], 'S': [21, 24], 
    'T': [16, 24], 'U': [22, 24], 'V': [18, 24], 
    'W': [24, 24], 'X': [20, 24], 'Y': [18, 24], 
    'Z': [20, 24]
}

char_width = {
    'a': 18, 'b': 19, 'c': 18,
    'd': 18, 'e': 18, 'f': 12,
    'g': 18, 'h': 18, 'i':  8,
    'j': 11, 'k': 18, 'l':  8,
    'm': 30, 'n': 19, 'o': 19,
    'p': 19, 'q': 19, 'r': 15,
    's': 17, 't': 13, 'u': 19,
    'v': 17, 'w': 22, 'x': 17,
    'y': 16, 'z': 17, 'A': 18,
    'B': 21, 'C': 21, 'D': 22,
    'E': 21, 'F': 21, 'G': 21,
    'H': 22, 'I':  8, 'J': 14,
    'K': 21, 'L': 19, 'M': 24,
    'N': 22, 'O': 22, 'P': 22,
    'Q': 22, 'R': 22, 'S': 21,
    'T': 16, 'U': 22, 'V': 18,
    'W': 24, 'X': 20, 'Y': 18,
    'Z': 20
}


def _box(frame, size=(10,10), origin=(0,0), boxcolor=(255,255,255)):
    origin = ceil(origin[0]), ceil(origin[1])
    conclusion = ceil(origin[0]+size[0]), ceil(origin[1]+size[1])
    
    if DEBUG :
        print("in _box") 
        print("\torigin :", origin)
        print("\tsize :", size)
        print("\tconclusion :", conclusion)

    cv2.rectangle(
        frame,
        origin,
        conclusion,
        boxcolor,
        -1,
        cv2.LINE_4
    )


def _text(frame, text, scale=1, origin=(0,0), textcolor=(0,0,0)):
    origin = ceil(origin[0]), ceil(origin[1]+22*scale)
    if DEBUG:
        print("in _text")
        print("\torigin :", origin)
        print("\tscale :", scale)
        print("\ttext :", text)

    cv2.putText(
        frame,
        text,
        origin,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        textcolor,
        1,
        cv2.LINE_AA
    )

# def draw_text_box(frame, text, scale=1, origin=(20,20), padding=12):
#     text_size = sum([char_width[_] for _ in text]), 22
#     padding*=scale

#     text_size = (text_size[0] + padding, text_size[1] + padding)

#     box_origin = (origin[0] + padding, origin[1] + padding)
#     txt_origin = (ceil(origin[0] + padding), ceil(origin[1] + padding))

#     _box(frame, text_size, box_origin)

#     _text(frame, text, scale, txt_origin)

def draw_text_box(frame, text, scale=1, origin=(20, 20), padding=8, textcolor=(0,0,0), boxcolor=(255,255,255)):
    padding*=scale
    text_size = sum([char_width[_] for _ in text]), 22

    text_size = (text_size[0]*scale+2*padding, text_size[1]*scale+2*padding)

    box_origin = origin
    txt_origin = origin[0]+padding, origin[1]+padding

    _box(frame, text_size, box_origin, boxcolor)
    _text(frame, text, scale, txt_origin, textcolor)

