def tempo_to_kmh(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    
    if total_seconds==0:
        return 0
    else:
        return round(3600/total_seconds,2)

def kmh_to_tempo(kmh):
    if kmh==0:
         return([0.0,0.0])
    else:
        minutes = 60 / kmh
        whole_minutes = int(60 // kmh)
        seconds = int((minutes - whole_minutes)*60)
        return([whole_minutes, seconds]) 
         

def target_to_speed(km, minutes):
    if minutes==0:
        return {'kmh':0, 'tempo':[0,0]}
    else:
        km_per_minute = km / minutes
        
        kmh = round(km_per_minute * 60,2)
        
        return {'kmh':kmh, 'tempo':kmh_to_tempo(kmh)}

