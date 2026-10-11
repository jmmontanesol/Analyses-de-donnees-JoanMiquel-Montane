camps = [3600, 4400, 5300, 6100]

for altitude in camps:
    if altitude < 5000:
        print("Camp de basse altitude:", altitude)
    elif altitude >= 5000:
        print("Camp de haute altitude:", altitude)