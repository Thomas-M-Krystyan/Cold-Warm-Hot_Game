# Cold-Warm-Hot Game

### Description:
Pre-Intermediate Python's script game to guessing a locker combination password of 3 digits.

Cold-Warm-Hot game is a deduction game you can play with a friend. Your friend thinks up<br>
a random 3-digit number with no repeating digits, and you try to guess what the number is.<br>
After each guess, your friend gives you three types of clues:

- Cold – None of the three digits you guessed is in the secret number
- Warm – One of the digits is in the secret number, but your guess has the digit in the wrong place
- Hot – Your guess has a correct digit in the correct place

You can get multiple clues after each guess. If the secret number is 456 and your guess is 546 the<br>
clues would be “hot warm warm”. The 6 provides hot (that digit position is correct) and the 5 and 4<br>
provide warm warm (that digits exist in secret number, althought their positions are incorrect). The<br>
sequence of clues matters – hot should be always before warm.

---
### Summary:

|  Language  | Version | Frameworks | Version |  Paradigm  |    Category     |      Level       |         Group project          | Code freeze |
|:----------:|:-------:|:----------:|:-------:|:----------:|:---------------:|:----------------:|:------------------------------:|:-----------:|
|   Python   |  3.5.2  |     -      |    -    | Procedural | Game, algorithm | Pre-Intermediate | Pair-programming + contributor | 12.11.2017* |

\* thanks for contribution of [Muhamed Hassan](https://github.com/Muhamed0Hassan)

---
### Run:

>Windows
- execute `.py` file

>Linux
- type `python3 [filename].py` in the [CLI](https://en.wikipedia.org/wiki/Command-line_interface)
