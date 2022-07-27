import math
from collections import defaultdict
from typing import List

from solutions import Solution


class Day20(Solution):
    PRIMES: List[int]

    def solve(self) -> (str, str):
        input_data = int(self.input_lines[0])
        self.PRIMES = self.__populate_primes(100)
        return self.__compute_part1(input_data), self.__compute_part2(input_data)

    @staticmethod
    def __check_is_prime(n):
        if n == 1 or n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True

    def __populate_primes(self, size):
        PRIMES = []
        PRIMES.append(2)
        count = 3
        while len(PRIMES) < size:
            if self.__check_is_prime(count):
                PRIMES.append(count)
            count += 2
        return PRIMES

    def __generate_prime_factorization(self, num):
        result = defaultdict(int)
        for prime in self.PRIMES:
            while num % prime == 0:
                num = num // prime
                result[prime] += 1
        return result

    @staticmethod
    def __geometric_sum(a: int, r: int, n: int):
        return a * ((r ** (n + 1)) - 1) / (r - 1)

    def __factors_sum(self, num):
        prime_factors = self.__generate_prime_factorization(num)
        result = 1
        for i in [self.__geometric_sum(1, prime_number, count) for prime_number, count in prime_factors.items()]:
            result *= i
        return int(result)

    def __compute_part1(self, total_gifts: int):
        gifts = total_gifts // 10
        result_found = False
        count = 1
        while not result_found:
            if self.__factors_sum(count) > gifts:
                result_found = True
            else:
                count += 1
        return count

    def __get_factors(self, prime_factors, current_index, current_divisor, dividend, valid_factors):
        if current_index == len(prime_factors):
            if dividend / current_divisor <= 50:
                valid_factors.append(current_divisor)
        else:
            prime, count = prime_factors[current_index]
            for _ in range(0, count + 1):
                self.__get_factors(prime_factors, current_index + 1, current_divisor, dividend, valid_factors)
                current_divisor *= prime

    def __factors_sum_with_limit(self, num):
        prime_factors = self.__generate_prime_factorization(num)
        prime_factors = [(prime, count) for prime, count in prime_factors.items()]
        valid_factors = []
        self.__get_factors(prime_factors, 0, 1, num, valid_factors)
        return sum(valid_factors)

    def __compute_part2(self, total_gifts: int):
        gifts = total_gifts // 11
        result_found = False
        count = 1
        while not result_found:
            if self.__factors_sum_with_limit(count) > gifts:
                result_found = True
            else:
                count += 1
        return count
