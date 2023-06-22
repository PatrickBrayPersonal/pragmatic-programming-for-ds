# Coupled 👎
class Ian:
    ...

    def book_happy_hour_at_highline(self, highline):
        highline.employees.get("jeff").send_email("we need a table")


# Decoupled 👍
class Ian:
    ...

    def book_happy_hour_at_highline(self, highline):
        highline.message("we need a table")
