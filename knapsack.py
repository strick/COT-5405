global learningMode
global currentStep
global fp

fp = open("./demo.html", "w")
currentStep = 1
learningMode = True

import copy


# Problem: Knapsack - Bottom up
# Author: Brian Strickland
# Email: brian.strickland@ucf.edu

# Fills a "knapsack" with the most valuable items until the defined
# bag weight limit is reached.
#
# itemValues - array of  values for each item
# itemWeights - array of weights of each item
# NOTE:  The itemValues and itemWeights indexes must match
# bagWeightLimit - the weight limit of the bag 
#
# return - a bag full of the most valuable items
def fillKnapsack(itemValues, itemWeights, bagWeightLimit):

    # Create a 2D array big enough to hold all item sets and weight
    #bag = [[0]*bagWeightLimit]*len(itemValues)
    #[col][row]
    bag = [['' for i in range(bagWeightLimit+1)] for j in range(len(itemValues)+1)]

    # Look at each item provided
    for i in range(len(itemValues)+1):

        # Calculate the values for a given combination at that current weight.
        for w in range(bagWeightLimit+1):

            # For a sack of weight 0 or an empty set of items
            if i == 0 or  w == 0:
                bag[i][w] = 0
     
            # If the current item is able to be in the solution, check to see
            elif itemWeights[i-1] <= w:

                proposedValue = itemValues[i-1] + bag[i-1][w-itemWeights[i-1]]

                # Item belongs in the solution
                if(proposedValue > bag[i-1][w]):
                    bag[i][w] = proposedValue
                    printHtmlStep(bagWeightLimit, bag, itemValues, itemWeights,i,w, True, i-1)
                # The item does not belong in the solution
                else:
                    bag[i][w] = bag[i-1][w]
                    printHtmlStep(bagWeightLimit, bag, itemValues, itemWeights,i,w, False, i-1)

            # Item does not belong in the solution 
            else:
                bag[i][w] = bag[i-1][w]
                printHtmlStep(bagWeightLimit, bag, itemValues, itemWeights, i,w, False, i-1)

    return bag[len(itemValues)][bagWeightLimit]

def printHtmlStep(W, bag, values, weights, i,w_small, in_solution, previousI):
    global currentStep
    global fp

    fp.write("<h1>Step " + str(currentStep) + "</h1>")
    if(not(in_solution)):
        fp.write("<h2>Item does not belong in the solution</h2>")
        #bag[i][w] = bag[i-1][w]
    else:
        fp.write("<h2>Item added to the solution</h2>")
    
    fp.write("i=" + str(i) + "<br />")
    fp.write("v<sub>i</sub>=" + str(values[i-1]) + "<br />")
    fp.write("w<sub>i</sub>=" + str(weights[i-1]) + "<br />")
    fp.write("w=" + str(w_small) + "<br />")
    fp.write("w-w<sub>i</sub>=" + str(w_small-weights[i-1]) + "<br />")

    fp.write("<table width=\"300px\"><tr><td>")
    fp.write("<table width=\"225px\" border=\"1\"><tr>")
    
    fp.write("<td></td>")
    for row in range(W+1):
        fp.write("<td class=\"bold\">" + str(row) + "</td>")
    fp.write("</tr>")

    for row in range(len(values)+1):
        fp.write("<tr>")
        if(row == 0):
            fp.write("<td class=\"bold\">&Theta;</td>") 
        else:
            fp.write("<td class=\"bold\">" + str(row) + "</td>")
        for col in range(len(bag[row])):
            if(str(bag[row][col]) == ''):
                fp.write("<td>&nbsp;</td>")
            elif(not(in_solution) and row == previousI and col == w_small):
                fp.write("<td bgcolor=\"red\">" + str(bag[row][col]) + "</td>")
            elif(not(in_solution) and row == i and col == w_small):
                fp.write("<td bgcolor=\"red\">" + str(bag[row][col]) + "</td>") 
            elif(in_solution and row == previousI and col == w_small - weights[i-1]):
                fp.write("<td bgcolor=\"green\">" + str(bag[row][col]) + "</td>")
            elif(in_solution and row == i and col == w_small):
                fp.write("<td bgcolor=\"green\">" + str(bag[row][col]) + "</td>")
            else:
                fp.write("<td>" + str(bag[row][col]) + "</td>")
        fp.write("</tr>")

    fp.write("</table>")
    fp.write("</td>")
    fp.write("<td>")
    fp.write("<table border=\"1\" width=\"75px\">")
   

    fp.write("<tr><td class=\"bold\" colspan=\"2\">Items</td></tr>")
    fp.write("<tr><td>v</td><td>w</td></tr>")
    for item in range(len(values)):
        if(values[i-1] == values[item]):
            fp.write("<tr bgcolor=\"#ccc\"><td class=\"bold\">" + str(values[item]) + "</td><td class=\"bold\">" + str(weights[item]) + "</td></tr>")
        else:
            fp.write("<tr><td>" + str(values[item]) + "</td><td>" + str(weights[item]) + "</td></tr>")

    fp.write("</table></td></tr></table>")

    currentStep += 1

def printBag(bag):
    for row in bag:
        print(row)

fp.write("<html><head><title>Example of Knapsack</title><style>.bold{font-weight:bold;}</style></head><body>")
bagValue = fillKnapsack([1,6,18,22,28], [1,2,5,6,7], 11)
print("Your bag can carry a value of " + str(bagValue))
fp.write("</body></html>")
fp.close()

# ToDo
# 1 - accept input from a file
# 2 - setup juiper
# 3 - create readme
# check for no item and no weight test cases

