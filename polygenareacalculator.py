class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width*2 + self.height*2

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = '*'*self.width + '\n'
        picture = line
        for i in range(1, self.height):
            picture += line
        return picture
    
    def get_amount_inside(self, shape):
        a, b = self.get_area(), shape.get_area()
        if a > b:
            return a // b
        return 0

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)
    
    def __str__(self):
        return f"Square(side={self.width})"