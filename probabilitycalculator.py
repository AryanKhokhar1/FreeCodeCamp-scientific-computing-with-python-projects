import copy
import random
# Consider using the modules imported above.

class Hat:
  # contents should be a list of strings containing one item for each ball
  # in the hat.
  def __init__(self, **kwargs):
    self.contents = list()
    self.__dict__.update(kwargs)
    # The arguments passed into the hat object upon creation should be
    # converted to a contents instance variable
    # Each item in the list should be a color name representing a single
    # ball of that color.
    # For example, if your hat is {"red": 2, "blue": 1}, contents should be
    # ["red", "red", "blue"].
    for key, value in kwargs.items():
      for i in range(kwargs[key]):
          self.contents.append(key)
  # The Hat class should have a draw method that accepts an argument
  # indicating the number of balls to draw from the hat.
  def draw(self,num_balls):
    new_list = list()
    # If the number of balls to draw exceeds the available quantity,
    # return all the balls.
    if num_balls>=len(self.contents):
      # Make a deep copy of the contents to a new list
      new_list = copy.deepcopy(self.contents)
      # Clear the contents as the whole list is returned
      self.contents.clear()
      # return the deep copy
      return new_list
    # This method should remove balls at random from contents and
    # return those balls as a list of strings.
    for i in range(num_balls):
      # randomly pick an item from the list
      n = random.choice(range(0,len(self.contents)))
      # append to the new_list that will be returned
      new_list.append(self.contents[n])
      # Since, this is a "without replacement copy", remove
      # that particular item from the contents
      self.contents.pop(n)
    # return the new_list
    return new_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # number of times the combination "expected_balls" will occur in
  # the complete set of experiments, initialize from 0
  count = 0
  for i in range(num_experiments):
    # In each iteration, make a deep copy of the 'hat' object
    hat_copy = copy.deepcopy(hat)
    # draw "num_balls_drawn" from the hat
    draw_balls = hat_copy.draw(num_balls_drawn)
    # Now to check, each ball and the number of times it occurs in
    # drawn set, initialize it to 0, e.g. {"red":2,"green":1}
    j = 0
    for key, val in expected_balls.items():
      # 'j' will only be incremented, if the drawn balls have
      # instance greater than or equal to the expected ball
      # e.g. if "red ball" are found in the list and their number
      # is greater than or equal to 2, and the "green ball" are found
      # in the drawn list and their number is equal to or greater than
      # 1, 'j' is incremented two times.
      if draw_balls.count(key)>=expected_balls[key]:
        j = j+1
    # Finally, if all the instances pass the conditions, it means
    # the drawn set has instances equal to or greater than the
    # expected ball in which case, we have found the combination,
    # so the count is incremented by 1
    if j==len(expected_balls):
      count = count+1
  return count/num_experiments