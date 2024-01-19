import pyxel

class Game:

  rect_x = 0
  rect_y = 0

  def __init__(self):
    pyxel.init(300, 200, title='My Game') # размер окна, название игры
    pyxel.mouse(True) # реакция на мышь
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q): # при одном нажатии на кнопку S
      pyxel.quit() # выход из игры

    if pyxel.btn(pyxel.KEY_W):
      self.rect_y -= 1
    if pyxel.btn(pyxel.KEY_S):
      self.rect_y += 1

    if pyxel.btn(pyxel.KEY_A):
      self.rect_x -= 1
    if pyxel.btn(pyxel.KEY_D):
      self.rect_x += 1

  def draw(self):
    pyxel.cls(0) # очистка экрана
    pyxel.text(120, 100, "Hello Pyxel", pyxel.frame_count % 15) # надпись по адресу в пикселях, мигающая
    pyxel.rect(self.rect_x, self.rect_y, 20, 15, 14) # квадрат, отступы, размеры, цвет
    # pyxel.circ(100, 100, 15, 12) # круг, отступы, радиус, цвет)


if __name__ == "__main__":
  Game()