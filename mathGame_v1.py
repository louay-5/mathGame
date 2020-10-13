"""
******************mathGame**********************[Developed byLouay Farah]
[French description]
Le principe du jeu consiste à saisir la liste des noms des joueurs séparés par un espace. Pour chaque
partie du jeu, l’ordinateur proposera le joueur parmi la liste des joueurs restants. A tour de rôle chaque
joueur commencera par donner le nombre d’essais puis l’ordinateur commencera à proposer une
opération de multiplication, le joueur est censé répondre, si la réponse est correcte un point sera ajouté
à son score. Une fois terminé son score sera affiché ainsi de suite. Le joueur avec le meilleur score sera
déclaré gagnant.

Notez bien qu'il faut installer des librairies additionnelles: pandas et matplotlib
(cmd > pip install pandas
 cmd > pip install matplotlib)
"""

import os                        #we'll use os in order to pause the program 
import random as rd              #we'll use choice fonction in order to choose a name randomly
import pandas as pd              #we'll use pandas to create our dataframe from the saved dictionary
import matplotlib.pyplot as plt  #we'll use this package to plot our bar plot
import pickle                    #we'll use the pickler and the unpickler modules to save and load scores


#change current working directory to the choosen one
while True:
    try:
        ch_dir=input("Choose an absolute directory of your recent savefile or to create a new one:  ")
        os.chdir("{}".format(ch_dir)) 
        break
    except:
        print("choose a valid directory. Try again!")

print("*******************Welcome to mathGame!*******************".center(20), end=3*'\n')


try:
    with open("fic_s","rb") as fic_s:
        ficunpickle=pickle.Unpickler(fic_s)
        dict=ficunpickle.load()
    print("Loading previous scores.....", end=2*'\n')
except:
    print("Creating new savefile.....", end=2*'\n')
    dict={}
    with open("fic_s", "wb") as fic_s:
        ficpickle=pickle.Pickler(fic_s)
        ficpickle.dump(dict)



#creating a dataframe of all previous players if there's actually a file
empty=False
try:
    col1, col2= dict.keys(), dict.values()
    d={"name":col1, "score":col2}
    df=pd.DataFrame(d)
except ValueError:
    empty=True
    pass

#creating the list of players
i=1
while i==1:
    try:
        print("Who are the players:", end="\n\n")
        noms=input()
        l=[i.lower() for i in noms.split(" ")]
        assert len(l)>1
        i=0
    except AssertionError:
        print("Enter at least 2 player names. Try again!")
        i=1


#Plotting a barplot showing previous players' scores
if empty!=True:
    df=df[df["name"].isin(l)]
    if df.value_counts().sum()!=0:
        print("This is your previous scores")
        print(df)
        fig1=plt.figure()
        plt.title("previous scores")
        plt.xlabel("name")
        plt.ylabel("score")
        plt.bar(df["name"],df["score"])
        plt.show()


#choosing difficulty
level=input("enter 'e' (easy), 'n' (normal), or other char (hard) :")
if level in "Ee":
    t=8
elif level in "Nn":
    t=15
else:
    t=25




#*******The actual game*******

best_player=None
highest_score=0
i=1
len_liste=len(l)

while i<=len_liste:
    #Choosing a player randomly
    print("Player no {} :".format(i), end="")
    j=rd.choice(l)
    #Choosing the score (new or previous one)
    if empty!=True:
        if j in dict.keys():
            print("{} Do you want to use your previous score (enter 'c') or a new one (enter other char)?".format(j.capitalize()))
            rep=input()
            if rep in "cC":
                score=dict[j]
            else:
                score=0
        else:
            score=0
    l.remove(j)
    print("{} How many times do you want to play?:".format(j.capitalize()), end="")
    while True:
        try:
            essais=int(input())
            break
        except ValueError:
            print("You must enter an integer. Try again!")
    #The question/answer part
    for nb in range(1,essais+1):
        n1=rd.randint(t-7,t)
        n2=rd.randint(t-7,t)
        print("Game {}:".format(nb), sep="")
        print("{}*{}=?".format(n1, n2))
        r=n1*n2
        print("Enter your answer:", sep="")
        m=1
        while m==1:
            try:
                re=int(input())
                m=0
            except ValueError:
                print("Enter an integer. Try again!")
                m=1                
        if re==r:
            print("Correct! {}".format(j.capitalize()))
            score+=1
        else:
            print("False! {}".format(j.capitalize()))
    #Saving the score into a dictionary
    dict[j.lower()]=score
    print(3*'\n', "Final result", end=2*"\n")
    print("{} game(s) and your score = {}".format(essais, score), end=4*'\n')
    if score>highest_score:
        highest_score=score
        best_player=j
    i+=1



print("*****************************************************************")
print("The winner is {} congratulations, score = {} !".format(best_player.capitalize(),highest_score))

save=input("Do you like to save your game? ('o' if yes or other char if not): ")
if save in "oO":
    print("saving....")
    with open("fic_s", "wb") as fic_s:
        ficpickle=pickle.Pickler(fic_s)
        ficpickle.dump(dict)

os.system("pause")
        
    
    
