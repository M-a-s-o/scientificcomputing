import itertools
import random
import sys
from collections import defaultdict
from math import sqrt


def exercise_01() -> None:
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps /= 2.0

    eps *= 2
    print("Exercise 1:")
    print("Machine precision is", eps)
    assert eps == sys.float_info.epsilon


def exercise_02() -> None:
    print("\n\nExercise 2, Part 1:")
    names = ["Mary", "John", "Sarah"]
    ages = [21, 56, 98]

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

    print("Exercise 2, Part 2:")
    random_list = [random.randint(0, 9) for _ in range(10)]

    for i, num in enumerate(random_list):
        print(f"Match: {num} and {i}")


def exercise_03() -> None:
    titles = [
        "don quixote",
        "in search of lost time",
        "ulysses",
        "the odyssey",
        "war and peace",
        "moby dick",
        "the divine comedy",
        "hamlet",
        "the adventures of huckleberry finn",
        "the great gatsby",
    ]

    # Quick way
    # new_titles = [title.title() for title in titles]

    # Manual way
    new_titles: list[str] = []
    for title in titles:
        new_title: str
        new_title_words: list[str] = []
        for word in title.split():
            new_word: str = chr(ord(word[0]) - 32) + word[1:]  # Assume [a-z]
            new_title_words.append(new_word)
        new_title = " ".join(new_title_words)
        new_titles.append(new_title)

    print("\n\nExercise 3:")
    print(new_titles)


def exercise_06() -> None:
    print("\n\nExercise 6:")

    def convert_type(a: str) -> str | float | int:
        if not isinstance(a, str):
            raise TypeError("Argument must be a string")

        if not a:
            return a

        try:
            if "." in a:
                return float(a)
            else:
                return int(a)
        except ValueError:
            return a

    print(convert_type("Cannot convert"))
    print(convert_type("1."))
    print(convert_type("1"))
    print(convert_type(""))
    try:
        print(convert_type(0))
        print(convert_type(0.0))
    except TypeError:
        print("Type error caught")


def exercise_09() -> None:
    print("\n\nExercise 9:")

    class Card:
        def __init__(self, suit: int = 1, rank: int = 2):
            if suit < 1 or suit > 4:
                print("Invalid suit, setting to 1")
                suit = 1

            self.suit = suit
            self.rank = rank

        def value(self):
            """we want things order primarily by rank then suit"""
            return self.suit + (self.rank - 1) * 14

        # we include this to allow for comparisons with < and > between cards
        def __lt__(self, other):
            return self.value() < other.value()

        def __eq__(self, other):
            return self.rank == other.rank and self.suit == other.suit

        def __repr__(self):
            return self.__str__()

        def __str__(self):
            suits = [
                "\u2660",  # spade
                "\u2665",  # heart
                "\u2666",  # diamond
                "\u2663",  # club
            ]

            r = str(self.rank)
            if self.rank == 11:
                r = "J"
            elif self.rank == 12:
                r = "Q"
            elif self.rank == 13:
                r = "K"
            elif self.rank == 14:
                r = "A"

            return r + ":" + suits[self.suit - 1]

    class Deck:
        """the deck is a collection of cards"""

        def __init__(self):
            self.nsuits = 4
            self.nranks = 13
            self.minrank = 2
            self.maxrank = self.minrank + self.nranks - 1

            self.cards: list[Card] = []

            for rank in range(self.minrank, self.maxrank + 1):
                for suit in range(1, self.nsuits + 1):
                    self.cards.append(Card(rank=rank, suit=suit))

        def shuffle(self):
            random.shuffle(self.cards)

        def get_cards(self, num: int = 1):
            # hand: list[Card] = []
            # for n in range(num):
            #    hand.append(self.cards.pop())

            # return hand
            return self.cards[:num]

        def __str__(self):
            string = ""
            for c in self.cards:
                string += str(c) + " "
            return string

    deck = Deck()
    count = 0
    samples = 100_000
    for _ in range(samples):
        deck.shuffle()
        cards = deck.get_cards(5)
        counts = defaultdict(list)
        for card in cards:
            counts[card.rank].append(card.suit)
        if (
            any(len(hand) == 3 for hand in counts.values())  # Three of a kind
            and not any(
                len(hand) == 2 for hand in counts.values()
            )  # Exclude full house
        ):
            count += 1
    mean = count / samples
    sem = sqrt(mean * (1 - mean) / samples)
    exact = 0.021128
    print(f"Exact      : {exact * 100} %")
    print(f"Monte Carlo: ({mean * 100:.3f} +/- {sem * 100:.3f}) %")
    print(f"z-score    : {(mean - exact) / sem}")


def exercise_12() -> None:
    print("\n\nExercise 12:")

    def get_triangle(n: int) -> list[list[int]]:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 1:
            raise ValueError("n must be non-zero")

        rows: list[list[int]] = []
        r: list[int] = [1]
        rows.append(r)
        for _ in range(1, n):
            r = [x + y for x, y in itertools.pairwise(r)]
            r.insert(0, 1)
            r.append(1)
            rows.append(r)
        return rows

    def pretty_print(triangle: list[list[int]]) -> None:
        char_max = len(str(max(triangle[-1])))
        line_size = (char_max + 1) * 2 * len(triangle)

        for row in triangle:
            line = " ".join(f"{n:{char_max * 2 + 1}}" for n in row)
            print(line.center(line_size))

    triang = get_triangle(10)
    pretty_print(triang)


if __name__ == "__main__":
    exercise_01()
    exercise_02()
    exercise_03()
    exercise_06()
    exercise_09()
    exercise_12()
