# Interactive ABC

> This algorithm, developed in `Python` using the `Pygame` library, aims to stimulate cognitive activities in children during the early stages of reading development through visual and interactive learning experiences that assist in alphabet letter recognition.
> 
> The project seeks to make contact with letters more intuitive, playful, and educational, contributing to the development of coordination, visual association, and alphabet familiarization in a fun and engaging way.

# Simulation

When a keyboard key is pressed:

- The screen changes color according to the selected letter;
- The pressed letter is displayed in highlight;
- The terminal informs which letter was typed.

Example:

```bash
This is the letter A.
```

---

# Architecture

```bash
src/
│
├── abc.py
├── README.md
└── requirements.txt
```

---

# System Requirements

To run the project, you will need:

- Windows, Linux, or MacOS computer;
- `Python 3` installed;
- `VS Code` (recommended);
- `Pygame` library installed.

---

# Python Installation

## 1. Download Python

Access the official website https://www.python.org/downloads/ and install the latest version of Python.

During installation, select the option:

```bash
Add Python to PATH
```

Then click:

```bash
Install Now
```

---

## 2. Verify Installation

Open your computer terminal and execute:

```bash
python --version
```

or:

```bash
python3 --version
```

The installed version should appear, something like:

```bash
Python 3.12.0
```

---

# VS Code Installation

## 1. Download VS Code

https://code.visualstudio.com/

---

## 2. Install the Python Extension

In `VS Code`, open the Extensions tab and search for:

```bash
Python
```

Install the latest extension developed by `Microsoft`.

---

# Pygame Installation

Open the VS Code terminal and execute:

```bash
pip install pygame
```

or:

```bash
pip3 install pygame
```

---

# requirements.txt

Create a file named:

```bash
requirements.txt
```

Containing:

```txt
pygame
```

This allows other users to automatically install the project dependencies using:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## 1. Open the Project Folder in VS Code

Structure:

```bash
interactive-abc/
│
├── abc.py
├── README.md
└── requirements.txt
```

---

## 2. Open the Terminal

In `VS Code`:

```bash
Terminal ------ New Terminal
```

---

## 3. Run the Program

```bash
python abc.py
```

or:

```bash
python3 abc.py
```

---

# Usage Method

| Key | Function |
|---|---|
| A-Z | Displays the corresponding letter |
| ESC | Closes the program |

- Press any letter on the keyboard;
- The screen color will change;
- The letter will appear highlighted;
- The terminal will display which letter was pressed.

---

# Observation

The program recognizes only alphabet letters. If other keys are pressed, the following message will be displayed:

```bash
This key is not a valid letter!
```
