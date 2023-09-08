import psutil
import datetime
import time

monitoring_period = 5
memory_threshold = 80

def log_system_info():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_filename = f"{current_date}-pub.log"
    notification_filename = f"{current_date}-notification.log"
    
    while True:
        try:
            # Get system information
            cpu_usage = psutil.cpu_percent()
            num_logical_cpus = psutil.cpu_count(logical=True)
            used_memory = psutil.virtual_memory().percent
            used_disk_space = psutil.disk_usage('/').percent
            current_host_ip = psutil.net_if_addrs()['eth0'][0].address  # Change 'eth0' to your network interface

            # Log system information
            with open(log_filename, 'a') as log_file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_line = f"{timestamp}, {cpu_usage}, {num_logical_cpus}, {used_memory}, {used_disk_space}, {current_host_ip}\n"
                log_file.write(log_line)

            # Check memory threshold and create a notification file if exceeded
            if used_memory > memory_threshold:
                with open(notification_filename, 'w') as notification_file:
                    notification_file.write("Low memory detected.")

            time.sleep(monitoring_period)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    log_system_info()
