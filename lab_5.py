def main():
    word_list = []
    total_vowels = 0
    total_consonants = 0

    while True:
        word = input("Input a sequence of words, one at a time (to stop, enter an empty string): ")
        if word == "":
            break
        word_list.append(word)

        vowels = "aeiouAEIOU"
        for char in word:
            if char in vowels:
                total_vowels += 1
            elif char.lower() in "bcdfghjklmnpqrstvwxyz":
                total_consonants += 1

    if not word_list:
        print("No words entered.")
        return

    shortest_word = min(word_list, key=len)
    longest_word = max(word_list, key=len)
    word_count = len(word_list)
    total_word_length = sum(len(word) for word in word_list)

    first_word = min(word_list, key=str.lower)
    last_word = max(word_list, key=str.lower)

    average_word_length = total_word_length / word_count if word_count else 0
    average_vowels = total_vowels / word_count if word_count else 0
    average_consonants = total_consonants / word_count if word_count else 0

    print(f"Longest word: {longest_word}, Shortest word: {shortest_word}")
    print(f"Number of words: {word_count}")
    print(f"Average word length: {average_word_length:.2f}")
    print(f"First word in lexicographic order: {first_word}, Last word in lexicographic order: {last_word}")
    print(f"Average number of vowels per word: {average_vowels:.2f}, Average number of consonants per word: {average_consonants:.2f}")

if __name__ == "__main__":
    main()
