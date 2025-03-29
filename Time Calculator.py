def add_time(start, duration, DayName=''):
    #1
    #get hour
    val_hour= int(start.split()[0].split(':')[0])
    val_hour_added = int(duration.split(':')[0])
    #get minute
    val_minute=int(start.split()[0].split(':')[1])
    val_minute_added = int(duration.split(':')[1])
    
    #calculate
    hour_time =  val_hour + val_hour_added
   
    minute_time = val_minute + val_minute_added 
   
    #get pm or am
    val_PM_AM = start.split()[1]
      
    #get day later
    days_total_later = hour_time // 24
    
    #get hour later
    hours_total_later = hour_time % 24    
    
    if minute_time >= 60:
        minute_time = minute_time - 60
        hour_time += 1
    
    if hour_time >= days_total_later * 24:
        hour_time -= days_total_later * 24               
        if hour_time == 0:
            hour_time=12
        elif hour_time >= 12:
            hour_time -= 12
            if hour_time==0:
                hour_time=12
            if val_PM_AM == 'AM':
                val_PM_AM = 'PM'
            else:
                print('go')
                val_PM_AM = 'AM'           
                days_total_later+=1

    
    Day_Name = ''
    if DayName !='':
        day_week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        d_check = day_week.index(DayName.lower())
        w_check = (d_check + days_total_later) % 7    
        DayName = day_week[w_check].capitalize()
        if days_total_later==1:
            Day_Name +=", "+DayName +' (next day)'
        elif days_total_later>1:
            Day_Name +=", "+DayName + " ("+str(days_total_later)+" days later)"
        else:
           Day_Name +=", "+DayName 
    else:
        if days_total_later==1:
            Day_Name +=' (next day)'
        elif days_total_later>1:
            Day_Name +=" ("+str(days_total_later)+" days later)"

    start = f'{hour_time}:{minute_time:02d} {val_PM_AM}' 
    new_time = f'{start}{Day_Name}'
    
    return new_time
    


if __name__ == "__main__":
      print(add_time('2:59 AM', '24:00', 'saturDay'))