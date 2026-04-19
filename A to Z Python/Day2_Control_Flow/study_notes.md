# Day 2: Control Flow (Decision Making)

In programming, we often need to make decisions. "If this happens, do that."

## 1. Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

## 2. The `if` Statement
```python
age = 18
if age >= 18:
    print("You can drive!")
else:
    print("Too young to drive.")
```

## 3. Multiple Conditions (`elif`)
`elif` is short for "else if".
```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

## 4. Logical Operators
- `and`: Both conditions must be true.
- `or`: At least one condition must be true.
- `not`: Flips the result (True becomes False).
