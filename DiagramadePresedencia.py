import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
from IPython.core.debugger import set_trace
start_times = ['2019-08-08 0:00', '2019-08-08 5:00', '2019-08-10 0:00', '2019-08-12 5:00', '2019-08-14 0:00', '2019-08-16 5:00']
end_times = ['2019-08-16 0:00', '2019-08-09 5:00', '2019-08-11 0:00', '2019-08-13 5:00', '2019-08-18 0:00', '2019-08-18 5:00']
index = ['Timeframe ' + str(i) for i in range(len(start_times))]
df = pd.DataFrame({'Start Time': pd.to_datetime(start_times),
              'End Time' : pd.to_datetime(end_times)}, index=index)
print(df)


