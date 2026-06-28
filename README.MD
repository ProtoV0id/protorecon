<div align="center">

# ProtoRecon

### A Modular Passive OSINT Framework for Security Professionals

*Fast. Modular. Built for reconnaissance.*

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## Overview

ProtoRecon is a modular Open Source Intelligence (OSINT) framework designed for passive reconnaissance.

Inspired by the workflow of Metasploit while remaining focused entirely on intelligence gathering, ProtoRecon provides an interactive console, target management, and expandable modules that make reconnaissance fast, organized, and repeatable.

The goal is simple:

> Collect information, not alerts.

ProtoRecon is intended for:

- Penetration Testers
- Red Teams
- Blue Teams
- OSINT Researchers
- Threat Intelligence Analysts
- Students learning reconnaissance

---

## Current Features

### Interactive Console

- Clean terminal interface
- Rich-powered tables and formatting
- Built-in help system
- Persistent command loop

### Target Management

Store targets once and reuse them across modules.

Example:

```text
target add example.com

target list

target aim 1
```

Modules automatically use the currently selected target.

---

### Current Modules

| Module | Description |
|---------|-------------|
| whois | Passive WHOIS lookup |
| username | Username enumeration using Sherlock |

Example:

```text
run whois target
```

or

```text
run username 1
```

---

## Planned Modules

The roadmap is focused on passive reconnaissance.

- DNS Enumeration
- Certificate Transparency Search
- ASN Lookup
- Reverse DNS
- Passive Subdomain Enumeration
- Email Intelligence
- GitHub Enumeration
- Breach Search
- Metadata Extraction
- Social Media Discovery
- Passive Vulnerability Intelligence
- Shodan Integration
- Censys Integration
- URL Intelligence
- Technology Fingerprinting
- Wayback Machine Lookup
- Security Headers
- CVE Intelligence
- Reporting Engine

---

## Planned Framework Features

- Module marketplace
- Configuration profiles
- Workspaces
- Report generation
- JSON export
- HTML reports
- API integrations
- Progress spinners
- Colorized output
- Module auto-discovery
- Plugin system

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOURUSERNAME/protorecon.git

cd protorecon
```

Install dependencies

```bash
pip install .
```

or

```bash
pip install -e .
```

---

## Usage

Launch ProtoRecon

```bash
protorecon
```

Example session

```text
ProtoRecon >

target add example.com

target list

target aim 1

run whois target

modules
```

---

## Project Structure

```
protorecon/

├── framework/
│   ├── cli.py
│   ├── state.py
│   ├── registry.py
│   ├── targets.py
│   └── ui.py
│
├── modules/
│   ├── whois.py
│   ├── username.py
│   └── modules.py
│
├── utils/
│
└── pyproject.toml
```

---

## Philosophy

ProtoRecon follows a few core principles.

- Passive first
- Modular by design
- Clean terminal experience
- Easy to extend
- Learn by building
- Minimize unnecessary dependencies

---

## Contributing

Contributions are welcome.

If you'd like to build a module:

1. Fork the project
2. Create your feature branch
3. Submit a pull request

Module developers are encouraged to follow the existing module interface for consistency.

---

## Roadmap

- [x] Interactive console
- [x] Target management
- [x] WHOIS module
- [x] Username enumeration
- [ ] Vulnerability intelligence
- [ ] Report generation
- [ ] Plugin loader
- [ ] Configuration profiles
- [ ] Workspace support
- [ ] Module marketplace

---

## Legal

ProtoRecon is intended for:

- Authorized security assessments
- Defensive security
- Education
- Research

Users are responsible for complying with all applicable laws and obtaining proper authorization before performing reconnaissance activities.

---

## License

MIT License

---

<div align="center">

**ProtoRecon**

*"Passive intelligence. Active defense."*

</div>