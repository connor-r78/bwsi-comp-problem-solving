import time

class SuperClass1:
  def info1(self):
    return "one used"

  def filler1(self):
    pass

  def filler2(self):
    pass

  def filler3(self):
    pass

class SuperClass2:
  def info2(self):
    return "two used"

class ChildClass(SuperClass1, SuperClass2):
  pass

child = ChildClass()

info1time = 0
info2time = 0

for i in range(1000):
  num = i % 2 + 1

  start = time.time()
  eval(f'child.info{num}()')
  end = time.time()
  
  elapsed = end - start

  exec(f'info{num}time += {elapsed}')

print(f'Average info1() time: {info1time / 500:.6f} seconds')
print(f'Average info2() time: {info2time / 500:.6f} seconds')
