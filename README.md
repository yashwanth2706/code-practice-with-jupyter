# Run C, Java, Python, Bash in a single Jupyter Notebook
![Project Demo](https://raw.githubusercontent.com/yashwanth2706/jupyter-setup-template/main/demo_gif/pythonJavaJupyter.gif)
---

## Supported Languages

| Language | Kernel Name | Package / Source | Notes |
|-----------|--------------|------------------|--------|
| Python | `python3` | Built-in (`ipykernel`) | Installed with Jupyter by default |
| Bash | `bash` | [`bash_kernel`](https://github.com/takluyver/bash_kernel) | Executes shell commands directly |
| C | `c` | [`jupyter-c-kernel`](https://github.com/brendan-rius/jupyter-c-kernel) | Compiles with GCC and runs natively |
| Java | `jbang-jjava` | [`JBang`](https://www.jbang.dev) / [`jupyter-java`](https://github.com/jupyter-java) | Runs Java interactively using JBang |

---

## Installation Guide (Debian / Ubuntu)

> Tested on Debian 13

### 1. System Prerequisites
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip openjdk-17-jdk gcc g++ wget unzip
```

### 2. Create and Activate a Virtual Environment
```bash
mkdir -p ~/JupyterInstallation && cd ~/JupyterInstallation
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install and Launch JupyterLab
```bash
pip install --upgrade pip
pip install jupyterlab
```

### 4. Add Kernels

#### Python (default)
Installed automatically with Jupyter.
```bash
python -m ipykernel install --user
```

#### Bash
```bash
pip install bash_kernel
python -m bash_kernel.install
```

#### C
```bash
pip install jupyter-c-kernel
install_c_kernel --user
```

#### Java (via JBang)
```bash
curl -Ls https://sh.jbang.dev | bash -s - app setup
jbang trust add https://github.com/jupyter-java
jbang app install --name=jbang-jjava jupyter@jupyter-java
```

Check installation:
```bash
jbang --version
```

### 5. Verify All Kernels
```bash
jupyter kernelspec list
```

Expected output:
```
Available kernels:
  python3       /home/user/.local/share/jupyter/kernels/python3
  bash          /home/user/.local/share/jupyter/kernels/bash
  c             /home/user/.local/share/jupyter/kernels/c
  jbang-jjava   /home/user/.local/share/jupyter/kernels/jbang-jjava
```

### 6. Start JupyterLab
```bash
jupyter lab
```
Then open a new notebook and choose your desired kernel (Python, C, Bash, or Java).

---

## Example Code Snippets

### Python
```python
print("Hello from Python!")
```

### Bash
```bash
echo "Hello from Bash!"
```

### C
```c
#include <stdio.h>
int main() {
    printf("Hello from C!\\n");
    return 0;
}
```

### Java
```java
class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Java!");
    }
}
```

---

## Maintenance

Remove a kernel:
```bash
jupyter kernelspec remove <kernel_name>
```

Update everything:
```bash
pip install --upgrade jupyterlab bash_kernel jupyter-c-kernel
jbang app install --force --name=jbang-jjava jupyter@jupyter-java
```

---

## License
MIT License — use freely with attribution.

---

### Notes
- All kernels are installed under `~/.local/share/jupyter/kernels/`.
- Requires JupyterLab ≥ 4.0 and Python ≥ 3.8.
- Each language executes within its isolated kernel backend.
