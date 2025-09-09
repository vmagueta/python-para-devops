data = {"servers": ["web01", "web02", "db01"]}
failed_servers = []

for server in data["servers"]:
    if "db" in server:
        failed_servers.append(server)
