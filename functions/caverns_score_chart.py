from funcions import score.py
import matplotlib.pyplot as plt

def plot():
    highest_score=1000
    score=sum(scoreList)
    plt.plot(score)
    ratings=[score,highest_score]
    x=["your score","highest score"]
    plt.bar(x, ratings)
    #plt.xlabel('blah blah blah')
    plt.ylabel('SCORE')
    plt.title('cavern scores')
    plt.show()
