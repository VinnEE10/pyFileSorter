import os
import shutil

#Simple program that allow you to sort given the right directories
#sourcepath is the origin point or where it will be searching for files
#variables with 'End' is your end destination
#to modify change the directory according to your PC 
#This isnt mine tho I just found this on stack overflow :/
sourcepath='C:/Users/Vincent/Downloads'
sourcefiles = os.listdir(sourcepath)
destinationpath = 'C:/Users/Vincent/Downloads/end'
imageEnd = 'C:/Users/Vincent/Downloads/images'
isoEnd = 'C:/Users/Vincent/Downloads/iso'
exeEnd = 'C:/Users/Vincent/Downloads/exe'
pdfEnd = 'C:/Users/Vincent/Downloads/pdf'
zipEnd = 'C:/Users/Vincent/Downloads/zip'
vidEnd = 'C:/Users/Vincent/Downloads/vid'
other = 'C:/Users/Vincent/Downloads/other' 
for file in sourcefiles:
    #images
    if file.endswith('.jpg'): #This catches the file you want to sort
        shutil.move(os.path.join(sourcepath,file), os.path.join(imageEnd,file))
        #here sourcepath is the origin and the variable imageEnd is the destination
    elif file.endswith('.png'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(imageEnd,file))
    elif file.endswith('.PNG'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(imageEnd,file)) 
    
    
    #vids
    elif file.endswith('.mov'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(vidEnd,file))
    elif file.endswith('.mp4'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(vidEnd,file))
    
    
    #text files
    elif file.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    elif file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(pdfEnd,file))
    
    

    
    #others
    elif file.endswith('.iso'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(isoEnd,file))
    elif file.endswith('.exe'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(exeEnd,file))
    
    #zips rars
    elif file.endswith('.zip'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(zipEnd,file))
    elif  file.endswith('.ZIP'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(zipEnd,file))
    elif  file.endswith('.rar'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(zipEnd,file))

            
