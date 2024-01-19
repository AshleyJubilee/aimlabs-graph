from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Aimlabs Graph")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def clearText():
    convertedText.set(f'')
    newHitsText.set(f'')   
    fewerMissesText.set(f'')
    tableShotsStr.set(f'')
    tableHitsStr.set(f'')
    tableAccStr.set(f'')
    return

def sqScore(*args):
    try: 
        hits = float(hitsText.get())
        shots = float(shotsText.get())
        target = float(targetText.get())
    except: 
        scoreText.set('Error')
        clearText()
        return
    
    if shots < hits:
        scoreText.set('Error')
        clearText()
        return

    score = round(hits * math.sqrt((hits/shots)*100))
    scoreText.set(f'{score}')
    misses = shots - hits
    i = 0

    # Hits +1
    while target > score: 
        i += 1
        score = (hits + i) * math.sqrt(((hits + i)/shots)*100)
    else:
        convertedText.set(f'{i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0
    
    # Hits, Shots +1
    while target > score: 
        i += 1
        score = (hits + i) * math.sqrt(((hits + i)/(shots + i))*100)
    else:
        newHitsText.set(f'{i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0

    # Shots -1
    while target > score: 
        if hits * 10 < target:
            fewerMissesText.set(f'N/A')
            break
        i += 1
        score = hits * math.sqrt((hits/(shots - i))*100)
        if (shots - i) < hits:
            score = hits * math.sqrt((hits/shots)*100)
            fewerMissesText.set(f'N/A')
    else:
        fewerMissesText.set(f'{i}')    
        score = hits * math.sqrt((hits/shots)*100)
        i = 0

    tableHits = [x for x in range(int((target//10)), int((target//10) + 15))]
    tableShots = [math.ceil(x**(3/2) / (target//10)**(1/2)) for x in tableHits]
    tableAcc = [f'{round(((x/y)*100), 1)}%' for x, y in zip(tableHits, tableShots)]

    tableShotsStr.set("\n".join(str(x) for x in tableShots))
    tableHitsStr.set("\n".join(str(x) for x in tableHits))
    tableAccStr.set("\n".join(str(x) for x in tableAcc))
 

hitsText = StringVar()
shotsText = StringVar()
targetText = StringVar()

scoreText = StringVar()
convertedText = StringVar()
newHitsText = StringVar()
fewerMissesText = StringVar()


ttk.Label(mainframe, text="Target").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Hits").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Shots").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Score:").grid(column=1, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Converted Hits:").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, text="New Hits:").grid(column=1, row=6, sticky=(W, E))
ttk.Label(mainframe, text="Fewer Misses:").grid(column=1, row=7, sticky=(W, E))

targetEntry = ttk.Entry(mainframe, width=7, textvariable=targetText).grid(column=2, row=1, sticky=W)
hitsEntry = ttk.Entry(mainframe, width=7, textvariable=hitsText).grid(column=2, row=2, sticky=W)
shotsEntry = ttk.Entry(mainframe, width=7, textvariable=shotsText).grid(column=2, row=3, sticky=W)

scoreDisplay = ttk.Label(mainframe, textvariable=scoreText).grid(column=2, row=4, sticky=W)
convertedDisplay = ttk.Label(mainframe, textvariable=convertedText).grid(column=2, row=5, sticky=W)
newHitsDisplay = ttk.Label(mainframe, textvariable=newHitsText).grid(column=2, row=6, sticky=W)
fewerMissesDisplay = ttk.Label(mainframe, textvariable=fewerMissesText).grid(column=2, row=7, sticky=W)

ttk.Button(mainframe, text="Calculate", command=sqScore).grid(column=1, row=8, sticky=W)

ttk.Label(mainframe, text="Hits").grid(column=3, row=1, sticky=(W), padx=10)
ttk.Label(mainframe, text="Shots").grid(column=4, row=1, sticky=(W), padx=10)
ttk.Label(mainframe, text="Acc. %").grid(column=5, row=1, sticky=(W), padx=10)

canvas = Canvas(mainframe, width=50, height=250, bg='#33393b', highlightthickness=0)
canvas2 = Canvas(mainframe, width=50, height=250, bg='#33393b', highlightthickness=0)
canvas3 = Canvas(mainframe, width=50, height=250, bg='#33393b', highlightthickness=0)

tableHitsStr = StringVar()
tableShotsStr = StringVar()
tableAccStr = StringVar()
hitsDisplay = ttk.Label(canvas, textvariable=tableHitsStr)
shotsDisplay = ttk.Label(canvas2, textvariable=tableShotsStr)
accDisplay = ttk.Label(canvas3, textvariable=tableAccStr)

canvas.grid(column=3, row=2, rowspan=10, sticky=W)
canvas2.grid(column=4, row=2, rowspan=10, sticky=W)
canvas3.grid(column=5, row=2, rowspan=10, sticky=W)

canvas.create_window(0, 0, anchor='nw', window=hitsDisplay)
canvas2.create_window(0, 0, anchor='nw', window=shotsDisplay)
canvas3.create_window(0, 0, anchor='nw', window=accDisplay)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
root.bind("<Return>", sqScore)
root.resizable(False, False)

root.tk.call('lappend', 'auto_path', 'awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')

s = ttk.Style()
s.theme_use('awdark')

root.mainloop()
