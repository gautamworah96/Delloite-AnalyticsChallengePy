import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import matplotlib

frame=pd.read_csv('crash.csv',sep=',')
matplotlib.rcParams['figure.figsize'] = (12.0, 8.0)

operator = frame[['Operator','Fatalities']].groupby('Operator').agg(['sum','count'])

fig_ops,((ax1, ax2), (ax3, ax4))=plt.subplots(2,2,sharex=True)
accidents = operator['Fatalities','count'].sort_values(ascending=False)
print(accidents)

frame['Year'] = frame['Date'].apply(lambda x: int(str(x)[-4:]))
interestingOps = accidents.index.values.tolist()[0:3]
interestingOps=interestingOps+accidents.index.values.tolist()[4:5]+accidents.index.values.tolist()[10:11]
print(interestingOps)
optrend = frame[['Operator','Year','Fatalities']].groupby(['Operator','Year']).agg(['sum','count'])
ops = optrend['Fatalities'].reset_index()
fig,axtrend = plt.subplots(2,1)
for op in interestingOps:
    ops[ops['Operator']==op].plot(x='Year',y='sum',ax=axtrend[0],grid=True,linewidth=4)
    
axtrend[0].set_title('Fatalities versus Year with regard to various Operators')

linesF, labelsF = axtrend[0].get_legend_handles_labels()

axtrend[0].legend(linesF,interestingOps,loc=0)
plt.show()