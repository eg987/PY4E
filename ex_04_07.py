def computegrade(score):
    if score >= 0.9 : 
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    elif score < 0.6 :
        print('F')
    else :
        print("Bad score")
        quit()

computegrade(0.67)

#question for future self: how would I get the program to give me back "Bad score" for non-number arguments? Would I have to reuse original float(score) like I originally worte code for 3_3?