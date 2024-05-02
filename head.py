import os

def title(subjek):
    print(' ' * int((47 - len(subjek)) /2) + subjek)
    
def head(program = str):
    os.system('cls')
    title(program)
    title("by: Taka.py")
    print(f"{'='*47}\n")