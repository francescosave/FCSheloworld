# Hello world in Javascript,Python e C#.

Questo progetto formativo prevede la scrittura di un hello world 
in tre linguaggi di programmazione analizzando alcuni aspetti 
principali della programmazione.

- utilizzo di vscode
- scrittura in markdown
- scripting in python per strutturare il progetto utilizzando efficaciemente una funzione,ciclando su un array e loggando il flusso ed eventuali errori
s
realizzare i 3 helloworld easy nei tre linguaggi che mandano a schermo la stringa hello world

Hello world sarà realizzato utilizzando vscode come editor quindi senza l'utilizzo di ide visuali
automatizzando atrtraverso il codice il più possibile.

``` python
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

# creae un file javascript,un file python e un progetto C#



# By setting exist_ok as True
# error caused due already
# existing directory can be suppressed
# but other OSError may be raised
# due to other error like
# invalid path name

```

1. Cloniamo la repo con il 
  ```git clone git@github.com:francescosave/FCSheloworld.git```

3. Eseguiamo il download di vsCode,Python,Node.Js e C#

2. Documentiamo tutto in questo file redme.md

3. Relizziamo lo script phython che ci permette di creare automaticamente la struttura del progetto 



<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>




---
> Note: Vedere pip e le virtualenv di python.Come loggare il flusso e gli errori dell'init








