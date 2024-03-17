#listOfRandomStuff = ["car","water", "cat", "ice", "whale", "butterscotch", "yellow", "green" , "molecules" , "reptiles" , "milk" , "time" , "food" , "rain" , "oval"]
#print(listOfStuff)
#print(listOfStuff[6])
#print(min(listOfRandomStuff)) #min()looks for the letter farthers up the alphabet
#print(max(listOfRandomStuff)) #max()looks for the letter farthers down the alphabet

import simpleplot
import matplotlib
database1 = [(8,9) , (7,0) , (0,-5),(8,1),(9,6)]
database2 = [(-7,3) , (5,-3) , (-4,-5), (-2, 9) , (1,-9)]
simpleplot.plot_lines("Sample",400,300,"x","y",[database1,database2],True,["Dataset1","Dataset2"])