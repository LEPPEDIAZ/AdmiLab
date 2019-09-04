import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
from IPython.core.debugger import set_trace
start_times = ['2019-08-08 0:00', '2019-08-08 5:00', '2019-08-10 0:00', '2019-08-12 5:00', '2019-08-14 0:00', '2019-08-16 5:00']
end_times = ['2019-08-16 0:00', '2019-08-09 5:00', '2019-08-11 0:00', '2019-08-13 5:00', '2019-08-18 0:00', '2019-08-18 5:00']
index = ['Timeframe ' + str(i) for i in range(len(start_times))]
df = pd.DataFrame({'Tiempo Inicio': pd.to_datetime(start_times),
              'Tiempo final' : pd.to_datetime(end_times)}, index=index)
print(df)

#cubo de tiempo 
rng = pd.date_range('2019-08-08 20:00', periods=1, freq='H')
ts = pd.DataFrame(0, index=rng, columns=['minuto'], dtype='float')
print(ts)

rng = pd.date_range('2019-08-08 20:00', periods=1, freq='H')
ts = pd.DataFrame(0, index=rng, columns=['minuto'], dtype='float')
print(ts)

rng = pd.date_range('2019-08-10 20:00', periods=1, freq='H')
ts = pd.DataFrame(0, index=rng, columns=['minuto'], dtype='float')
print(ts)
print(rng)
rng = pd.date_range('2019-08-12 20:00', periods=2, freq='H')
ts = pd.DataFrame(0, index=rng, columns=['minuto'], dtype='float')
print(ts)

rng = pd.date_range('2019-08-16 20:00', periods=1, freq='H')
ts = pd.DataFrame(0, index=rng, columns=['minuto'], dtype='float')
print(ts)

for index, row in ts.iterrows():
    start_boundary = index
    end_boundary = index + Hour()
    time_count = pd.Timedelta('0 m')
    for _, raw_data in df.iterrows():
        start_time = raw_data['Tiempo Inicio']
        end_time = raw_data['Tiempo final']
        if end_time > start_boundary:
            if start_time < end_boundary:
                if start_time <= start_boundary:
                    if end_time >= end_boundary:
                        time_count = time_count + (end_boundary - start_boundary)
                    else:
                            time_count = time + (end_time - start_boundary)
                else:
                    if end_time >= end_boundary:
                        time_count = time_count + (end_boundary - start_time)
                    else:
                        time_count = time_count + (end_time - start_time)
    ts.at[index, 'minuto'] = time_count.seconds / 60
    print(ts) 
    print(df)
    print("calcular", ts.at[index, 'minuto'])