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

**Horoscope Feature Tests:** 
The Horoscope Generator tests verify that users get a string after making their selection of solar sign (personal traits sentence), and another string (fortune) after selecting a fortune type. It also checks that the fortune exists in one of the files where fortunes are stored.

Filename: test_horoscope.py 
Path: /app/functions/test_horoscope.py

The tests in this file test the horoscopeTraits() and horoscopeFortuneGenerator() functions that produce the horoscope output. Two tests check that the functions return an output of type string, with a length greater than 0. The second test checks that the fortune returned exists in one of the files from where fortunes should be sourced. 
To run the tests, cd into the app/functions directory and run test_horoscope.py

**Schema Tests:**
The schema tests test the schema file that serves as the basis of the database. They test inserts into a database that uses this schema, as well as the schema contraints unique and foreign key. The output should confirm that all 4 tests pass, or report any test failures.

Filename: test_schema.py
Path: /tests/test_schema.py

To run the tests from highest level directory in terminal: ./tests/test_schema.py


### User Acceptance Testing

### Test 1: Home page
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions                                                        |    Expected Result                                                               |    Actual Result    |    Pass/Fail    |    Initial & date    |
|------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------|-----------------|----------------------|
|    1       |    Go to kismet website at: https://kismet3308.herokuapp.com/          |    Kismet home page loads and greets user                                        |                     |                 |                      |
|    2       |    Click “mood ring” “register” or “log in” to leave the home page.    |    Main menu stays at top of page. Page content/body changes to linked   page    |                     |                 |                      |
|    3       |    Click “Home” in the main menu at the top left of the screen         |    User is returned to the home page.                                            |                     |                 |                      |
Pass/Fail_______ Initial & Date______

### Test 2: Fortune Cookie
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on “Fortune Cookie” link at the top of the page    |    Fortune cookie page loads with picture of fortune cookie    |         |         |         |
|    3    |    Click on the “get fortune” button    |    Fortune cookie image changes. Text is displayed with user’s fortune    |         |         |         |
Pass/Fail_______ Initial & Date______

### Test 3: Mystic 9 Ball
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|------------------------------------------------------------------|----------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on the “mystic 9 ball” link at the top of the page    |    Mystic 9 ball page loads    |         |         |         |
|    3    |    Click on “give me an answer”    |    Mystic 9 ball displays answer    |         |         |         |
Pass/Fail______ Initial & Date______

### Test 4: Horoscope
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|------------------------------------------------------------------|----------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on the “Horoscope” link at the top of the screen    |    Horoscope page loads    |         |         |         |
|    3    |    Click on your Zodiac sign    |    User gets a personality trait line, and is asked what kind of fortune (s)he wants    |         |         |         |
|    4    |    Click on a type of fortune    |    User gets a fortune of the kind selected, and is asked if (s)he wants another one    |         |         |         |
|    5    |    Click on Yes or No    |    If Yes, page asks user to select a type of fortune. Return to Step 4    |         |         |         |
Pass/Fail______ Initial & Date______

## Test 5: Genie
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on the “Genie” link at the top of the page    |    Genie page loads    |         |         |         |
|    3    |    User picks a turtle to race, and starts the race    |    Turtles race until 3 have finished. If user’s turtle won, then text   informs user that their wish will come true. Otherwise, user is told to play   again.    |         |         |         |
Pass/Fail______ Initial & Date______

### Test 6: Mood Ring
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|------------------------------------------------------------------|----------------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on the “mood ring” link at the top of the page    |    User is taken to the mood ring page    |         |         |         |
|    3    |    Click on the "Tell Me My Mood" button    |    Ring changes colors and current mood is displayed    |         |         |         |
Pass/Fail______Initial & Date______

### Test 7: Register/Login
Test case Author: Carter Reid

Test case Executed by: ______________

|    Step    |    Instructions    |    Expected Result    |    Actual Result    |    Pass/Fail    |    Initial & Date    |
|------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------|-----------------|----------------------|
|    1    |    Go to kismet website at: https://kismet3308.herokuapp.com/    |    Kismet home page loads and greets user    |         |         |         |
|    2    |    Click on the “Register” link at the top of the page    |    User is prompted to enter Username, password, and select an astrology   sign    |         |         |         |
|    3    |    Enter username/password and select a star sign. Click Register    |    User Registration is confirmed    |         |         |         |
Pass/Fail______ Initial & Date______

