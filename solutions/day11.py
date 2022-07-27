from solutions import Solution


class Day11(Solution):
    INVALID_CHARACTERS = ['i', 'o', 'l']

    def solve(self) -> (str, str):
        first_pass = self.__get_next_password(self.input_lines[0], self.INVALID_CHARACTERS)
        return first_pass, self.__get_next_password(first_pass, self.INVALID_CHARACTERS)

    @staticmethod
    def __generate_letter_increments(exclude_list):
        letters_increments = {}
        for i in range(ord('a'), ord('z') + 1):
            letter = chr(i)
            if letter not in exclude_list:
                if i == ord('z'):
                    letters_increments[letter] = 'a'
                else:
                    if chr(i + 1) in exclude_list:
                        letters_increments[letter] = chr(i + 2)
                    else:
                        letters_increments[letter] = chr(i + 1)
            else:
                letters_increments[letter] = chr(i + 1)
        return letters_increments

    @staticmethod
    def __check_for_increasing_sequence(password):
        for i in range(len(password) - 3):
            if (ord(password[i]) == ord(password[i + 1]) - 1) and (ord(password[i + 1]) == ord(password[i + 2]) - 1):
                return True
        return False

    @staticmethod
    def __check_for_double_pairs(password):
        count = 0
        i = 0
        while i <= len(password) - 2:
            if password[i] == password[i + 1]:
                i += 1
                count += 1
            i += 1

        return count >= 2

    def __validate_password(self, password):
        return self.__check_for_increasing_sequence(password) and self.__check_for_double_pairs(password)

    def __increment_password(self, password, letter_increments, index):
        if index < 0:
            return ''
        elif password[index] == 'z':
            return self.__increment_password(password[:index], letter_increments, index - 1) + letter_increments[
                password[index]]
        else:
            return password[:index] + letter_increments[password[index]]

    def __get_next_password(self, current_password, invalid_characters):
        letter_increments = self.__generate_letter_increments(invalid_characters)

        invalid_character_position = -1
        for i in range(len(current_password)):
            if current_password[i] in invalid_characters:
                invalid_character_position = i
                break

        if invalid_character_position > 0:
            current_password = current_password[:invalid_character_position] \
                               + letter_increments[current_password[invalid_character_position]] \
                               + ''.join(['a'] * (len(current_password) - 1 - invalid_character_position))

        current_password = self.__increment_password(current_password, letter_increments, len(current_password) - 1)

        while not self.__validate_password(current_password):
            current_password = self.__increment_password(current_password, letter_increments, len(current_password) - 1)

        return current_password
