import psutil as ps


def get_kekw():
    res = {}
    kekw = ps.users()
    for users, value in kekw.items():
        res[users] = {
            "users": value.users,
            "terminal": value.terminal,
        }
        return res


def show(**kwargs):
    kekw_template = (
        "users: {0:>30} \n"
        "terminal: {terminal:>20} \n"
    )


    kekw_info_str = ""
    for users, value in kwargs["kekw"].items():
        kekw_info_str += kekw_template.format(users, **value)
    print(kekw_info_str)

def main():
    kekw_data = get_kekw()
    show(
        kekw = kekw_data,

    )


if __name__ == "__main__":
    main()

