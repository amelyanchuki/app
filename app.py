import psutil as ps

def get_cpu():
    res = {}
    cpu_time = ps.cpu_times(percpu=True)
    res["time"] = {}
    for index, core in enumerate(cpu_time):
        res["time"][f"core_{index}"] = (core.user, core.system)
    res["load"] = ps.cpu_percent(percpu=True, interval=0.3)
    return res

def get_disk():
    ...


def show(**kwargs):
    cpu_time_template = "User time for {0} {1:>10}, \tsystem time for {0} {2:>10}\n"
    cpu_time_str = ""
    cpu = kwargs["cpu"]
    for key, value in cpu["time"].items():
        cpu_time_str += cpu_time_template.format(key, *value)
    print(cpu_time_str)


def main():
    cpu_data = get_cpu()
    disk_data = get_disk()


    show(
        cpu=cpu_data,
        disk = disk_data
    )

if __name__ == "__main__":
    main()
