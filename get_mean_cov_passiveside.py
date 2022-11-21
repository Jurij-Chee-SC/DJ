import pandas

import os
import pandas as pd
import numpy as np

def get_data(Depth_number):
    Raw_data = pd.read_csv('Data'+str(Depth_number)+'.csv', index_col=0)
    Raw_data_tran = Raw_data.T
    #print(Raw_data_tran )
    #print(list(Raw_data_tran ))
    #print(pd.DataFrame(Raw_data_tran.min()))
    Nc_Index = []
    for i in range (0,int(0.5*len(list(Raw_data.T)) )):
        Nc_Index.append(list(Raw_data.T)[2*i+1])
    #print(Nc_Index)
    #print(pd.DataFrame(Raw_data_tran.min()).loc[Nc_Index])
    '''
    for i in range(0,int(len(Raw_data_tran.min())/2)):
        print(Raw_data_tran.min()[2*i+1])
    '''

    Output = pd.DataFrame(Raw_data_tran.max(), columns=[str(Depth_number)]).loc[Nc_Index]
    return Output

All_out = pd.DataFrame()
for i in range(1,61):
    All_out = pd.concat([All_out,get_data(i)],axis=1)
All_out.to_csv('3Final_Nc_at_various_depth_pass.csv')