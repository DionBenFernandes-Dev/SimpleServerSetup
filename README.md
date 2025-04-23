# SimpleServerSetup

A simple Python project demonstrating calculator operations via two client-server communication modes: **Server-Sent Events (SSE)** and **Standard Input/Output (STDIO)**. This project is ideal for learning about basic client-server architecture and dual-mode communication in Python.

---

## File Structure

```
SimpleServerSetup/
├── .gitignore
├── .python-version
├── README.md
├── client-sse.py
├── client-stdio.py
├── pyproject.toml
├── requirements.txt
├── server.py
├── uv.lock
```

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.python-version**: Python version management file.
- **README.md**: Project documentation.
- **client-sse.py**: Python client using Server-Sent Events (SSE) to communicate with the server.
- **client-stdio.py**: Python client using Standard Input/Output (STDIO) for command-line interaction.
- **pyproject.toml**: Project metadata and build configuration.
- **requirements.txt**: Lists required Python packages.
- **server.py**: Main server logic supporting both SSE and STDIO modes.
- **uv.lock**: Dependency lock file for reproducible environments.

---

## Key Terms

- **Server-Sent Events (SSE)**: A web technology enabling a server to push real-time updates to a client over HTTP.
- **Standard Input/Output (STDIO)**: Traditional method for user interaction in the terminal, where input is provided via keyboard and output is printed to the screen.

---

## How the Project Works

**SimpleServerSetup** allows you to run a calculator service in two modes:

- **SSE Mode**:
  - The server (`server.py`) starts an HTTP endpoint for SSE.
  - The SSE client (`client-sse.py`) connects to the server, sends calculation requests, and receives results as real-time event streams.
  - Useful for web-based or networked applications that require live updates.

- **STDIO Mode**:
  - The server (`server.py`) can also handle requests from a command-line client (`client-stdio.py`).
  - The client sends expressions via standard input and receives results via standard output.
  - Ideal for quick, local calculations directly from the terminal.

Both modes use the same server logic, ensuring consistent calculation behavior.

---

## Installation & Usage

**Prerequisites:**  
- Python 3.7 or higher

**Installation:**

```bash
git clone https://github.com/DionBenFernandes-Dev/SimpleServerSetup.git
cd SimpleServerSetup
pip install -r requirements.txt
```

**Running the Project:**

- **Start the Server:**
  ```bash
  python server.py
  ```

- **Use STDIO Client:**
  ```bash
  python client-stdio.py
  ```
  Enter expressions as prompted and receive results instantly.

- **Use SSE Client:**
  ```bash
  python client-sse.py
  ```
  This client will connect to the server and handle calculations via SSE.

---