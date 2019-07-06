import os
from tqdm import tqdm as tqdm
from shutil import copyfile


count=0
rdir = '/home/jdegange/vision/MARG'
for _, dirs, _ in os.walk(rdir):
    for dir in tqdm(dirs): # Looks at  all the xml folders
        for subdir, _, files in os.walk(os.path.join(rdir,dir)):
                    for file in files:
                        if file.endswith('.tif'):
                            count = count+1
                            #clean new filename from original path                          
                            orig_fn = str(subdir)+str(file)
                            new_fn = orig_fn.replace("/","_")
                            new_fn = new_fn.replace("._","")
                            new_fn = new_fn.split("_")[-1]
                            new_fn = dir+"_"+new_fn

                            #move all files with common class from subdirs into same dir
                            old_dir =os.path.join(subdir,file)
                            new_dir =os.path.join(rdir,dir,new_fn)
                            
                            print("Moving from ", old_dir," to:",new_dir)
                            copyfile(old_dir,new_dir)



print("Finished renaming and moving {} files.".format(count))

