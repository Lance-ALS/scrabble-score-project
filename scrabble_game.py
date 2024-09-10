import random
import time

class ScrabbleGame:
    letter_scores = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }
    
    dictionary = {
        2: ['is', 'an', 'on', 'it', 'up'],
        3: ['dog', 'cat', 'bat', 'run', 'sun'],
        4: ['tree', 'frog', 'book', 'fire', 'blue'],
        5: ['apple', 'grape', 'flame', 'track', 'crane'],
        6: ['flower', 'castle', 'ticket', 'circle', 'bubble'],
        7: ['running', 'jumping', 'picture', 'present', 'freight'],
        8: ['elephant', 'building', 'fantasy', 'computer', 'hospital'],
        9: ['strawberry', 'adventure', 'sunflower', 'chocolate', 'dinosaur']
    }

    def __init__(self):
        self.total_score = 0

    def calculate_score(self, word):
        score = 0
        word = word.lower()  # Convert the word to lowercase to handle case insensitivity
        for letter in word:
            if letter in ScrabbleGame.letter_scores:
                score += ScrabbleGame.letter_scores[letter]
        return score
    
    def setUp(self):
        self.game = ScrabbleGame()

    def validate_word(self, word):
        if not word.isalpha():
            raise ValueError("Input must be alphabetic characters only.")
        return word.lower() in self.dictionary.get(len(word), [])

    def check_word_length(self, word, required_length):
        return len(word) == required_length
    
    def generate_random_word_length(self):
        return random.randint(2, 9)

    def play_round(self):
        required_length = self.generate_random_word_length()
        print(f"Please enter a word of length {required_length}. You have 15 seconds.")
    
        start_time = time.time()
        word = input("Your word (or type 'quit' to exit): ").strip()
        end_time = time.time()

        if word.lower() == 'quit':
            return 'quit'  

        time_taken = end_time - start_time

        if time_taken > 15:
            print("Time is up! No score for this round.")
            return 0

        if not self.check_word_length(word, required_length):
            print(f"Invalid word length. Word should be {required_length} characters.")
            return 0

        if not self.validate_word(word):
            print(f"Invalid word. Not found in dictionary.")
            return 0

        score = self.calculate_score(word)
        adjusted_score = self.adjust_score_based_on_time(score, time_taken)
        return adjusted_score
    
    def check_game_over(self, rounds):
        if rounds >= 10:
            return self.total_score
        return None
    
    def adjust_score_based_on_time(self, score, time_taken):
        if time_taken < 5:
            return score + 5  
        elif time_taken < 10:
            return score + 3
        return score

def main():
    game = ScrabbleGame()
    rounds = 0

    while True:
        if rounds == 10:
            print(f"Game over! Your total score is: {game.total_score}")
            break

        print(f"Round {rounds + 1}:")
        score = game.play_round()

        if score == 'quit':
            print(f"Thank you for playing! Your total score is: {game.total_score}")
            break

        game.total_score += score
        print(f"Score for this round: {score}")
        rounds += 1

if __name__ == "__main__":
    main()