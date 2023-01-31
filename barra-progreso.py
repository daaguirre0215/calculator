from tqdm import tqdm
from time import sleep

tareas = ['tarea 1','tarea 2','tarea 3','tarea 4','tarea 5']

for i in tqdm(tareas):
    sleep(0.10)