# Reaction Test Bot

## Project Details

This project is an auto reaction test clicker for [humanbenchmark.com/tests/reactiontime](https://humanbenchmark.com/tests/reactiontime). The code takes a screenshot of a single pixel, checks for the green colours and clicks. Tested to have a reaction time of 33 ms.

## Instructions

Enter [humanbenchmark.com/tests/reactiontime](https://humanbenchmark.com/tests/reactiontime).

Change the values in code if required.  
X_OFFSET is the X position of the top-left corner and Y_OFFSET is the Y position of the top-left corner.

```python
X_OFFSET = 500
Y_OFFSET = 500
```

Once the code is running, start the test and let the program take over. At the end of the test, make sure to terminate the program.

## Requirements

`pip install numpy`  
`pip install mss`  
`pip install mouse`

## Note

I have found it performs faster and more consistently on the Chrome browser compared to Firefox.
