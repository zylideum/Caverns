import matplotlib.pyplot as plt

scoreList = []
def score(x):
    scoreList.append(x)
    print("You gained", x, "points. Your total score is", sum(scoreList))
    totalScore = sum(scoreList)
    
def plot():
    highest_score=8002
    score=sum(scoreList)
    plt.plot(score)
    ratings=[score,highest_score]
    x=["your score","highest possible score"]
    plt.bar(x, ratings)
    #plt.xlabel('blah blah blah')
    plt.ylabel('SCORE')
    plt.title('cavern score')
    plt.show()

