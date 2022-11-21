import pandas

import os
import pandas as pd
import numpy as np


def intplt(Coor_1, coor_and_y, column_name):
    #sort value
    Coor_1.columns = ['z1']
    Coor_1.sort_values(by= ['z1'],ascending = True, inplace= True)

    coor_and_y.columns = ['z2','y2']
    coor_and_y.sort_values(by= ['z2'],ascending = True, inplace= True)
    y_out = []
    for i in range(0,len(Coor_1)):
        if Coor_1.iloc[i,0]<=coor_and_y.iloc[0,0]:
            y_out_i =  ((coor_and_y.iloc[1,1]-coor_and_y.iloc[0,1]))/((coor_and_y.iloc[1,0]-coor_and_y.iloc[0,0])) \
                *(Coor_1.iloc[i,0]-coor_and_y.iloc[0,0])+coor_and_y.iloc[0,1]
        elif Coor_1.iloc[i,0]>=coor_and_y.iloc[-1,0]:
            y_out_i =  ((coor_and_y.iloc[-1,1]-coor_and_y.iloc[-2,1]))/((coor_and_y.iloc[-1,0]-coor_and_y.iloc[-2,0])) \
                *(Coor_1.iloc[i,0]-coor_and_y.iloc[-2,0])+coor_and_y.iloc[-2,1]
        else:
            for h in range(0,len(coor_and_y)):
                if Coor_1.iloc[i,0]>=coor_and_y.iloc[h,0] and Coor_1.iloc[i,0]<coor_and_y.iloc[h+1,0]:
                    y_out_i = ((coor_and_y.iloc[h+1,1]-coor_and_y.iloc[h,1]))/\
                              ((coor_and_y.iloc[h+1,0]-coor_and_y.iloc[h,0])) \
                              *(Coor_1.iloc[i,0]-coor_and_y.iloc[h,0])+coor_and_y.iloc[h,1]
        y_out_i = [y_out_i]
        y_out.append(y_out_i)
    y_out = pd.DataFrame(y_out)
    y_out.columns = [column_name]
    return y_out
    #print(Coor_1)
    #print(coor_and_y)
    #print(y_out)

def main_program(number, frame):
    number = str(number)
    #This is for getting the data of Z coor in FM
    FM_matrix = pd.read_csv(number + '\\fm'+str(frame)+'.csv')
    Coordinate_row = pd.DataFrame(FM_matrix["CutZ"])
    Coordinate_row = pd.DataFrame(Coordinate_row.iloc[0:-1])
    #print(Coordinate_row)

    #This is for getting the data of su
    sui_row = pd.read_csv(number + '\\su.csv', names=['ID','z1','su1'],sep='\s+')
    sui_row = pd.DataFrame(sui_row[['z1','su1']])
    #print(sui_row)

    #This is for getting the data of p_y
    p_y_row = pd.read_csv(number + '\\PILE'+str(frame)+'.csv', names=['ID','z1','su1'],sep='\s+')
    p_y_row = pd.DataFrame(p_y_row[['z1','su1']])


    #sui_row.sort_values(by = ['z'],ascending = True, inplace= True)


    output_odb = pd.concat([FM_matrix,intplt(Coordinate_row,sui_row,'su')], axis=1)
    output_odb = pd.concat([output_odb,intplt(Coordinate_row,p_y_row,'pile_y')],axis=1 )
    #print(output_odb)
    output_odb = pd.DataFrame(output_odb, columns = ["CutZ","Fx", 'My', 'su', 'pile_y'])
    output_odb = pd.DataFrame(output_odb.iloc[0:-1,])
    output_odb['CutZ'] = 15 - output_odb['CutZ']
    #normalisation of pile y by diameter of 0.88 m
    output_odb['pile_y'] = output_odb['pile_y']/0.88
    output_odb.sort_values(by= ['CutZ'],ascending = True, inplace= True)
    #output_odb.drop(['CutName', 'CutX', 'CutY', 'Mx', 'Mz', 'Fy', 'Fz','FrameId'], axis=1, inplace=True)
    #output_odb.to_csv('result11.csv', index=False)
    #print(output_odb)
    #print(output_odb['Fx'])
    output_odb.reset_index(inplace=True)
    output_odb['Fx_diff']=output_odb['Fx'].diff()
    output_odb['p']=output_odb['Fx'].diff()/output_odb['CutZ'].diff()
    output_odb['Nc']=output_odb['p']/output_odb['su']/0.88
    output_odb.drop(columns=['index'], inplace=True)
    return output_odb

def Todolist(start, end):
    To_do_list = []
    for i in range(start,end):
        result_list = os.listdir(str(i))
        if len(result_list) < 3:
            To_do_list.append([i,0])
        else:
            frame_num = int((len(result_list)-3)/2)
            To_do_list.append([i,frame_num])
    return To_do_list

'''
alldata = pd.DataFrame()
for n in Todolist():
    print(n[0])
    if n[1]==0:
        print('Skip')
    else:
        single_data = main_program(n[0],n[1])[['pile_y','Nc']]
        single_data.columns = [str(n[0])+' pile_y','Nc']
        alldata=pd.concat([alldata, single_data], axis=1)
alldata.to_csv('data.csv')
'''
#print(main_program(4,12))


def section_get(section_numb,number, frame):
    section = pd.DataFrame(main_program(number, frame)[['pile_y','Nc']]).iloc[section_numb,:]
    section = pd.DataFrame(section)
    #section = np.array(section)

    #section.reshape(-1,1)
    #section = pd.DataFrame(section)
    return section
def Get_Section_all(section_numb,start, end):
    section_data = pd.DataFrame()
    for n in Todolist(start, end):
        section_number_frame = pd.DataFrame()
        if n[1] == 0:
            print('skip')
        else:
            print(n[0])
            for i in range(0,n[1]+1):
                single_data = section_get(section_numb, n[0],i)
                single_data.columns = [str(i)]
                #print(single_data)
                section_number_frame = pd.concat([section_number_frame,single_data],axis=1)
            section_number_frame.index = [str(n[0]) + 'pile_y', str(n[0]) + 'Nc']
            section_data = pd.concat([section_data,section_number_frame], axis =0)
    return section_data

for i in range(1,9):
    Get_Section_all(5*i,1,201).to_csv('Data'+str(5*i)+'.csv')