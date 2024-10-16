import os
import numpy as np

#generate exp files
#Step 1: Open expressions table and find the name and unit of the parameters to be changed. 
#Step 2: Type in unit type exactly (MilliMeter,Meter,Feet,Inch,Degrees) for each parameter

#Step 3: Type desired decimal precision and output filepath ending with / ("C:/LRI/Exp/")
precision = 3 #number of decimals
user_home = os.path.expanduser("~")
path = os.path.join(user_home, "Documents","LRI CFD","NX","EXPS","")
#Step 4: Fill out parameters and steps
#Make parameter string '' to use less parameters. Only have blank parameters after filled ones
#Min value, max value (inclusive) and step size 
#parameter 1
p1 = 'angle1'
min1 = 50
max1 = 140
stp1 = 1
units1 = 'Degrees'

#parameter 2
p2 = ''
min2 = 90
max2 = 110
stp2 = 5
units2 = 'Degrees'

#parameter 3
p3 = ''
min3 = 90
max3 = 110
stp3 = 5
units3 = 'Degrees'

#parameter 4
p4 = ''
min4 = 90
max4 = 110
stp4 = 15
units4 = 'Degrees'

#parameter 5
p5 = ''
min5 = 1
max5 = 2
stp5 = 1
units5 = 'Degrees'

def delete_files_in_folder(folder_path):
    """
    Delete all files in the specified folder.
    
    :param folder_path: The path to the folder from which files will be deleted.
    """
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Iterate over all the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file (not a subfolder)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        print(f"The folder {folder_path} does not exist or is not a directory.")

delete_files_in_folder(path)

for i in np.arange(min1,max1+stp1,stp1):
    i = round(i,precision)
    outputpath1 = f'{path}'
    text1 = f"// Version:  3\n[{units1}]{p1}={i}"
    outputpath1 += f'{p1}_{i}'
    if p2 != '':
        for j in np.arange(min2,max2+stp2,stp2):
            j = round(j,precision)
            text2 = text1 + f"\n[{units2}]{p2}={j}"
            outputpath2 = f'{outputpath1}-{p2}_{j}'
            if p3 != '':
                for k in np.arange(min3,max3+stp3,stp3):
                    k = round(k,precision)
                    text3 = text2 + f"\n[{units3}]{p3}={k}"
                    outputpath3 = f'{outputpath2}-{p3}_{k}'
                    if p4 != '':
                        for l in np.arange(min4,max4+stp4,stp4):
                            l = round(l,precision)
                            text4 = text3 + f"\n[{units4}]{p4}={l}"
                            outputpath4 = f'{outputpath3}-{p4}_{l}'
                            if p5 != '':
                                for m in np.arange(min5,max5+stp5,stp5):
                                    m = round(m,precision)
                                    text5 = text4 + f"\n[{units5}]{p5}={m}"
                                    outputpath5 = f'{outputpath4}-{p5}_{m}'
                                    with open(f"{outputpath5}.exp",'w') as f:
                                        f.write(text5)
                                        f.close()
                            else:
                                with open(f"{outputpath4}.exp",'w') as f:
                                    f.write(text4)
                                    f.close()
                    else:
                        with open(f"{outputpath3}.exp",'w') as f:
                            f.write(text3)
                            f.close()
            else:
                with open(f"{outputpath2}.exp",'w') as f:
                    f.write(text2)
                    f.close()
    else:
        with open(f"{outputpath1}.exp",'w') as f:
            f.write(text1)
            f.close()

