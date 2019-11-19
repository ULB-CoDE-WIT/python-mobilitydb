from MobilityDB import *
from datetime import datetime

print("\n# PERIOD")

# Constructor

var = PERIOD('[2019-09-08, 2019-09-10]')
print("Constructor string:", var)
var = PERIOD('[2019-09-08, 2019-09-10)')
print("Constructor string:", var)
var = PERIOD('(2019-09-08, 2019-09-10]')
print("Constructor string:", var)
var = PERIOD('(2019-09-08, 2019-09-10)')
print("Constructor string:", var)
var = PERIOD('2019-09-08', '2019-09-10')
print("Constructor 2 args:", var)
var = PERIOD('2019-09-08', '2019-09-10', False, True)
print("Constructor 4 args:", var)

# Accessor functions
var1 = var.lower()
print("lower:", var1)
var1 = var.upper()
print("upper:", var1)
var1 = var.lower_inc()
print("lower_inc:", var1)
var1 = var.upper_inc()
print("upper_inc:", var1)
var1 = var.duration()
print("duration:", var1)

# Comparisons
var1 = PERIOD('2019-09-08', '2019-09-10', True, True)
var2 = PERIOD('2019-09-08', '2019-09-10', False, True)
print("Eq:", var1 == var2)
print("Lt:", var1 < var2)
print("Le:", var1 <= var2)
print("Gt:", var1 > var2)
print("Ge:", var1 >= var2)

print("\n# TIMESTAMPSET")

# Constructor
var = TIMESTAMPSET('{2019-09-08, 2019-09-10, 2019-09-11, 2019-09-12}')
print("Constructor string:   ", var)
var = TIMESTAMPSET('2019-09-08', '2019-09-10', '2019-09-11', '2019-09-12')
print("Constructor strings:  ", var)

t1 = datetime.strptime('2019-09-08', '%Y-%m-%d')
t2 = datetime.strptime('2019-09-10', '%Y-%m-%d')
t3 = datetime.strptime('2019-09-11', '%Y-%m-%d')
t4 = datetime.strptime('2019-09-12', '%Y-%m-%d')
var = TIMESTAMPSET(t1, t2, t3, t4)
print("Constructor datetimes:", var)

# Error
# t4 = datetime.strptime('2019-09-11', '%Y-%m-%d')
# var = TIMESTAMPSET(t1, t2, t3, t4)

# Accessor functions
var1 = var.timespan()
print("Timespan:", var1)
var1 = var.numTimestamps()
print("numTimestamps:", var1)
var1 = var.startTimestamp()
print("startTimestamp:", var1)
var1 = var.endTimestamp()
print("endTimestamp:", var1)
var1 = var.timestampN(1)
print("timestampN(1):", var1)
var1 = var.timestampN(4)
print("timestampN(4):", var1)
var1 = var.timestamps()
print("timestamps:", var1)

print("\n# PERIODSET")

# Constructor
var = PERIODSET('{[2019-09-08, 2019-09-10], [2019-09-11, 2019-09-12), \
    [2019-09-13,2019-09-13], (2019-09-14, 2019-09-15]}')
print("Constructor string:  ",var)
var = PERIODSET('[2019-09-08, 2019-09-10]', '[2019-09-11, 2019-09-12)', \
    '[2019-09-13,2019-09-13]', '(2019-09-14, 2019-09-15)')
print("Constructor elements:",var)

# Accessor functions
var1 = var.timespan()
print("Timespan:", var1)

var1 = var.numTimestamps()
print("numTimestamps:", var1)
var1 = var.startTimestamp()
print("startTimestamp:", var1)
var1 = var.endTimestamp()
print("endTimestamp:", var1)
var1 = var.timestampN(1)
print("timestampN(1):", var1)
var1 = var.timestamps()
print("timestamps:", var1)

var1 = var.numPeriods()
print("numPeriods:", var1)
var1 = var.startPeriod()
print("startPeriod:", var1)
var1 = var.endPeriod()
print("endPeriod:", var1)
var1 = var.periodN(1)
print("periodN(1):", var1)
var1 = var.periods()
print("periods:", var1)
