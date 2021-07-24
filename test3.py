import psutil as ps


def get_users():
    res={}   
    users = ps.users()
    for name, value in users.items():
        res[name] = {
            "name": value.name,
            "terminal": value.terminal,
            "started": value.started
            }
    return res



def show (**kwargs):
    us_template = (
        "name: {name:>10}\n"
        "terminal: {terminal:>10}\n"
        "started: {started:>10}"
    )
    us_str = ""
    for name2,anyone in kwargs["users"].items():
        us_str += us_template.format(name2, anyone)
    print(us_str)




def main():
    users_data = get_users()




    show(
 users = users_data   
)


main()

