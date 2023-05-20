# Python program to explain os.makedirs() method

# importing os module
import os

# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists
# But It can be suppressed by
# setting the value of a parameter
# exist_ok as True


def makedirs(nameDir):
    # Directory
    directory = nameDir

    # Parent Directory path
    parent_dir = "readme/"

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'Nikhil'
    try:
        os.makedirs(path, exist_ok = False)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)


# ciclare questa parte qui
makedirs('js')
makedirs('python')


# By setting exist_ok as True
# error caused due already
# existing directory can be suppressed
# but other OSError may be raised
# due to other error like
# invalid path name
