def defang(s: str) -> str:
    return f"{s} defanged = {s.replace('.', '[.]')}"


print(defang("127.0.0.1"))