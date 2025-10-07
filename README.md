# Jupyter Notebook Setup and Code for Python & Java (DSA Practice)

Easily manage both **Python** and **Java** code within the Jupyter environment.
This repository consists of code to practice code and understand the concept behind the logic

---

![Project Demo](https://raw.githubusercontent.com/yashwanth2706/data-structures-algo/main/demoGif/pythonJavaJupyter.gif)

## Git Configuration on Windows

If you get this warning from Git (commonly on Windows):

> `LF will be replaced by CRLF the next time Git touches it`

Configure Git to support Unix-style line endings (recommended, especially for `.ipynb` files):

```bash
git config --global core.autocrlf false
git config --global core.eol lf
```

---

## Jupyter Installation for Python

### 1. Create a project directory and navigate into it

```bash
mkdir my_jupyter_project
cd my_jupyter_project
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### macOS/Linux:

```bash
source .venv/bin/activate
```

#### Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt):

```bash
.venv\Scripts\activate.bat
```

### 4. Install Jupyter Notebook

```bash
pip install jupyter
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## IJava Kernel Installation (Pre-built Binary Method)

This guide explains how to install the **IJava kernel** for Jupyter using pre-built binaries. This avoids common compatibility issues with Gradle or newer Java versions.

### Prerequisites

* **Java Development Kit (JDK 9 or higher)** — Preferably JDK 17 or JDK 21.
* **Python & Jupyter** — Ensure both are installed.

---

### Installation Steps

#### 1. Download the latest pre-built binary

```bash
wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip
```

#### 2. Unzip the archive

```bash
unzip ijava-1.3.0.zip
```

#### 3. Run the installer script

Do **not** `cd` into the `java` subdirectory. Run:

```bash
python3 install.py --sys-prefix
```

#### 4. Verify installation

```bash
jupyter kernelspec list
```

You should see `java` in the list of installed kernels.

---

## Usage

1. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

2. **Create a New Notebook** → Choose the **Java** kernel.

3. **Run Java Code Interactively**:

   ```java
   String message = "Hello from IJava!";
   System.out.println(message);
   ```

---

## Troubleshooting

* **Error:** `can't open file 'install.py': [Errno 2] No such file or directory`

  * Make sure you are running the script from the correct directory (e.g., `~/JupyterInstallation/IJava`).
  * Do **not** navigate into the `java` subdirectory.

* **Gradle Build Issues:**

  * If you face issues with `gradlew` during source build, use the **pre-built binary** approach above to avoid version mismatches.

---
