# https://www.interviewcake.com/question/python/bracket-validator?course=fc1&section=queues-stacks
# You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces,
# brackets, and parentheses are off. To save you both some time,
# you decide to write a braces/brackets/parentheses validator.
#
# Let's say:
#
# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.


def validate_brackets(chars):
    openers = {"{", "(", "["}
    closers = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    bracket_stack = []

    for char in chars:
        if char in openers:
            bracket_stack.append(char)
        elif char in closers:
            if not bracket_stack or bracket_stack.pop() != closers[char]:
                return False
    if bracket_stack:
        return False
    return True


b1 = "{ [ ] ( ) }"
b2 = "{ [ ( ] ) }"
print(validate_brackets(b1))
print(validate_brackets(b2))