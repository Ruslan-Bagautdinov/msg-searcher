"""
This module provides a Trie data structure for efficient pattern matching. It is used to create regex patterns from lists of words.
"""

import re


class Trie:
    """
    A Trie (prefix tree) implementation for creating regex patterns from a list of words.
    """

    def __init__(self):
        self.data = {}

    def add(self, word):
        """
        Add a word to the Trie.

        :param word: The word to add.
        """
        ref = self.data
        for char in word:
            ref[char] = char in ref and ref[char] or {}
            ref = ref[char]
        ref[''] = 1

    def dump(self):
        """
        Dump the Trie data.

        :return: The Trie data.
        """
        return self.data

    def quote(self, char):
        """
        Escape special characters in the character for use in regex.

        :param char: The character to escape.
        :return: The escaped character.
        """
        return re.escape(char)

    def _pattern(self, p_data):
        """
        Recursively generate a regex pattern from the Trie data.

        :param p_data: The Trie data.
        :return: The regex pattern.
        """
        data = p_data
        if "" in data and len(data.keys()) == 1:
            return None

        alt = []
        cc = []
        q = 0
        for char in sorted(data.keys()):
            if isinstance(data[char], dict):
                try:
                    recurse = self._pattern(data[char])
                    alt.append(self.quote(char) + recurse)
                except:
                    cc.append(self.quote(char))
            else:
                q = 1
        cconly = not len(alt) > 0

        if len(cc) > 0:
            if len(cc) == 1:
                alt.append(cc[0])
            else:
                alt.append('[' + ''.join(cc) + ']')

        if len(alt) == 1:
            result = alt[0]
        else:
            result = "(?:" + "|".join(alt) + ")"

        if q:
            if cconly:
                result += "?"
            else:
                result = "(?:%s)?" % result
        return result

    def pattern(self):
        """
        Generate a regex pattern from the Trie.

        :return: The regex pattern.
        """
        return self._pattern(self.dump())
