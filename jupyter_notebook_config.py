c = get_config()  # type: ignore # This line is not needed if you directly set attributes as shown above

# Allow remote access
c.ServerApp.allow_remote_access = True

# Bind to all IP addresses
c.ServerApp.ip = '0.0.0.0'

# Set the port to 8888 or another port you prefer
c.ServerApp.port = 8888

# Do not open a browser window by default
c.ServerApp.open_browser = False

# Disable authentication
c.ServerApp.token = ''  # No token required
c.ServerApp.password = ''  # No password required
