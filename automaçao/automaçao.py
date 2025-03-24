import pyautogui as pt
import time as tm

# Pausar antes de começar
tm.sleep(2)

# Listas com os nomes dos produtos e quantidades
produtos = ["Brahma", "Coca-Cola", "Heineken", "Pepsi"]
quantidades = [1, 2, 3, 4]

# Iterar sobre as listas de produtos e quantidades
for produto, quantidade in zip(produtos, quantidades):
    pt.press("n")  # Pressiona "n" para adicionar novo item
    tm.sleep(1)
    pt.click(x=417, y=290)  # Clique na área onde o nome do produto deve ser digitado
    tm.sleep(0.5)
    pt.press("tab")  # Navega para o campo do nome do produto
    tm.sleep(0.5)
    pt.write(produto)  # Escreve o nome do produto
    tm.sleep(0.5)
    pt.press("tab")  # Navega para o campo de quantidade
    tm.sleep(0.5)
    pt.write(str(quantidade))  # Escreve a quantidade
    tm.sleep(0.5)
    pt.press("enter")  # Pressiona enter para adicionar o produto
    tm.sleep(0.5)
    pt.press("enter")  # Confirma a adição do produto

# Fim da automação