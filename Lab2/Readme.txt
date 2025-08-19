BackupManager

A simple shell script to create a backup of files and folders, compress them, and store them into a tar archive.

🔹 How it works

The script starts by preparing a base tar command with the -c (create) option.

It repeatedly asks the user for absolute paths of files/folders they want to include.

After each entry, it asks if the user wants to add more.

Once the user is done, it asks for a name of the backup file.

It runs the built command and generates a .tar file containing the selected files/folders.

🔹 Commands Used

tar -c
Creates a new tar archive.

tar -f <filename>
Specifies the name of the archive file to create.

read
Reads user input from the terminal.

while [ "$option" != "n" ]
Loops until the user enters n to stop adding more files.

Command building (command="$command $FileName")
Dynamically builds the tar command with all the selected files and folders.

Command substitution ($($command))
Executes the final built tar command.

🔹 Example Run


$ ./BackupManager.sh
This is a tool to create a backup of files/folders and compress them
Enter the absolute path of the file/folder
/home/user/Documents/report.docx
Any more files to backup?(Y/n)
Y
Enter the absolute path of the file/folder
/home/user/Pictures
Any more files to backup?(Y/n)
n
What would you like to name the backup file
mybackup.tar

Perfect 👍 I’ve gone through the three scripts. Below are **README.md style explanations** for each, similar to the one we wrote for `BackupManager`.

---

# 🔑 PasswordGenerator

A shell script to generate **random secure passwords**. The user can either:

* Generate a strong random password with `openssl`, or
* Customize the password length and composition (uppercase, lowercase, numbers, special characters).

---

## 🔹 How it works

1. Functions (`upper`, `lower`, `number`, `special`) generate random characters from defined sets.
2. The script asks the user whether they want an **OpenSSL password** or a **custom password**.
3. For custom passwords:

   * User specifies how many uppercase, lowercase, numbers, and special characters they want.
   * The script randomly picks characters and concatenates them.
4. The final password is displayed to the user.

---

## 🔹 Commands Used

* **`$RANDOM`** → Generates random integers used for selecting characters.
* **Parameter expansion `${s:$index:1}`** → Extracts a character at position `$index` from a string.
* **`openssl rand -base64 N`** → Generates cryptographically secure random strings.
* **String concatenation** → Builds the password by appending characters in a loop.

---

## 🔹 Example Run

```bash
$ ./PasswordGenerator.sh
Do you want an OpenSSL password or custom one? (openssl/custom)
custom
Enter number of uppercase letters: 3
Enter number of lowercase letters: 4
Enter number of digits: 2
Enter number of special characters: 1
Generated password: AbXhjs92@
```

---

# 🖥️ ResourceMonitor

A shell script to monitor **system processes** and display the **top 5 CPU and memory consuming processes** every 5 seconds.

---

## 🔹 How it works

1. Runs in an **infinite loop**, refreshing every 5 seconds.
2. Clears the screen and prints two sections:

   * Top 5 processes by **memory usage**.
   * Top 5 processes by **CPU usage**.
3. Press `Ctrl+C` to exit.

---

## 🔹 Commands Used

* **`ps -e -o pid,ppid,comm,pmem --sort=-%mem`** → Lists processes sorted by memory usage.
* **`ps -e -o pid,ppid,comm,pcpu --sort=-%cpu`** → Lists processes sorted by CPU usage.
* **`head -n 6`** → Takes header + top 5 results.
* **`while true; do ... done`** → Infinite monitoring loop.
* **`clear`** → Refreshes screen before each update.

---

## 🔹 Example Run

```bash
$ ./ResourceMonitor.sh
This is Resource Monitor that shows the top 5 processes that use most cpu and memory.
Press Ctrl+C to exit

Top 5 by Memory consumption
  PID  PPID COMMAND %MEM
  123     1 firefox 15.0
  456     1 chrome  12.5
  ...

Top 5 by CPU consumption
  PID  PPID COMMAND %CPU
  789     1 gcc     99.0
  555     1 java    55.5
  ...
```

---

# ➗ BasicCalculator

A shell script that acts as a **simple calculator** using shell arithmetic.

---

## 🔹 How it works

1. Greets the user and explains its purpose.
2. Loops until the user chooses to quit.
3. Reads a mathematical expression from the user.
4. Uses **bash arithmetic expansion** `$(( ))` to evaluate the expression.
5. Displays the result.

---

## 🔹 Commands Used

* **`read`** → Accepts input expressions from the user.
* **`$((expression))`** → Performs integer arithmetic (supports `+`, `-`, `*`, `/`, `%`).
* **`while [ "$option" != "n" ]`** → Loop until user quits.

---

## 🔹 Example Run

```bash
$ ./BasicCalculator.sh
This is a basic calculator that can compute basic mathematical expressions including additions and multiplications

Enter the expression to execute
5+3*2
Output : 11

Would you like to continue?(Y/n)
n
```

---

