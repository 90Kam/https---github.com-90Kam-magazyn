import os
from datetime import datetime

now = datetime.now()

date = now.strftime('%Y - %m - %d')

folder_name = f"{date}"
os.mkdir(folder_name)

report_name = f"report.html"
report_path = os.path.join(folder_name, report_name)
with open (report_path, 'w') as f:
    f.write('This is the report for today')

print(f"Folder '{folder_name}' and report file '{report_name}' have been created")