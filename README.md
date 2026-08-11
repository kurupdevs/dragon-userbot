# 🐉 Dragon Userbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-orange)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)

**A simple, fast, lightweight and highly customizable Telegram Userbot.**

[Features](#-features) · [Setup](#-setup) · [Commands](#-commands) · [Deploy](#-deploy)

</div>

---

## 📦 Features

- ⚡ **Fast & Lightweight** — Minimal resource usage, maximum speed
- 🎛️ **Highly Customizable** — Easy to add your own modules
- 🔌 **Plug-and-Play Modules** — Just drop a `.py` file in `modules/`
- 🎯 **11 Built-in Modules** — Ping, Alive, Spam, PM Permit, TagAll, Shayari, and more

### Module List

| Module | Command | Description |
|--------|---------|-------------|
| Ping | `.ping` | Check bot latency |
| Alive | `.alive` | Show uptime status |
| Spam | `.spam <count> <msg>` | Send repeated messages |
| PM Permit | Auto | Approve/block PM requests |
| TagAll | `.tagall <msg>` | Tag all group members |
| Shayari | `.shayari` | Random shayari |
| Magic | `.magic` | Fun magic tricks |
| Gali | `.gali` | Generate text |
| Flirt | `.flirt` | Random flirt lines |
| FakeCoding | `.code` / `.hack` | Fake coding animation |
| ModList | `.modlist` | List installed modules |

---

## 🚀 Setup

### Prerequisites
- Python 3.9+
- Telegram API credentials from [my.telegram.org](https://my.telegram.org/apps)

### Quick Install

```bash
git clone https://github.com/kurupdevs/dragon-userbot.git
cd dragon-userbot
pip install -r requirements.txt
# Create .env with your API_ID and API_HASH
python main.py
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID | Yes |
| `API_HASH` | Telegram API Hash | Yes |

---

## 🐳 Deploy

### Docker
```bash
docker build -t dragon-userbot .
docker run -d --env-file .env dragon-userbot
```

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <strong>Built with 💜 by <a href="https://github.com/kurupdevs">KurupDevs</a></strong>
</div>
