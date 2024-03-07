import pandas as pd

data = pd.read_csv("DataSet/Iris.csv")
data2 = data.drop("Id", axis=1)
data3 = data2.drop("Species", axis=1)
columns = list(data3)
data_var = []
distance_var = []
my_data = pd.read_csv("DataSet/test_data.csv")
my_data2 = my_data.drop("Id", axis=1)
my_data3 = my_data2.drop("Species", axis=1)
result=[]
for k in range(0, 11):
    for i in range(0, 140):
        for j in columns:
            elem = data2[j][i]
            data_var.append(elem)
        distance = ((my_data2[columns[0]][k]-data_var[0])**2 + (my_data2[columns[1]][k]-data_var[1])**2 + (my_data2[columns[2]][k]-data_var[2])**2 + (my_data2[columns[3]][k]-data_var[3])**2)**0.5
        distance_var.append(distance)
        data_var = []
    if len(distance_var) % 140 == 0:
        result.append(distance_var)
        distance_var=[]
for i in range(0,11):
    print(str(i)+"=")
    knn = pd.DataFrame(result[i])
    knn["SepalLengthCm"] = data2["SepalLengthCm"]
    knn["SepalWidthCm"] = data2["SepalWidthCm"]
    knn["PetalLengthCm"] = data2["PetalLengthCm"]
    knn["PetalWidthCm"] = data2["PetalWidthCm"]
    knn["Species"]=data2["Species"]
    print(knn.nsmallest(12,[0]))
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    """)
