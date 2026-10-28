with open('_portal_generators/it_sections_u6.py', 'r', encoding='utf-8') as f:
    u6 = f.read()

pos1 = u6.find('id="it6-mobile-security"')
pos2 = u6.find('id="it6-safety-operational"')
pos3 = u6.find('id="sec31-arith"')

print("Mobile security length:", pos2 - pos1)
print("Safety operational length:", pos3 - pos2)
