import hashlib
from solutions import Solution


class Day4(Solution):

    def solve(self) -> (str, str):
        return self.compute_hash(self.input_lines[0], 5), self.compute_hash(self.input_lines[0], 6)

    @staticmethod
    def compute_hash(key: str, zero_length: int):
        md5_hash = hashlib.md5(key.encode())
        i = -1

        while md5_hash.hexdigest()[:zero_length] != zero_length * '0':
            i += 1
            str2hash = key + str(i)
            md5_hash = hashlib.md5(str2hash.encode())

        return i
