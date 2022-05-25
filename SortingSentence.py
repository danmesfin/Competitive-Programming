class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key=lambda word: word[-1])
        words = map(lambda word: word[:-1], words)
        ItMakesSense = ' '.join(words)
        return ItMakesSense
