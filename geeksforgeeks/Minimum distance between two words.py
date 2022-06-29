class Solution:
    def shortestDistance(self, s, word1, word2):
        # code here
        start = 0
        i = 0
        j = 0
        dict = {word1: [], word2: []}
        list = []
        for i in range(len(s)):
            if s[i] == word1:
                dict[word1].append(i)
            elif s[i] == word2:
                dict[word2].append(i)

        for i in range(len(dict[word1])):
            for k in range(len(dict[word2])):
                list.append(abs(dict[word1][i] - dict[word2][k]))

        print(min(list))

s = ["the", "quick", "brown","fox","quick"]
word1 = "the"
word2 = "fox"
obj = Solution()
obj.shortestDistance(s,word1,word2)