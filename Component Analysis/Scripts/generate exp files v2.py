#generate exp files
#This will delete all files currently in Documents/LRI CFD/NX/EXP
#Step 1: Open expressions table and find the name and unit of the parameters to be changed. 
#Step 2: Type in unit type exactly (MilliMeter,Meter,Feet,Inch,Degrees) for each parameter

#Step 3: Type desired decimal precision
precision = 3 #number of decimals

#Step 4: Fill out parameters and steps
#Min value, max value (inclusive) and step size 
parameter = 'deflection_angle'
min = 0
max = 30
step = 5
units = 'Degrees'   #MilliMeter,Meter,Feet,Inch,Degrees

#Inlet Velocity: (m/s)
inletmin = 50
inletmax = 200
inletstep = 50
#Step 5: Run code


import os
def delete_files_in_folder(folder_path):
    #Delete all files in the specified folder.
    #:param folder_path: The path to the folder from which files will be deleted.
    if os.path.exists(folder_path) and os.path.isdir(folder_path):     # Check if the folder exists
        # Iterate over all the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file (not a subfolder)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        print(f"The folder {folder_path} does not exist or is not a directory.")

#User's folder path generated from folder structure script        
user_home = os.path.expanduser("~")
path = os.path.join(user_home, "Documents","LRI CFD","NX","EXPS","")
delete_files_in_folder(path)

def float_range(start,stop,step):
    #equivalent to numpy.arange(start,stop+step,step)
    #inclusive of both start and stop
    while start<stop+step:
        yield round(start,precision)
        start += step

count = 0
for v in float_range(inletmin,inletmax,inletstep):
    for i in float_range(min,max,step):
        count += 1
        outputpath = f'{path}{v:03}m_s_{i:02}deg'
        text = f"// Version:  3\n[{units}]{parameter}={i}"
        with open(f"{outputpath}.exp",'w') as f:
                f.write(text)
                f.close()
print(f"Succesfully created {count} files in {path}")