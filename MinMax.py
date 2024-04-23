import math
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
if curDepth == targetDepth:
return scores[nodeIndex]
if maxTurn:
return max(
minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
)
else:
return min(
minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
)
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array separated by spaces:")
scores_input = input().split()
scores = [int(score) for score in scores_input]
treeDepth = math.log(len(scores), 2)
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))