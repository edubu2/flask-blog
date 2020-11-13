import heapq
import re

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


def summarize_text(original_text, sent_max_length=30, top_n=3):
    """Takes a long text string (such as an article or email) and returns the top n most important sentences as a formatted string. 

    Only sentences that have fewer words than sent_max_length can be included in the summary, regardless of content. """

    assert sent_max_length >= 25, "Max sentence length must be greater than or equal to 25"

    def parse_text(original_text):
        """Cleans up the original text so it can be tokenized. Returns full_text & clean_text. """

        full_text = str(original_text)
        # replace reference number (i.e. [n]) with empty space, if any..
        full_text = re.sub(r'\[[0-9]*\]', ' ', full_text)
        # replace one or more spaces with one space
        full_text = re.sub(r'\s+', ' ', full_text)
        # convert all uppercase characters into lowercase characters
        clean_text = full_text.lower()
        # replace character other than [a-zA-Z0-9]
        clean_text = re.sub(r'\W', ' ', clean_text)
        # replace digit with empty
        clean_text = re.sub(r'\d', ' ', clean_text)
        # replace one or more spaces with one space (again)
        text = re.sub(r'\s+', ' ', full_text)

        return full_text, clean_text

    def rank_sentence(full_text, clean_text):
        """Splits text string into sentences, then ranks them. Returns two dictionaries: sentence_score and word_count. """

        sentences = nltk.sent_tokenize(full_text)
        stop_words = nltk.corpus.stopwords.words('english')

        # create dict with the count of each word in the text (excluding stop words). The most frequently used words will be considered the most important
        word_count = {}
        words = nltk.word_tokenize(clean_text)
        for word in words:
            if word not in stop_words:
                word_count[word] = word_count.get(word, 0) + 1

        # rank sentences based on the freq. of the words inside them
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

    def generate_summary(original_text, sent_max_length, top_n):
        """Generates the top three sentences in a string using the wrapped functions above. """

        full_text, clean_text = parse_text(original_text)
        sentence_score, _ = rank_sentence(full_text, clean_text)
        best_sentences = heapq.nlargest(
            top_n, sentence_score, key=sentence_score.get)
        summarized_text = []
        sentences = nltk.sent_tokenize(full_text)

        for sentence in best_sentences:
            summarized_text.append(sentence)

        summarized_text = "\n".join(summarized_text)

        return summarized_text

    # Back to Main function (summarize_text)
    # Generate Summary
    summary = generate_summary(original_text, sent_max_length, top_n)
    return summary
