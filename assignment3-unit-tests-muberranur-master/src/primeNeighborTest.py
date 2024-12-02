import unittest
import primeNeighbor as pn  

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        
        pass

    def tearDown(self):
       
        pass

    def test010(self):
        # Test when the input is already a prime number
        actualResult = pn.primeNeighbor(upperBound=2)
        expectedResult = 2
        self.assertEqual(expectedResult, actualResult)

    def test020(self):
        # Test when the input is a prime number (greater than 2)
        actualResult = pn.primeNeighbor(upperBound=7)
        expectedResult = 7
        self.assertEqual(expectedResult, actualResult)

    def test030(self):
        # Test when the input is not a prime, expecting the closest lower prime number
        actualResult = pn.primeNeighbor(upperBound=8)
        expectedResult = 7
        self.assertEqual(expectedResult, actualResult)

    def test040(self):
        # Test when the input is a non-prime number, expecting the closest lower prime
        actualResult = pn.primeNeighbor(upperBound=10)
        expectedResult = 7
        self.assertEqual(expectedResult, actualResult)

    def test050(self):
        # Test when the input is a number with a closest lower prime
        actualResult = pn.primeNeighbor(upperBound=14)
        expectedResult = 13
        self.assertEqual(expectedResult, actualResult)

    def test060(self):
        # Test when the input is a large prime number
        actualResult = pn.primeNeighbor(upperBound=101)
        expectedResult = 101
        self.assertEqual(expectedResult, actualResult)

    def test070(self):
        # Test when the input is 1 (edge case, no primes below 1)
        actualResult = pn.primeNeighbor(upperBound=1)
        expectedResult = 0  # Should return 0 for invalid or non-prime numbers
        self.assertEqual(expectedResult, actualResult)

    def test080(self):
        # Test when the input is a string (should return 0)
        actualResult = pn.primeNeighbor(upperBound="hello")
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test090(self):
        # Test when the input is a negative number (should return 0)
        actualResult = pn.primeNeighbor(upperBound=-5)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test100(self):
        # Test when the input is a large number (1000), expecting closest lower prime
        actualResult = pn.primeNeighbor(upperBound=1000)
        expectedResult = 997  # Nearest lower prime is 997
        self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()
