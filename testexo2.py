from TP_Exo2_190923_TuanMinh import bissextile
from TP_Exo2_190923_TuanMinh import months
from TP_Exo2_190923_TuanMinh import valid
from TP_Exo2_190923_TuanMinh import calendar

test1 = print(bissextile(2000))     #True
test2 = print(bissextile(1467))     #False
test3 = print(bissextile(2004))     #True
test4 = print(months(1,2000))       #31
test5 = print(months(2,2000))       #29
test6 = print(months(2,2001))       #28
test7 = print(months(7,2000))       #31
test8 = print(months(8,2000))       #31
test9 = print(months(11,2000))      #30
test10 = print(valid(31,2,2000))    #False
test11 = print(valid(29,2,2000))    #True
test12 = print(valid(31,8,2000))    #True
test13 = print(valid(31,11,2000))   #False
test14 = print(valid(30,10,2000))   #True
test15 = calendar()