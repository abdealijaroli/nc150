class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26  # initialize count for each letter in 'a' to 'z'
            for char in word:
                count[ord(char) - ord('a')] += 1  # increment count for that letter
            key = tuple(count)  # convert to tuple so it can be used as a dict key
            anagrams[key].append(word)  # group the word under this key

        return list(anagrams.values())