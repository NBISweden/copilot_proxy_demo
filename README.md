# Copilot Proxy Demo

A demo repo to show what Copilot sends to GitHub.

## Man-in-the-Middle Proxy

Start the mitmproxy container with the following command:

```bash
docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8081:8080 mitmproxy/mitmproxy
```

This will open a window that shows you all traffic that goes through the proxy.

## Configure Copilot

Install the Copilot extension for your editor the way you usually do, and then configure the proxy settings.

### Vim/Neovim

1. Edit the `~/.vimrc` or `~/.config/nvim/init.vim` file
2. Add the following lines:

```vim
let g:copilot_proxy = "127.0.0.1:8080"
let g:copilot_proxy_strict_ssl = v:false
```

### VSCodium

1. Open the settings with `Ctrl + ,`
2. Search for "proxy"
3. Enter `http://localhost:8081` as the `Http: Proxy` setting
4. Uncheck the `Http: Proxy Strict SSL` setting

![](./images/vscodium-proxy-settings.png)

## Edit files

Open a file in your editor and start editing. You should see the traffic in the mitmproxy window once you start typing in the file.










