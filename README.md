# Copilot Proxy Demo

A demo repo to show what Copilot sends to GitHub, inspired by https://code.kiwi.com/articles/cautiously-configuring-copilot/

## Man-in-the-Middle Proxy

Start the [mitmproxy](https://hub.docker.com/r/mitmproxy/mitmproxy/) container with the following command:

```bash
docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy
```

This will open a window that shows you all traffic that goes through the proxy.

## Configure Copilot

Install the Copilot extension for your editor the way you usually do, and then configure the proxy settings.

### Vim/Neovim

1. Edit the `~/.vimrc` or `~/.config/nvim/init.vim` file
2. Add the following lines to tell Copilot to use the proxy and not care about SSL certificates:

```vim
let g:copilot_proxy = "http://127.0.0.1:8080"
let g:copilot_proxy_strict_ssl = v:false
```

### VSCodium

1. Open the settings with `Ctrl + ,`
2. Search for "proxy"
3. Enter `http://localhost:8081` as the `Http: Proxy` setting
4. Uncheck the `Http: Proxy Strict SSL` setting

![](./images/vscodium-proxy-settings.png)

## Editing files

Open a file in your editor and start editing. You should see the traffic in the mitmproxy window once you start typing in the file. By default, Copilot will be active on startup and for more or less all file types, and send the content of the file to the server every time you type a character.

As seen in `api_reader.bad.py`, Copilot will send the content of the file to the server, which contains the API key. This is a bad practice, as the API key should not be shared with anyone. 

```python
# Define the API endpoint
api_url = 'https://example-api.com/data'
api_key = 'SEUNiTMcpNyXKXnnaNTz70pe0kWm'
```

The `api_reader.better.py` file shows how to store the API key in a separate YAML file, which will prevent Copilot from sending the key to the server when just editing the Python file.

```python
# Read API key from the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['api_key']
api_url = config['api_url']
```
The YAML file is added to the `.gitignore` file to avoid commiting the API key to the git repo. If you were to edit the YAML file though, Copilot would still send the content to the server, as it does not respect the `.gitignore` file.









