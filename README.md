<div align="center">

<img src="assets/rasa.png" width="120" alt="Rasa logo" />

# Rasa

**Persian & English Keyboard Switcher**
A fast and lightweight keyboard language converter for Windows.

![Version](https://img.shields.io/badge/Version-v1.0.0-1f6feb)
![Python](https://img.shields.io/badge/Python-3.14.7-d4a72c)
![License](https://img.shields.io/badge/License-Rasa_License-238636)

</div>

[English](README.md) | [فارسی](README_FA.md)

---

<a id="english"></a>

### What is Rasa?

**Rasa** is a lightweight Windows utility designed to quickly convert incorrectly typed text between **Persian and English keyboard layouts**.

Have you ever started typing in Persian while your keyboard was set to English?

For example:

```text
slhk
```

instead of:

```text
سلام
```

Rasa helps solve this problem without requiring you to retype the entire sentence.

### ✨ Why Rasa?

Switching keyboard languages and retyping text can be annoying, especially when you notice the mistake after typing a complete sentence.

Rasa provides a simple workflow:

```text
Type with the wrong keyboard layout
            ↓
        Press a shortcut
            ↓
      Rasa processes the text
            ↓
       Text is converted
            ↓
      Continue working
```

The goal is simple:

> **Fix your text. Don't type it again.**

### ⚡ Quick Access

Rasa is designed to run quietly in the Windows system tray.

You do not need to keep a window open while using it.

#### Use Rasa

Press the configured global shortcut while working in another application.

Rasa can access the selected or copied text, convert the keyboard layout, and place the corrected text back into the clipboard.

This makes Rasa useful while working with:

```text
Web Browsers
Text Editors
Chat Applications
Code Editors
Office Applications
Terminal Applications
```

### 🧠 What Can Rasa Do?

#### 🇮🇷 Persian → English

Rasa can convert text typed with the Persian keyboard layout into its corresponding English keyboard input.

For example:

```text
ضصثقفغعهخح
```

can be converted according to the standard Persian keyboard mapping.

#### 🇬🇧 English → Persian

Rasa can also convert English-keyboard text into Persian.

For example:

```text
slhk
```

becomes:

```text
سلام
```

This is useful when you accidentally type Persian text while your keyboard is still using the English layout.

### ⌨️ Keyboard Mapping

Rasa uses keyboard-layout mappings to convert characters.

Example:

```text
English → Persian

q → ض
w → ص
e → ث
r → ق
t → ف
y → غ
u → ع
i → ه
o → خ
p → ح
[ → ج
] → چ
\ → پ
```

The mapping can be extended to support additional characters and keyboard states.

### 🔄 Simple Workflow

Rasa is designed to keep the workflow as simple as possible:

```text
Select or copy text
        ↓
Press Rasa shortcut
        ↓
Read clipboard content
        ↓
Detect / convert keyboard layout
        ↓
Replace the text
        ↓
Continue working
```

This allows the user to correct keyboard-layout mistakes without manually retyping the text.

### 🖥️ System Tray

Rasa works as a Windows system-tray application.

The application can remain active in the background while keeping the desktop clean.

The tray menu provides access to Rasa controls and application actions.

Example:

```text
Rasa
│
├── Shortcut
│
└── Exit
```

### 🔥 Key Features

| Feature              | Description                                       |
| -------------------- | ------------------------------------------------- |
| ⚡ Fast Conversion    | Quickly convert incorrectly typed text            |
| 🇮🇷 Persian Support | Convert text using the Persian keyboard layout    |
| 🇬🇧 English Support | Convert text using the English keyboard layout    |
| ⌨️ Global Shortcut   | Trigger Rasa while using other applications       |
| 📋 Clipboard Support | Work with text through the Windows clipboard      |
| 🖥️ System Tray      | Run quietly in the Windows notification area      |
| 🪶 Lightweight       | Designed to use minimal system resources          |
| 🔄 Keyboard Mapping  | Convert characters using keyboard-layout mappings |
| 🎨 Modern UI         | Built with a clean PySide6 interface              |
| 🌐 Windows Support   | Designed for Windows desktop environments         |

### ⌨️ Keyboard Shortcut

Rasa uses a global keyboard shortcut to trigger text conversion.

The shortcut can be configured in the application.

Example:

```text
Global Shortcut
       ↓
     Rasa
       ↓
Read clipboard
       ↓
Convert text
       ↓
Replace clipboard text
```

The shortcut is designed to work while another application is in focus.

### 📋 Clipboard

Rasa uses the Windows clipboard as part of its text-conversion workflow.

The general process is:

```text
Application
     ↓
Selected / copied text
     ↓
Windows Clipboard
     ↓
Rasa
     ↓
Keyboard Layout Conversion
     ↓
Updated Clipboard
```

This allows Rasa to work with text from many different Windows applications.

### 🔐 Privacy

Rasa is designed around local text processing.

The keyboard-layout conversion does not require a remote server or online translation service.

The conversion process is performed locally on the user's computer.

> Rasa does not need an internet connection for its core keyboard-layout conversion functionality.

### 🏗️ Architecture

Rasa separates the user interface, keyboard handling, clipboard processing, and language conversion logic.

```text
                          Rasa
                            │
              ┌─────────────┴─────────────┐
              │                           │
          User Interface              Core Logic
              │                           │
              │              ┌────────────┼────────────┐
              │              │            │            │
              │           Hotkey       Clipboard    Language
              │           Manager       Manager      Mapping
              │              │            │            │
              └──────────────┴────────────┴────────────┘
                             │
                       Text Conversion
```

This structure makes the project easier to maintain and provides a foundation for future features.

### 📦 Project Components

The main components of Rasa include:

```text
Hotkey Manager
Clipboard Manager
Language Switcher
Notification Manager
Theme Loader
System Tray
PySide6 UI
```

Each component has a specific responsibility within the application.

### 🛠️ Technology Stack

Rasa is built primarily with:

* **Python**
* **PySide6**
* **pynput**
* **Windows Clipboard**
* **Keyboard Layout Mapping**

#### Runtime

```text
Windows 10
Windows 11
```

#### Development

```text
Python 3.14.7
PySide6
pynput
```

> The exact Python version used for each release is specified in the corresponding release information.

### 📦 Installation

#### Option 1 — Download the Release

The easiest way to use Rasa is to download the latest release.

**Latest Release:** [Go to release page](https://github.com/Tavanafzar/Rasa/releases/)

Download the latest version and run the application.

### 🗺️ Roadmap

Rasa is an evolving project. Potential future improvements include:

* [ ] Automatic language detection
* [ ] More complete Persian keyboard mapping
* [ ] Improved text conversion
* [ ] Custom keyboard layouts
* [ ] Custom global shortcut
* [ ] More Windows integration
* [ ] Better clipboard handling
* [ ] Additional language support
* [ ] Customizable notifications
* [ ] Improved system-tray controls
* [ ] Startup with Windows
* [ ] More advanced text correction

The roadmap may change as Rasa develops.

### 🐛 Bug Reports

Found a problem? Please create a GitHub Issue and include:

* Rasa version
* Windows version
* Steps to reproduce the problem
* Expected behavior
* Actual behavior
* Relevant screenshots
* Error messages or logs

### 💡 Feature Requests

Have an idea for Rasa? Open a Feature Request and describe:

```text
What should Rasa do?
Why would this feature be useful?
How should the feature work?
```

Screenshots, examples, and use cases are welcome.

### 📜 License

Rasa is distributed under the license specified in this repository.

See:

[Read the License](LICENSE)

### 👨‍💻 Author

**GitHub — [PARSA MIRI](https://github.com/PARSAMIRI)**

Developer and creator of **Rasa**.

> ⭐ **Star the repository if you like Rasa!**
> If Rasa is useful to you, consider giving the repository a star on GitHub.

---

<div align="center">

**Rasa — Type it wrong. Fix it fast.**

Made with ❤️ by Parsa Miri

</div>
