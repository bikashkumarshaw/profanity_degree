# encoding=utf8
import argparse
from nltk.tokenize import sent_tokenize

class Profanity(object):
    def run(self):
        self.args = self._define_args()
        self.slur = []
        if self.args.profanity_file:
            self._prepare_slur(self.args.profanity_file)
        else:
            self._prepare_slur("default_slur.txt")
        self._check_profanity()

    def _prepare_slur(self, slur_file):
        f = open(slur_file)
        for line in f:
            line = line.strip().lower().replace("!", "")
            self.slur.append(line)

    def _calulate_profanity(self, intersection, text_words):
        profanity = 0
        for words in intersection:
            profanity = profanity+text_words.count(words)

        return (float(profanity)/len(text_words))*100

    def _check_profanity(self):
        tweet_file = open(self.args.tweet_file)
        for lno, line in enumerate(tweet_file):
            line = line.strip().lower().replace("!", "")
            sentence = sent_tokenize(line.decode("utf-8"))
            for index, each_sent in enumerate(sentence):
                words = each_sent.split(" ")
                intersection = set(self.slur)&set(words)
                sent_slur_degree = self._calulate_profanity(intersection, words)
                print ("line no. {0} sentence no. {1} has a slur degree of {2}".format(lno+1, index+1, sent_slur_degree))

    def _define_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--tweet-file", help="specify the abs file path containing tweets", type=str, required=True)
        parser.add_argument("--profanity-file", help="specify the abs file path containing foul words", type=str)
        args = parser.parse_args()
        return args

if __name__=="__main__":
    Profanity().run()
