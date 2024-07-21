number_of_participant=int(input("Enter number of participant: "))
scores=list(map(int,input("Enter scores separted by spaces: ").split()))
scores.sort()
maximum = scores.index(max(scores))
runner_up_score = scores[maximum - 1]
print(f"Runner up score of the game is {runner_up_score}")