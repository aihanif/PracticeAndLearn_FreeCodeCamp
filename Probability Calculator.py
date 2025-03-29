import copy
import random

class Hat:
    def __init__(self, **balls):       
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def __repr__(self):
        return self.contents

    def __str__(self):       
        return self.contents

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]#will remain the same        
            self.contents.clear() # clear all ball
            return drawn_balls
        
        
        #random pick ball                
        drawn_balls = random.sample(self.contents, num_balls)
        
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_success=0

    for _ in range(num_experiments):
        copyhat = copy.deepcopy(hat)
        drawn_from_copy = copyhat.draw(num_balls_drawn)

        drawn_counts = {}
        for ball in drawn_from_copy:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1 #if ball not yet add, will set 0,if have same ball will plus 1

        #success = all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items())
        check_success=[]
        total_true = 0
        
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) >= count:
                check_success.append((color,'true'))
        #count the success
        if len(expected_balls.items()) == len(check_success):
            total_success+=1

       

    return total_success/num_experiments # probality of success


hat1 = Hat(red=2, blue=1)
print(hat1.contents)
print(hat1.draw(1))
hat2 = Hat(red=5, orange=4)
#print(hat2)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#print(hat3)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
              expected_balls={'red':2,'green':1},
              num_balls_drawn=5,
              num_experiments=2000)

print(f"probability - {probability:.3f}")