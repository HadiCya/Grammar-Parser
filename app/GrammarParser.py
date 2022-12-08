import nltk

def parse(text):
    nltk.download('averaged_perceptron_tagger')
    #text = "As a customer, I want to be able to order and pay for a pizza from a touchscreen in the lobby by selecting the pizza type and toppings for one or more pizzas. I want to see the total amount due for each pizza and the total amount due for the complete order, displayed on the screen as I select and deselect items. I want to be able to add/delete entire pizzas from the order as well as add/delete toppings from each pizza. When I confirm the order, the system should prompt me for credit card payment."
    print("THIS IS THE TEXT " + text)
    ans = nltk.pos_tag(nltk.word_tokenize(text))
    nouns = []
    verbs = []
    for val in range(len(ans)):
        temp = ans[val][1]
        if(temp == 'NN'):
            try:
                if (ans[val-1][1] == 'TO'):
                    verbs.append(ans[val][0])
                else:
                    nouns.append(ans[val][0])
            except IndexError:
                print("IndexError")
        if(temp == 'NNS' or temp == 'NNPS' or temp == 'NNP' or temp == 'PRP'):
            nouns.append(ans[val][0])
        elif(temp == 'VBZ' or temp == 'VB' or temp == 'VBD' or temp == "VBN" or temp == "VBP" or temp == "VBG"):
            verbs.append(ans[val][0])
    nouns = [*set(nouns)]
    verbs = [*set(verbs)]
    return nouns, verbs