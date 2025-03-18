from datetime import datetime

dthr_at = datetime.now()
dt_txt = dthr_at.strftime('%d/%m/%Y')
hr_txt = dthr_at.strftime('%H:%M')
print(f"Data: {dt_txt} Hora: {hr_txt} ")





