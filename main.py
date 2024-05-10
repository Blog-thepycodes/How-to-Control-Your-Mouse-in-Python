import time
from pynput.mouse import Controller, Button
from screeninfo import get_monitors
 
 
mouse = Controller()
 
 
def get_screen_center():
 
 
   monitor = get_monitors()[0]
   center_x = monitor.width // 2
   center_y = monitor.height // 2
   return center_x, center_y
 
 
def move_to_position(x, y, absolute=True):
   
   if absolute:
       mouse.position = (x, y)
   else:
       new_x, new_y = mouse.position
       mouse.position = (new_x + x, new_y + y)
 
 
def draw_letter(vertices):
 
 
   mouse.press(Button.left)  # Press the left mouse button
   for x, y in vertices:
       move_to_position(x, y, False)
       time.sleep(0.2)  # Delay for visibility
   mouse.release(Button.left)  # Release the left mouse button
   time.sleep(1)  # Pause between letters
 
 
def draw_p():
   vertices = [(0, -100), (50, 0), (0, 50), (-50, 0), (0, 150)]
   draw_letter(vertices)
 
 
def draw_y():
   vertices = [(-50, -100), (50, 100), (0, 0), (50, -100)]
   draw_letter(vertices)
 
 
def draw_c():
   vertices = [(50, 0), (0, -100), (-100, 0), (0, 100)]
   draw_letter(vertices)
 
 
def draw_o():
   vertices = [(0, -100), (50, 0), (0, 100), (-50, 0)]
   draw_letter(vertices)
 
 
def draw_d():
   vertices = [(0, -100), (50, 0), (0, 100), (-50, 0)]
   draw_letter(vertices)
 
 
def draw_e():
   vertices = [(0, -100), (100, 0), (0, 100), (-100, 0), (0, -50), (50, 0)]
   draw_letter(vertices)
 
 
def draw_s():
   vertices = [(0, -50), (50, 0), (0, -50), (-50, 0), (0, -50), (50, 0)]
   draw_letter(vertices)
 
 
def draw_word_pycodes():
   center_x, center_y = get_screen_center()
   initial_x = center_x - 300  # Adjust starting position to fit larger letters
   initial_y = center_y - 200
 
 
   move_to_position(initial_x, initial_y)  # Start position adjustment for the whole word
   draw_p()
   move_to_position(100, 0, False)  # Relative move to the next letter start
   draw_y()
   move_to_position(100, 0, False)
   draw_c()
   move_to_position(100, 0, False)
   draw_o()
   move_to_position(100, 0, False)
   draw_d()
   move_to_position(100, 0, False)
   draw_e()
   move_to_position(100, 0, False)
   draw_s()
 
 
def main():
   draw_word_pycodes()
 
 
if __name__ == "__main__":
   main()
