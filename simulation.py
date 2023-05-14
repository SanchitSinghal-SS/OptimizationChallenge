team = {
    'a': 2000000*(1+0.1),
    'b': 1800000*(1+0.15),
    'c': 1700000*(1+0.2),
    'd': 1400000*(1+0.3),
    'e': 1575000*(1+0.25),
}

arm = 1.48

disguise = {
    'ac': [4000*(1+0.3), 60*1.1],
    'sg': [8000*(1+0.6), 60*1.15]
}

weapon = {
    'sg': [20000*(1+0.15), 1.35],
    't': [35000*(1+0.3), 1.15],
    'sd': [30000*(1+0.2), 1.25]
}

rooms = {
    0: ['mg', 650000*9, 8.5*9, 3],
    1: ['caw', 950000*6, 12*6, 4],
    2: ['ee', 900000*7, 12.5*7, 5],
    3: ['aac', 1180000*5, 14.5*5, 4],
    4: ['pal', 1450000*4, 16*4, 3],
    5: ['sr', (6000000-205000*(1+0.5)), 50, 4]
}

eff = {
    'a': [0.46, 0.51, 0.43, 0.49, 0.54, 0.56],
    'b': [0.51, 0.59, 0.46, 0.55, 0.61, 0.63],
    'c': [0.54, 0.59, 0.51, 0.57, 0.61, 0.65],
    'd': [0.6, 0.64, 0.58, 0.61, 0.69, 0.71],
    'e': [0.52, 0.57, 0.51, 0.54, 0.59, 0.64],
}

exit = {
    'c': 8850*(1+0.45),
    'h': 10800*(1+0.2)
}

tc = [['a', 'b', 'e'], ['a', 'd', 'e'],
      ['b', 'c', 'd'], ['a', 'd'], ['c', 'e'], ['b', 'c']]
max = [0,[],0,0,[]]
count = 0
for t in tc:
    for d in disguise:
        for w in weapon:
            for i in range(0, len(rooms)-2):
                for j in range(i+1, len(rooms)-1):
                    for k in range(j+1, len(rooms)):
                        for e in exit:
                            cost = 0.0
                            tim = 0.0
                            loot = 0.0
                            guards = 0
                            eff1 = 0.0
                            eff2 = 0.0
                            eff3 = 0.0
                            for mem in t:
                                cost = cost + team[mem]
                            if len(t) == 2:
                                cost = cost*arm
                            print(cost)
                            cost = cost + disguise[d][0]*len(t)
                            cost = cost + weapon[w][0]*len(t)
                            for mem in t:
                                eff1 = eff1+eff[mem][i]
                                eff2 = eff2+eff[mem][j]
                                eff3 = eff3+eff[mem][k]
                            eff1 = eff1/len(t) * rooms[i][2]
                            eff2 = eff2/len(t) * rooms[j][2]
                            eff3 = eff3/len(t) * rooms[k][2]
                            loot = rooms[i][1] + rooms[j][1] + rooms[k][1]
                            guards = rooms[i][3] + rooms[j][3] + rooms[k][3]
                            tim = tim + guards*weapon[w][1]/len(t)
                            tim = tim + (eff1 + eff2 + eff3)/len(t)
                            cost = cost + exit[e]*len(t)*tim
                            count = count +1
                            if tim<=disguise[d][1]:
                                if (loot-cost) > max[0]:
                                    max[0] = loot-cost
                                    max[1] = t
                                    max[2] = d
                                    max[3] = w
                                    max[4] = [rooms[i][0],rooms[j][0],rooms[k][0],cost, loot, tim]
print(max,count)
                        
