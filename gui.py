from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Aimlabs Graph")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def sqScore(*args):
    hits = float(hitsText.get())
    shots = float(shotsText.get())
    target = float(targetText.get())
    score = round(hits * math.sqrt((hits/shots)*100))
    scoreText.set(f'Score: {score}')
    misses = shots - hits
    i = 0

    # Hits +1
    while target > score: 
        i += 1
        score = (hits + i) * math.sqrt(((hits + i)/shots)*100)
    else:
        convertedText.set(f'Converted Hits: {i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0
    
    # Hits, Shots +1
    while target > score: 
        i += 1
        score = (hits + i) * math.sqrt(((hits + i)/(shots + i))*100)
    else:
        newHitsText.set(f'New Hits: {i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0

    # Shots -1
    while target > score: 
        i += 1
        score = (hits) * math.sqrt((hits/(shots - i))*100)
        if (shots - i) < hits:
            score = hits * math.sqrt((hits/shots)*100)
            fewerMissesText.set(f'Fewer Misses: N/A')
    else:
        fewerMissesText.set(f'Fewer Misses: {i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0

    # tableShots = [x for x in range(int(target/10), (round(1.25 * (target/10))))]
    # tableHits = [math.ceil((target/10)**(2/3) * x**(1./3)) for x in tableShots]
    
    # targetTable = pd.DataFrame({"Hits": tableHits, "Shots": tableShots})
    # targetTable = targetTable.assign(Accuracy=100 * round(targetTable["Hits"]/targetTable["Shots"], 3)).set_index("Shots")
    # print(targetTable)

hitsText = StringVar()
shotsText = StringVar()
targetText = StringVar()

scoreText = StringVar()
convertedText = StringVar()
newHitsText = StringVar()
fewerMissesText = StringVar()


hitsEntry = ttk.Entry(mainframe, width=7, textvariable=hitsText).grid(column=2, row=2, sticky=W)
shotsEntry = ttk.Entry(mainframe, width=7, textvariable=shotsText).grid(column=2, row=3, sticky=W)
targetEntry = ttk.Entry(mainframe, width=7, textvariable=targetText).grid(column=2, row=1, sticky=W)

scoreDisplay = ttk.Label(mainframe, textvariable=scoreText).grid(column=1, row=4, sticky=W)
convertedDisplay = ttk.Label(mainframe, textvariable=convertedText).grid(column=1, row=5, sticky=W)
newHitsDisplay = ttk.Label(mainframe, textvariable=newHitsText).grid(column=1, row=6, sticky=W)
fewerMissesDisplay = ttk.Label(mainframe, textvariable=fewerMissesText).grid(column=1, row=7, sticky=W)

ttk.Label(mainframe, text="Hits").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Shots").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Target").grid(column=1, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=sqScore).grid(column=3, row=7, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
root.bind("<Return>", sqScore)

root.mainloop()