# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# key-lessons:

* Working with open and read for getting a file from a file path and reading its file_contents
* Organizing project among different files instead of all files being packed into one main.py file
* Utils/stats.py
  * count words - easy logic to think through.
    * split() - no arguments for split gave me the better result. Originally I was using split(" ") on space and was missing roughly an additional 500 words because of this. As a result I learned that using split() with no arguments will split on any whitespace character. This includes multiple white spaces, tabs and newline characters. 
  * count chars - easy after speaking with boots (ai of boot.dev). Originally I was splitting out the entire book text as a list of words vs the entire document being one string. This was forcing me to try and do some double for loop logic in order to get just the chars for each individual word. The logic got messy really quickly. I learned that treating one massive file of text as just one string has its advantages. The for loop is simple. We check for each character in the file and add 1 to the value of char_count if we've seen the character before. 
  * pretty_print - this was a headache. It wasn't intuitive in my mind to break the given dict into an even smaller subset of dictionaries. Originally. Just iterating over the key, value pairs of the char_dict.items() was good enough for me to try and return the formatted results.
    * isalpha() started to give me trouble. I understand now why we are doing it on the key vs the list object but it was not clear to me at first how I should be performing this check. Could also be brain fatigue that got to me at this point. 
  * sort/sort_on - a concept I can just not wrap my head around with Python. Lot of helper methods here that I don't fully understand. Reading it in hindsight the logic makes sense. If there is another value to iterate on we iterate and return all the values. We then use these values to sort our original list. 
  * formatting after this was relatively the same as my original approach, I did a double for loop before talking to boots. I then changed it to use the next(iter()). Either way works but I hate seeing double for loops. Makes me think O(n^2).

# Goals for rewrite:
* Keep the A/C's the same. Try to use less help on the logic with boots. Will probably still need to reference this existing code until I understand the nuances of the language. 
* Break out more of the functions. Try to be better at variable and function naming to ease with code clarity. Trying to emphasize more on creating self documenting code vs code that has comments to explain my logic. 
* Nail the rewrite in less than 4 hours. 
