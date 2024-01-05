{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib as plt\n",
    "import numpy as np\n",
    "import tkinter as tk\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Global Functions\n",
    "def sqScore(hits, shots, target):\n",
    "    score = round(hits * math.sqrt((hits/shots)*100))\n",
    "    print(f'Score: {score}')\n",
    "    misses = shots - hits\n",
    "    i = 0\n",
    "\n",
    "    # Hits +1\n",
    "    while target > score: \n",
    "        i += 1\n",
    "        score = (hits + i) * math.sqrt(((hits + i)/shots)*100)\n",
    "    else:\n",
    "        print(f'Converted Hits: {i}')    \n",
    "        score = hits * math.sqrt((hits/shots)*100)\n",
    "        i = 0\n",
    "    \n",
    "    # Hits, Shots +1\n",
    "    while target > score: \n",
    "        i += 1\n",
    "        score = (hits + i) * math.sqrt(((hits + i)/(shots + i))*100)\n",
    "    else:\n",
    "        print(f'New Hits: {i}')    \n",
    "        score = hits * math.sqrt((hits/shots)*100)\n",
    "        i = 0\n",
    "\n",
    "    # Shots -1\n",
    "    while target > score: \n",
    "        i += 1\n",
    "        score = (hits) * math.sqrt((hits/(shots - i))*100)\n",
    "        if (shots - i) < hits:\n",
    "            score = hits * math.sqrt((hits/shots)*100)\n",
    "            break\n",
    "    else:\n",
    "        print(f'Fewer Misses: {i}')    \n",
    "        score = hits * math.sqrt((hits/shots)*100)\n",
    "        i = 0\n",
    "\n",
    "    tableShots = [x for x in range(int(target/10), (round(1.25 * (target/10))))]\n",
    "    tableHits = [math.ceil((target/10)**(2/3) * x**(1./3)) for x in tableShots]\n",
    "    \n",
    "    targetTable = pd.DataFrame({\"Hits\": tableHits, \"Shots\": tableShots})\n",
    "    targetTable = targetTable.assign(Accuracy=100 * round(targetTable[\"Hits\"]/targetTable[\"Shots\"], 3)).set_index(\"Shots\")\n",
    "    print(targetTable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "window = tk.Tk()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dev",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
