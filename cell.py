from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')
        line= Line(Point(x1, y2), Point(x2, y2))
        if self.has_bot_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')

    def draw_move(self, to_cell, undo=False):
        center1 = Point(((self._x1 + self._x2) / 2), ((self._y1 + self._y2) / 2))
        center2 = Point(((to_cell._x1 + to_cell._x2) / 2), ((to_cell._y1 + to_cell._y2) / 2))
        line = Line(center1, center2)
        if not undo:
            self._win.draw_line(line, 'red')
        else:
            self._win.draw_line(line, 'gray')
        