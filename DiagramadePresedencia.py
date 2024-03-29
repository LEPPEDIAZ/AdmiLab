import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
start_time = ['2019-08-08 0:00', '2019-08-08 5:00', '2019-08-10 0:00', '2019-08-12 5:00', '2019-08-14 0:00', '2019-08-16 5:00','2019-08-18 5:00','2019-08-18 5:00','2019-08-20 0:00', '2019-08-22 5:00','2019-08-24 5:00','2019-08-26 5:00', '2019-08-28 5:00', '2019-08-30 5:00','2019-09-01 5:00', '2019-09-03 5:00', '2019-09-03 5:00', '2019-09-03 5:00', '2019-09-05 5:00', '2019-09-07 5:00', '2019-09-09 5:00', '2019-09-14 5:00', '2019-09-15 5:00','2019-09-15 5:00', '2019-09-19 5:00', '2019-09-23 5:00','2019-09-23 5:00','2019-09-27 5:00', '2019-10-01 5:00', '2019-10-27 5:00', '2019-11-06 5:00', '2019-11-06 5:00', '2019-11-16 5:00', '2019-11-18 5:00']
end_time = ['2019-08-16 0:00', '2019-08-09 5:00', '2019-08-11 0:00', '2019-08-13 5:00', '2019-08-18 0:00', '2019-08-18 5:00','2019-09-01 5:00', '2019-08-19 5:00','2019-08-21 0:00','2019-08-23 5:00', '2019-08-25 5:00', '2019-08-27 5:00', '2019-08-29 5:00', '2019-08-31 5:00','2019-09-02 5:00','2019-09-04 5:00' , '2019-09-04 5:00', '2019-09-04 5:00','2019-09-06 5:00', '2019-09-08 5:00', '2019-09-14 5:00', '2019-09-16 5:00', '2019-09-16 5:00', '2019-09-18 5:00', '2019-09-22 5:00', '2019-09-24 5:00','2019-09-28 5:00','2019-09-30 5:00', '2019-10-26 5:00', '2019-11-05 5:00', '2019-11-24 5:00', '2019-11-15 5:00', '2019-11-17 5:00', '2019-11-23 5:00']
index = ['Timeframe ' + str(i) for i in range(len(start_time))]
df = pd.DataFrame({'Tiempo Inicio': pd.to_datetime(start_time),
              'Tiempo final' : pd.to_datetime(end_time)}, index=index)
pesimista = [8,1,1,1,1,1,3,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,3,3,1,5,3,26,8,8,3]
optimista = [2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,2,1,3,3,1,2,1,10,5,5,1]
probable = [4,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,3,3,15,1,15,8,1,1]
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


def DP (iteraciones):
    dias = [] 
    dia = 0
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
        print("calcular", (ts.at[index, 'minuto'])/100) 
    for i in range (iteraciones):
        for k in range (len(pesimista)):
            h = plt.hist(np.random.triangular(optimista[k],probable[k], pesimista[k], 100000), bins=200,density=True)
            plt.show()
    

DP (10000)
DP (100000)