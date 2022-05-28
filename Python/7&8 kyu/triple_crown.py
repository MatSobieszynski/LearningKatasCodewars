receivers={
  'Cooper Kupp': 
    {
    'Receiving yards': 1786, 
    'Receiving touchdowns': 18, 
    'Receptions': 117
    },
  'Justin Jefferson': 
    {
    'Receiving yards': 1700, 
    'Receiving touchdowns': 17, 
    'Receptions': 115
    },
  'Davante Adams': 
    {
    'Receiving yards': 1650, 
    'Receiving touchdowns': 16, 
    'Receptions': 110
    }
}






def triple_crown(receivers):
    max_yards = []
    max_touchdowns = []
    max_receptions = []
    for receiver in receivers:
        max_yards.append(receivers[receiver]['Receiving yards'])
        max_touchdowns.append(receivers[receiver]['Receiving touchdowns'])
        max_receptions.append(receivers[receiver]['Receptions'])
    max_n = [max(max_yards), max(max_touchdowns), max(max_receptions)]
    for receiver in receivers:
        if (receivers[receiver]['Receiving yards'] == max_n[0] and max_yards.count(max_n[0]) ==1) and (receivers[receiver]['Receiving touchdowns'] == max_n[1] and max_touchdowns.count(max_n[1]) ==1) and (receivers[receiver]['Receptions'] == max_n[2] and max_receptions.count(max_n[2]) ==1):
            return receiver
    return 'None of them'

        
    
print(triple_crown(receivers))