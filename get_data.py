
from netmiko import ConnectHandler
from datetime import datetime
import csv


now = str(datetime.now().strftime("%Y-%m-%d %H:%M")) #%Y-%m-%d, %H:%M:%S

switch_num = 1 # Count node number

success = 0  
fail = 0

with open('switch_backup2.csv', 'a', newline='') as f:
    write = csv.writer(f)
    #write.writerow(['Total', 'Status', 'Hosts', 'Date'])

    with open('ip.txt') as switches:
        for ip in switches:
            print('Backing up configuration SW'+ str(switch_num) + ' ' + ip)
            print('.....')
            print(' ')
            SW = {
                'device_type':'cisco_ios',
                'ip':ip,
                'username':'admin',
                'password':'vnpro',
                'secret':'cisco'
            }
            try:
                ssh = ConnectHandler(**SW)      

            except:
                print('~ Backup failed !!! , check error in file backup_error.log ~')
                print('\n')
                
                # write in log file
                with open("backup_error.log", 'a') as logf:
                    logf.write('Backup Failed on ')
                    logf.write(now)
                    logf.write(" - Cannot connect via SSH or Telnet to SW")
                    logf.write(str(switch_num))
                    logf.write(' ')
                    logf.write(ip)
                    logf.write('\n')
                sw_name = 'SW' + str(switch_num)
                ###write.writerow([sw_name, switch_num, ip, 'failed', now])

                fail += 1
                switch_num += 1 
                
                continue
            
            ssh.enable()
            position = ssh.find_prompt() #=> SW1 
            # backup file
            sw_name=position[:-1]   #  -> SW1     
            filename = sw_name + '.txt'
            
            show_run = ssh.send_command('show running-config')   
            
            with open(filename, "w") as log_file:
                log_file.write("#"*26)
                log_file.write(' DATE: '+ now + ' ')
                log_file.write("#"*26 + '\n')
                log_file.write(show_run)
            print('~ Successful !! ~')
            print('\n')
            # write
            ###write.writerow([sw_name, switch_num, ip, 'successful', now])
            switch_num += 1
            success += 1
        
        #write.writerow(['Hosts', 'Status','Count' 'Date'])
        write.writerow([switch_num - 1, 'successful', success, now])
        write.writerow([switch_num - 1, 'failed', fail, now])

        print('*'*35+' DONE!!! '+'*'*35)
        print("-> Successful:",success)
        print("-> Failed:",fail)
        

