fd = open('315M')
data = fd.read()

entries = data.split('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')[1:]

tpms = {}

for entry in entries:
    lines = entry.split('\n')
    if 'TPMS' in lines[2]:
        date = lines[1].split()[2]
        time = lines[1].split()[3]
        pair = lines[2].split()[2] +','+ lines[2].split()[-1]
        if pair in tpms:
            if date in tpms[pair]:
                tpms[pair][date].append(time)
            else:
                tpms[pair][date] = [time]
        else:
            tpms[pair] = {date:[time]}

for k,v in sorted(tpms.items()):
    count = 0
    summary = []
    for k2,v2 in v.items():
        count += len(v2)
        summary.append(str(k2 + ': ' + str(len(v2))))
    summary = ','.join(summary)
    print(k,' \tcount:',count,'\t',summary)
