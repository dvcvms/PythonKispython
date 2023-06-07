# def nul (i):
#     if (i=="SMALI"):
#         return 0
#     else: return 1


# def main(x):
#     if (x[4] == 1978):
#         return 11
#     else:
#         if (x[3] == 1989):
#             return 10
#         elif (x[3] == 1965):
#             if (x[4] == 2009):
#                 return 6
#             elif (x[4] == 2018):
#                 return 7
#             else: return (8 + nul(x[0]))
#         else:
#             if (x[4] == 2009):
#                 return 9
#             elif (x[4] == 2018):
#                 return(1 + nul(x[0]))
#             else:
#                 if (x[1]==1983):
#                     return 3
#                 elif (x[1] == 1960):
#                     return 4
#                 else:
#                     return 5


def nit(x, top, bot):
    if (x[0] == "SMALI"):
        return top
    else:
        return bot


def one(x, top, middle, bot):
    if (x[1] == 1983):
        return top
    if (x[1] == 1960):
        return middle
    return bot


def four(x):
    if (x[4] == 2009):
        return 6
    if (x[4] == 2018):
        return 7
    return nit(x, 8, 9)


def secFour(x):
    if (x[4] == 2009):
        return 0
    if (x[4] == 2018):
        return nit(x, 1, 2)
    return one(x, 3, 4, 5)


def three(x):
    if (x[3] == 1989):
        return 10
    if (x[3] == 1965):
        return four(x)
    return secFour(x)


def main(x):
    if (x[2] == 1978):
        return 11
    return three(x)


print(main(['SMALI', 1993, 2018, 1965, 2009]))