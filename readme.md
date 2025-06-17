# Glimmer Network Vulnerability Scanner

A lightweight Python-based network scanner that detects live hosts and scans for open ports, performing basic banner grabbing to help identify potentially vulnerable services on your network.

---

## Overview

This tool allows you to quickly scan a local network using CIDR notation (e.g., `192.168.1.0/24`) and identify devices with open common ports. It can be used for network inventory, security assessments, or educational purposes.

> Warning: For legal and ethical reasons, **only use this scanner on networks you own or have explicit permission to test.**

---

## Tech Stack

- Language: Python 3
- Libraries:
  - `socket` – low-level networking
  - `ipaddress` – IP range parsing
  - `threading` – concurrent scanning for performance

---

## Key Features

- Scan an entire subnet for live hosts
- Detect open common ports (e.g., 22, 80, 443, 3389, etc.)
- Perform banner grabbing to help identify services
- Multithreaded for fast concurrent scanning
- Simple, lightweight, and dependency-free (except for built-in libraries)

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-vuln-scanner.git
cd python-vuln-scanner
