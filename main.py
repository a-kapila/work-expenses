#Simple greedy algorithm to clear debts minimally 

import pandas as pd
import numpy as np
#Get dict of debtors and creditors
df = pd.from_csv('work_expenses.csv').loc[0:2].to_dict()

while True:
    #sort in ascending order
    df = {k: v for k, v in sorted(df.items(), key=lambda item: item[1])}
    cred = np.absolute(list(df.values())[-1])
    deb = np.absolute(list(df.values())[0])
    if cred == deb:
        print(df.keys()[0] + 'pays' + df.keys()[-1] + ' ' + str(cred)
        del df.keys()[0]
        del df.keys()[-1]
    elif cred > deb:
        print(df.keys()[0] + 'pays' + df.keys()[-1] + ' ' + str(deb)
        del df.keys()[0]
    else:
        print(df.keys()[0] + 'pays' + df.keys()[-1] + ' ' + str(cred)
        del df.keys()[-1]
    if df == {}:
        break