import pandas as pd 
import glob 
import os


def append_all_files(filename):
    data = pd.read_csv(filename)


    print(data)  
    return data

if __name__ == "__main__":
    append_all_files('/Users/Bowen/Downloads/Project_1/automate_report/data/sales_product_data/Sales_April_2019.csv')

  #def __append_all_files(extension, directory):
  #all_filenames = [i for i in glob.glob('{directory}/*.{ext}'.format(directory=directory, ext=extension))]

    #combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)

    #combined_csv.drop(combined_csv[combined_csv['Quantity Ordered'] == 'Quantity Ordered'].index, inplace=True)

#return