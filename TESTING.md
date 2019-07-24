# Testing

**Project title:**

“Kismet”

**Team members' names:**

Florencia Cabral<br/> Gregory Giordano<br/> Kristin Kernler<br/> Daniel Kingsley<br/> Carter Reid

### Automated Test Cases

**Fortune Cookie tests:**
The Fortune Cookie tests are designed around the random output of the fortune cookie feature.

Filename: test_cookie.py
Path: /app/functions/test_cookie.py

The tests in this file test the getAFortune() and getLuckyNumbers() functions that produce the fortune cookie output. Because the out is random, we can test invariant qualities. The first test (test_getAFortune) asserts that the output is a string and is of length greater than 0. The second test (test_getLuckyNumbers) asserts that the length of the output string is within the possible range, asserts that there are 6 output numbers, and asserts that each number is within the specefied ranges: The first 5 numbers are between 1 and 69 inclusive, and the sixth number is between 1 and 26 inclusive. 

To run the tests, simply cd into the app/functions directory and run test_cookie.py 



### User Acceptance Testing