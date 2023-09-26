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
#             else: return (11 + nul(x[0]))
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

def main(x):
    if (x[3] == 'MUPAD'):
        return 11
    if (x[3] == 'J'):
        return 10
    if (x[3] == 'SMT'):
        if (x[0] == 1999):
            if (x[1] == 1982):
                if (x[4] == 'GAP'):
                    return 0
                if (x[4] == 'NIM'):
                    return 1
            if (x[1] == 1976):
                return 2
        if (x[0] == 2001):
            if (x[1] == 1982):
                if (x[4] == 'GAP'):
                    return 3
                if (x[4] == 'NIM'):
                    return 4
            if (x[1] == 1976):
                return 5
        if (x[0] == 1985):
            if (x[1] == 1976):
                return 9
            if (x[2] == 2007):
                return 6
            if (x[2] == 2001):
                return 7
            if (x[2] == 1983):
                return 8
print(main([2001, 1976, 2001, 'J', 'NIM']))
print(main([2001, 1976, 1983, 'MUPAD', 'NIM']))
print(main([1999, 1976, 2001, 'SMT', 'GAP']))
print(main([2001, 1976, 2007, 'SMT', 'GAP']))
print(main([2001, 1982, 2001, 'SMT', 'NIM']))
