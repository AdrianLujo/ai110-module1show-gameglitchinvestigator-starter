# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

First time that I ran the game, was presented with a screen to submit number guesses. Three difficulties (Easy, Normal, and Hard), with an option to toggle hints, a "New Game" button and a "Submit Guess" button.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. First time that you run the game on Normal difficulty, you have 7 attempts available. Subsequent games allow 8 attempts

2. Following prompt to "Press Enter to Apply" does nothing. User can only press the "Submit Guess" button to submit their guess. I expected to be able to press enter to submit my guess.

3. The "Go Lower" and "Go Higher" hints don't correspond to the secret value. When the secret value is 8, I guessed 66 and was told to go higher. I should've been told to go lower.

4. After winning or losing a game, pressing the "New Game" button does reset the secret value and the number of attempts (both available and used), however, pressing Enter or pressing "Submit Guess" does not register a response.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 5 when secret is 30| Expected hint to be "Go Higher"|Received hint "Go Lower" | No error |
|Guessed 100 when secret is 30 | Expected hint to be "Go Lower"|Received hint "Go Higher" |No error |
|Pressed "New Game" after winning a game|Can submit guesses by pressing "Submit Guess" | Game updates secret and attempts, but cannot submit guesses. Game is stuck| No error|
|Pressed "New Game" with an unfinished game|Expect score to reset| Score persists to new game| No error|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude in VSCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked Claude why I was getting the incorrect hints when a guess was too high or too low, Claude identified that the hints were flipped, which was correct. I confirmed by looking at the code and Claude's suggestion, and creating a unit test to confirm the correct outcome.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude suggested coercing valid values to integers to solve for the app.py passing the secret as a string on even attempts. It's better in this case to ensure that all attempts pass the secret as an integer, so I suggested that fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Running a test against the bug and trying to recreate the scenario by using the application.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  I didn't want to refactor the reset game state function out of app.py, so I ran taht test manually. I lost a game and pressed the New Game button, confirming that I now had a fresh game state and could submit new guesses. This showed that Claude's suggestion arrived at the intended outcome.
- Did AI help you design or understand any tests? How? Yes, Initially, the first three default tests were failing. I asked Claude why and it pointed out that I needed to return the initial value of the two by using the [0] index on result.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit recreates the entire page by running the script from scratch on user interaction. Without session state, the user's data from interacting with the application would be lost on the next rerun. Session state stores data between reruns so that it persists as the user is interacting with the application. Data does not survive browser page refreshes and is local to the instance that user is running.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
Using AI to help explain why something isn't working well, then validating that in the code. This is better than just taking Claude's word for it.
- What is one thing you would do differently next time you work with AI on a coding task?
I would've not taken every suggestion from the start and looked to understand the underlying cause. There was a case where AI suggested a fix that was a bandaid to code that wasn't doing anything useful.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed how I think about AI generated code in that it can be useful as a starting point but should be validated and tested to ensure correct functionality.
