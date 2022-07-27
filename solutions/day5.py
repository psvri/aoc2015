from solutions import Solution


class Day5(Solution):
    BAD_WORDS = ('ab', 'cd', 'pq', 'xy')
    VOWELS = 'aeiou'
    VOWEL_COUNT = 3

    def solve(self) -> (str, str):
        part1_nice_counts = 0
        part2_nice_counts = 0
        for line in self.input_lines:
            if self.__part2_is_good(line):
                part2_nice_counts += 1
            if self.__part1_is_good(line):
                part1_nice_counts += 1

        return part1_nice_counts, part2_nice_counts

    @staticmethod
    def __is_repeating_present(s, diff=1):
        for i in range(len(s) - diff):
            if s[i] == s[i + diff]:
                return True
        return False

    def __contain_vowels(self, s: str):
        vowels = 0
        for vowel in self.VOWELS:
            vowels += s.count(vowel)
        return vowels >= self.VOWEL_COUNT

    def __contains_bad_words(self, s):
        for word in self.BAD_WORDS:
            if word in s:
                return True

    @staticmethod
    def __contains_repeating_pairs(s):
        for i in range(len(s) - 3):
            for j in range(i + 2, len(s) - 1):
                if s[i:i + 2] == s[j:j + 2]:
                    return True

    def __part1_is_good(self, s):
        return self.__is_repeating_present(s) and self.__contain_vowels(s) and not self.__contains_bad_words(s)

    def __part2_is_good(self, s):
        return self.__is_repeating_present(s, 2) and self.__contains_repeating_pairs(s)
