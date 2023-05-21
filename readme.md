# Hello world in Javascript,Python e C#.

Questo progetto formativo prevede la scrittura di un hello world 
in tre linguaggi di programmazione analizzando alcuni aspetti 
principali della programmazione che un dev dovrebbe conoscere.

- utilizzo di uno strumento di base come vscode
- scrittura di un file di testo ma formattato in markdown
- scripting in python per strutturare il progetto utilizzando efficaciemente una funzione,ciclando su un array e loggando il flusso ed eventuali errori
- realizzare i 3 applicativi helloworld easy nei tre linguaggi che mandano a schermo la stringa hello world linguaggio
- Versioniamo il tutto nella nostra repository remota
- Scriveremo dei test di base
- Scriveremo la documentazione di base per qualsiasi utente voglia utilizzare la nostra applicazione
- Scrivere l'applicazione in ambito web

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
  oppure con
  ```git clone https://github.com/francescosave/FCSheloworld.git```

3. Eseguiamo il download di .Net SDK 6,git,Python,Node.Js e vsCode.

2. Documentiamo tutto in questo file redme.md

3. Relizziamo lo script phython che ci permette di creare automaticamente la struttura del progetto 

4. Lanciamo lo script python loggando l'output dello schermo su un file ``` py .\init.py > log-init.txt```



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








