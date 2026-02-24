# 🛡️ Pickle-Bypass-Research
### Bypassing AI Model Security Scanners with Advanced Bytecode Obfuscation

This repository contains my research on exploiting and bypassing static analysis tools for ML models (specifically **ModelScan** by Protect AI). 

## 🔍 Research Overview
The goal was to demonstrate how serialized Python objects (Pickle) can be weaponized to achieve **Remote Code Execution (RCE)** while remaining undetected by popular security scanners.

## 🚀 The Evolution of the Bypass
I developed 10 versions of the exploit, moving from simple signatures to complex logic obfuscation:

1.  **v1-v5**: Basic attacks using `os.system`, `eval`, and `shutil`. (Detected by ModelScan ❌)
2.  **v7**: Manual Bytecode construction (Protocol 0). (Detected ❌)
3.  **v8-v9**: Attribute obfuscation using `getattr` and `operator.attrgetter`. (Detected ❌)
4.  **v10 (The Ghost)**: **Successful Bypass** using `pydoc.locate`. (Undetected ✅)

## 🏆 Key Finding: The pydoc.locate Bypass
By utilizing the `pydoc.locate` function, the exploit dynamically resolves sensitive functions like `os.system` at runtime. Since the bytecode doesn't contain direct references to dangerous modules, it successfully evades static signature-based detection.

## 🛠️ Environment
- **Hardware:** MacBook Pro M4 (Apple Silicon)
- **Isolation:** Docker (python:3.11-slim)
- **Target Scanner:** ModelScan v0.x

## ⚠️ Disclaimer
This research is for educational and ethical security testing purposes only.
