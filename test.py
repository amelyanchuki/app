import psutil as ps

def get_cpu():
    res = {}
    cpu_time = ps.cpu_times(percpu=True)
    res["time"] = {}
    for index, core in enumerate(cpu_time):
        res["time"][f"core_{index}"] = (core.user, core.system)
    res["load"] = ps.cpu_percent(percpu=True, interval=0.3)
    return res




def get_virtual_memory():
    res = {}
    vir_mem = ps.virtual_memory()
    print(vir_mem)
    return res



def swap_memory():
    res = {}
    swap_mem = ps.swap_memory()
    print(swap_mem)
    return(res)




def get_users():
    res={}   
    us = ps.users()
    for us in enumerate(us):
        print(us)
    return res



def get_disk():
    res = {}
    disk = ps.disk_partitions()
    for disk in enumerate(disk):
        print(disk)
    disk_usage = ps.disk_usage("/")
    print(disk_usage)
    return res






def get_network():
    res = {}
    network = ps.net_io_counters(pernic=True)
    for inter, value in network.items():
        res[inter] = {
            "bytes_sent": value.bytes_sent,
            "bytes_recv":value.bytes_recv, 
            "errin":value.errin, 
            "errout":value.errout
            }
    return res




def show(**kwargs):
    cpu_time_template = "User time for {0} {1:>10},\tsystem time for {0} {2:>10}\n"
    cpu_time_str = ""
    cpu = kwargs["cpu"]
    for key, value in cpu["time"].items():
        cpu_time_str += cpu_time_template.format(key, *value)
    print(cpu_time_str)

    net_info_template = (
    "Interface: {0:>10} ->\n"
    "bytes_sent: {bytes_sent:>15}\n"
    "bytes_recv: {bytes_recv:>15}\n"
    "errin: {errin:>20}\n"
    "errout: {errout:>19}\n"
)
 
    net_info_str = ""
    for name, value in kwargs["network"].items():
        net_info_str +=net_info_template.format(name, **value)
    print(net_info_str) 



def main():
    cpu_data = get_cpu()
    vir_mem_data = get_virtual_memory()
    swap_mem_data = swap_memory()
    users_data = get_users()
    disk_data = get_disk
    network_data = get_network()
    



    show(
        cpu=cpu_data,
        virt_mem = vir_mem_data,
        swap_memo = swap_mem_data,
        users = users_data,
        disk = disk_data,
        network = network_data
    


   )

if __name__ == "__main__":
    main()