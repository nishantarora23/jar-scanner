import os
import main

# Check if report directory is available or not

report_dir = os.path.join(main.current_dir, "Report")
if os.path.exists(report_dir):
    os.chdir(report_dir)
else:
    os.chdir(main.current_dir)
    os.mkdir("Report")
    os.chdir(report_dir)
