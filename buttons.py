from utils.drawing import draw_text_box
from utils.colors import color_dict_HSV

class Button:
    def __init__(self, text="Button", posX=0, posY=0, bgcolor=(255, 255, 255), textcolor=None, scale = 0.5) -> None:
        self.x_left   = posX
        self.y_top    = posY
        
        self.x_right  = None
        self.y_bottom = None

        self.text    = text

        self.bg_color = bgcolor

        if text in color_dict_HSV and not textcolor:
            self.fg_color = tuple(color_dict_HSV[text][1])
        elif textcolor:
            self.fg_color = textcolor
        else:
            self.fg_color = (0, 0, 0)
        
        self.scale = scale
        
        # Run blank to set the box limits
        self.show()

    def __str__(self) -> str:
        return f"Button({self.text} --> From : {self.x_left, self.y_top}  |  To : {self.x_right, self.y_bottom})"


    def show(self, frame = None):
        self.x_right, self.y_bottom = draw_text_box(
            frame       = frame,
            text        = self.text,
            origin      = (self.x_left, self.y_top),
            scale       = self.scale,
            boxcolor    = self.bg_color,
            textcolor   = self.fg_color
        )
        return (self.x_right, self.y_bottom)
    

    def isInside(self,x,y):
        return x in range(self.x_left, self.x_right) and y in range(self.y_top, self.y_bottom)

# (BL, TR)
'''
    (XL, YT)
             +-------------------+
             |                   |
             |       R E D       |
             |                   |
             +-------------------+ 
                                   (XR, YB)
 RED BOX = Dimestions = (50, 30)                                   
'''
