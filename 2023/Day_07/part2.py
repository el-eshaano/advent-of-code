import readfile
from collections import defaultdict

card_strengths = ['J', '2', '3', '4', '5',
                  '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


class Hand:

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.score = -1
        self.get_score()

    def get_score(self):
        counts = defaultdict(int)
        for c in self.cards:
            counts[c] += 1

        res = list(counts.items())
        res = [[x[1], card_strengths.index(x[0])] for x in res]
        res.sort(reverse=True)

        cards = [x[1] for x in res]

        j_present, j_index = False, -1
        if 0 in cards:
            j_index = cards.index(0)
            j_present = True

        if j_present:
            num_j = res[j_index][0]
            i = 0
            while num_j > 0 and i < len(res):

                if i == j_index:
                    i += 1
                    continue

                cards_wanted = 5 - res[i][0]
                cards_added = min(cards_wanted, num_j)
                res[i][0] += cards_added
                num_j -= cards_added

                i += 1

            res[j_index][0] = num_j

        res.sort(reverse=True)
        res = [x[0] for x in res]

        if res[0] == 5:
            self.score = 6
        elif res[0] == 4:
            self.score = 5
        elif res[0] == 3:
            if res[1] == 2:
                self.score = 4
            else:
                self.score = 3
        elif res[0] == 2:
            if res[1] == 2:
                self.score = 2
            else:
                self.score = 1
        else:
            self.score = 0

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        else:
            l = [card_strengths.index(x) for x in list(self.cards)]
            ol = [card_strengths.index(x) for x in list(other.cards)]

            i = 0
            while (l[i] == ol[i]):
                i += 1

            if i == 5:
                return False
            else:
                return l[i] < ol[i]

    def __str__(self):
        return self.cards + " | " + str(self.bid)


input = readfile.line_by_line('input.txt')
hands = []
for line in input:
    cards, bid = line.split(' ')
    bid = int(bid)
    hands.append(Hand(cards, bid))

hands.sort()

winnings = 0
for i, h in enumerate(hands):
    winnings += (i + 1) * h.bid

print(winnings)
