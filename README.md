# Jupyter notebook based Python & Java code for DSA practice
- Easily manage both Python and Java code with Jupyter envirornment

Configuration:
If you get a warning from git (This likely can happen in Windows)
"LF will be replaced by CRLF the next time Git touches it"

Configure git to support Unix like systems (Even when there is no warning)
(Recommended for managing .ipynb files)

`git config --global core.autocrlf false`

`git config --global core.eol lf`


## Jupyter installtion for Java and Python

# IJava Kernel for Jupyter: Installation via Pre-built Binary

This guide outlines the steps to install the IJava kernel for Jupyter using the pre-built binary method. This approach avoids common compatibility issues with Gradle and newer Java versions.

## Prerequisites

-   **Java Development Kit (JDK) 9 or higher**: You must have a JDK installed and configured on your system. A recent LTS version like JDK 17 or JDK 21 is recommended.
-   **Python and Jupyter**: Ensure you have Python and the `jupyter` package installed.

## Installation Steps

1.  **Download the latest pre-built binary**. Obtain the `ijava-$version.zip` file from the [IJava GitHub releases page](https://github.com/SpencerPark/IJava/releases/).

    ```sh
    wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip
    ```

2.  **Unzip the archive**. Extract the contents of the downloaded ZIP file.

    ```sh
    unzip ijava-1.3.0.zip
    ```

3.  **Run the installer script**. This script, `install.py`, is now in your current directory (`~/JupyterInstallation/IJava`). You should not `cd` into the `java` subdirectory.

    ```sh
    python3 install.py --sys-prefix
    ```

4.  **Verify the installation**. Confirm the Java kernel is successfully installed by listing all available kernels.

    ```sh
    jupyter kernelspec list
    ```
    You should see `java` in the list of installed kernels.

## Usage

1.  **Launch Jupyter**: From your terminal, start the Jupyter Notebook server.

    ```sh
    jupyter notebook
    ```

2.  **Create a New Java Notebook**: In your web browser, click the **New** button and select the **Java** kernel.

3.  **Execute Java code**: You can now write and run Java code in the notebook's cells, leveraging the interactive features of JShell.

    ```java
    String message = "Hello from IJava!";
    System.out.println(message);
    ```

## Troubleshooting

-   **`Error: can't open file 'install.py': [Errno 2] No such file or directory`**: If you see this error, ensure you are running the `install.py` script from the correct directory (`~/JupyterInstallation/IJava`), not from inside the `java` subdirectory.

-   **Installation issues with `gradlew`**: If you encounter issues when building from source with `gradlew`, using the pre-built binary method (as you did) is the correct approach to avoid potential version mismatch problems with newer Java versions.
