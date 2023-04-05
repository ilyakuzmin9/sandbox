
hand_2 = ['9', 'Q', '8', 'A']
card_dict = {'A': 1, 'K': 10, 'Q': 10, 'J': 10}

def hand_sum(a_hand):
    cards_sum = 0
    counters_aces = 0
    for card in a_hand:
        if card == 'A':
            counters_aces += 1
        if card.isdigit():
            cards_sum = cards_sum + int(card)
        else:
            for key, value in card_dict.items():
                if card == key:
                    cards_sum = cards_sum + value

    if cards_sum > 21 and counters_aces > 0:
        for count in range(counters_aces):
            cards_sum = cards_sum - 10
            if cards_sum <= 21:
                break
            else:
                continue
    elif cards_sum < 21 and counters_aces > 0:
        for count in range(counters_aces):
            if cards_sum + 10 > 21:
                break
            else:
                cards_sum = cards_sum + 10
    return cards_sum

h2 = hand_sum(hand_2)





arrivals = [2, 5, 1, 2, 0, 10, 3]

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keywords = ['casino', 'car']
l = enumerate(doc_list)

index_list = []
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    # >>> word_search(doc_list, 'casino')
    # >>> [0]
    """
    index_list = []
    keyword = keyword.lower()
    for item in doc_list:
        plain_item = item.lower().replace('.', '').replace(',', '')
        plain_item_list = plain_item.split()
        for element in plain_item_list:
            if element == keyword:
                index_list.append(doc_list.index(item))
                break
    return index_list


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    # >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    # >>> keywords = ['casino', 'they']
    # >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    dic = {}
    print(type(dic))
    for item in keywords:
       dic.update({item: word_search(doc_list, item)})
    return dic


d = multi_word_search(doc_list, keywords)






st = '12345'
print(st.isdigit())

help(any)
import this

print(this)

middle = len(arrivals)/2
if middle.is_integer():
    middle = int(middle)
end = len(arrivals) - 1

lst = arrivals[middle:end]

if 10 in lst:
    print('True')
    pass

new_lst = sorted(lst)
print(new_lst.__len__())

# x = 12
# print(x.imag)

c = 12 + 3j
print(c.imag)
print(c.real)

# help(x.bit_length())

x = 0.125
help(x.as_integer_ratio())