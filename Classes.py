class MathSeries:
    @staticmethod
    def is_prime(number):
        """Checks if a number is prime."""
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def get_prime_numbers(n):
        """Generates n prime numbers."""
        primes = []
        current = 2
        while len(primes) < n:
            if MathSeries.is_prime(current):
                primes.append(current)
            current += 1
        return primes

    @staticmethod
    def fibonacci(n):
        """Generates Fibonacci series up to the nth term."""
        fib = []
        a, b = 0, 1
        for _ in range(n):
            fib.append(a)
            a, b = b, a + b
        return fib

    @staticmethod
    def geometric_progression(a, r, n):
        """Generates geometric progression with starting term a, common ratio r
        up to the nthterm."""
        progression = []
        term = a
        for _ in range(n):
            progression.append(term)
            term *= r
        return progression

    @staticmethod
    def permutation(lst):
        """Generates all permutations of a given list."""
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        perms = []
        for i in range(len(lst)):
            m = lst[i]
            remaining_list = lst[:i] + lst[i+1:]
            for p in MathSeries.permutation(remaining_list):
                perms.append([m] + p)
        return perms
