import psutil as ps

def get_disk():
    res = {}
    disk = ps.disk_partitions(all=True)
    for disk, mem in disk.items():
        res[disk] = {
            "device": mem.device,
            "fstype": mem.fstype,
            "opts": mem.opts,
        }
    return res



get_disk()
        


# def show(**kwargs):


# def main():
#     disk_data = get_disk()

#     show(
#         disk = disk_data
#     )
# if __name__ == "__main__":
#     main()