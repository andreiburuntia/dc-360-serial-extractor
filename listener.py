import serial
import select
import json

map_of_meaning = {
    'Bt': 'Body Type',
    'GE': 'Gender',
    'AG': 'Age',
    'Hm': 'Height (cm)',
    'Pt': 'Clothes Weight (kg)',
    'Wk': 'Weight (kg)',
    'FW': 'Fat %',
    'fW': 'Fat Mass (kg)',
    'MW': 'FFM (kg)',
    'mW': 'Muscle Mass (kg)',
    'sW': 'Visceral Fat Rating', #?
    'bW': 'Bone Mass (kg)',
    'wW': 'TBW (kg)',
    'ww': 'TBW %',
    'MI': 'BMI',
    'Sw': 'Sw - ?', #?
    'OV': 'OV - ?', #?
    'IF': 'IF - ?', #?,
    'rb': 'BMR (kJ)',
    'rB': 'BMR (kcal)',
    'rJ': 'rJ - ?', #?
    'rA': 'rA - ?', #?
    'UF': 'Bioelectrical R1',
    'VF': 'Bioelectrical X1',
    'RF': 'Bioelectrical R2',
    'XF': 'Bioelectrical X2',
    'CS': 'CS'
}

com_port = 'COM4'
baud_rate = 9600
timeout = 60

conn = serial.Serial(com_port, baud_rate, timeout=timeout)
msg = conn.readline()
#f = open('out', 'wb')
#f.write(msg)
#f.close()

#f = open('out', 'rb')
#msg = f.readline()

stringified = msg.decode("utf-8")

raw = "Bt" + stringified.split("Bt",1)[1]

val_list = raw.split(',')

keys = val_list[::2]
vals = val_list[1::2]

res_dict = {}

ind=0
for key in keys:
    res_dict[map_of_meaning[key]] = vals[ind]
    ind+=1

print(json.dumps(res_dict))