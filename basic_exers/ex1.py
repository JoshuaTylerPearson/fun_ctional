"""
Write a program that accepts 10 student records (roll number and score) and prints them in decreasing order of scores.
In case there are multiple records pertaining to the same student, the program should choose a single record containing
the highest score.
The program should be capable of accepting a multi-line input. Each subsequent line of input will contain a student
record, that is, a roll number and a score (separated by a hyphen).
The output should consist of the combination of roll number and corresponding score in decreasing order of score.

INPUT to program

1001-40
1002-50
1003-60
1002-80
1005-35
1005-55
1007-68
1009-99
1009-10
1004-89

[
    '1001-40', '1002-50', '1003-60', '1002-80', '1005-35',
    '1005-55', '1007-68', '1009-99', '1009-10', '1004-89'
]

OUTPUT from program

1009-99
1004-89
1002-80
1007-68
1003-60
1005-55
1001-40

"""


def sort_scores(number_grade):
    return (                    # TODO return /ordered/ list of key value pairs w/o for-loop
        dict(                   # TODO descriptively functionalize steps
            zip(
                map(
                    lambda x: x[:4],
                    sorted(
                        number_grade,
                        key=lambda x: int(x[5:]),
                    )
                ),
                map(
                    lambda x: x[5:],
                    sorted(
                        number_grade,
                        key=lambda x: int(x[5:]),
                    )
                )
            )
        )
    )

print(
    sort_scores(
        [
            '1001-40', '1002-50', '1003-60', '1002-80', '1005-35',
            '1005-55', '1007-68', '1009-99', '1009-10', '1004-89'
        ]
    )
)

