import sys
import pandas as pd
import numpy as np
import heapq
import re

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


def main():
    file_name = "text_files/" + \
        str(input("1. Enter text file name (without extension): ")) + ".txt"
    sent_max_length = 30
    top_n = 3

    def get_text(text_file):
        """Takes a .txt file and returns the text, as well as the cleaned text. """

        with open(text_file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        # replace reference number (i.e. [n]) with empty space, if any..
        text = re.sub(r'\[[0-9]*\]', ' ', text)
        # replace one or more spaces with one space
        text = re.sub(r'\s+', ' ', text)
        # convert all uppercase characters into lowercase characters
        clean_text = text.lower()
        # replace character other than [a-zA-Z0-9]
        clean_text = re.sub(r'\W', ' ', clean_text)
        # replace digit with empty
        clean_text = re.sub(r'\d', ' ', clean_text)

        return text, clean_text

    def rank_sentence(text, clean_text):
        """Splits text string into sentences, then ranks them. """

        sentences = nltk.sent_tokenize(text)
        stop_words = nltk.corpus.stopwords.words('english')

        word_count = {}
        words = nltk.word_tokenize(clean_text)
        for word in words:
            if word not in stop_words:
                word_count[word] = word_count.get(word, 0) + 1

        sentence_score = {}

        for sentence in sentences:
            sentence_words = nltk.word_tokenize(sentence.lower())
            num_words = len(sentence.split(' '))

            for word in sentence_words:
                if word in word_count.keys():
                    # only take sentence that has less than 30 words
                    if num_words < sent_max_length:
                        # add word score to sentence score
                        sentence_score[sentence] = sentence_score.get(
                            sentence, 0) + word_count[word]

        return sentence_score, word_count

    def generate_summary(file_name, sent_max_length, top_n):
        text, clean_text = get_text(file_name)
        sentence_score, _ = rank_sentence(text, clean_text)
        best_sentences = heapq.nlargest(
            top_n, sentence_score, key=sentence_score.get)
        summarized_text = []
        sentences = nltk.sent_tokenize(text)

        for sentence in best_sentences:
            summarized_text.append(sentence)

        summarized_text = "\n".join(summarized_text)

        return summarized_text

    # Back to Main
    # Generate Summary
    summary = generate_summary(file_name, sent_max_length, top_n)
    print("------------------ \nSUMMARY START\n", summary)


if __name__ == '__main__':
    main()
