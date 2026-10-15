def give_role(user, role, roles=None):
    if roles is None:
        roles = []
    roles.append(role)
    return {"user": user, "roles": roles}

admin = give_role("ali", "admin")

print(admin)
editor = give_role("sara", "editor")


print(editor)
 



team = ["ali", "sara", "john"]
backup = None
if backup is None:
    backup = team.copy()
team.append("mike")
print(backup)



assert admin["roles"] == ["admin"]
assert editor["roles"] == ["editor"]


assert backup == ["ali", "sara", "john"]
assert team == ["ali", "sara", "john", "mike"]


print("All assertions passed successfully!")