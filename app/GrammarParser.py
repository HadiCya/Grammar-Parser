import nltk
import spacy

def parse2(text):
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    ans = nltk.pos_tag(nltk.word_tokenize(text))
    print(ans)
    nouns = []
    verbs = []
    for val in range(len(ans)):
        temp = ans[val][1]
        if(temp == 'NN' or temp == 'NNS' or temp == 'NNPS' or temp == 'NNP' or temp == 'PRP'):
            nouns.append(ans[val][0])
        elif(temp == 'VBZ' or temp == 'VB' or temp == 'VBD' or temp == "VBN" or temp == "VBP" or temp == "VBG"):
            verbs.append(ans[val][0])
    nouns = [*set(nouns)]
    verbs = [*set(verbs)]
    return nouns, verbs

text = "As a customer, I want to be able to order and pay for a pizza from a touchscreen in the lobby by selecting the pizza type and toppings for one or more pizzas. I want to see the total amount due for each pizza and the total amount due for the complete order, displayed on the screen as I select and deselect items. I want to be able to add/delete entire pizzas from the order as well as add/delete toppings from each pizza. When I confirm the order, the system should prompt me for credit card payment."
text = "I am going to bed"
text = "The quick brown fox jumps over the lazy dog"
text = "This functions well most of the time, but sometimes nouns and verbs are mixed up"
text = "The jump was amazing."
text = "I like ohfgoidhod and cats"


def parse(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    nouns = []
    verbs = []

    for token in doc:
        if token.pos_ == "NOUN":
            nouns.append(token.text)
        elif token.pos_ == "VERB":
            verbs.append(token.text)

    return nouns, verbs