import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) #Já que é um Tuple no args, se só tiver um argumento tem que terminar o tuple com uma vírgula ',' para deixar o Python saber que é um tuple (Ex.: args ==("Scooby", ) ), caso contrário dá erro.
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
# Os joins fazem esperar a thread acabar o que tá fazendo para continuar com o restante do programa, se não tivesse isso, ia dar o print e depois printar as tarefas quando elas forem concluídas, dá mais rápida até mais demorada

print("All chores are complete!")