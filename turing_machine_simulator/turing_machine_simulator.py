import tkinter as tk
from tkinter import messagebox
import multiprocessing
import threading
import time
import random

# ---------------------- Turing Machine Simulator Class ----------------------
class TuringMachine:
    def __init__(self, input_tape):
        self.input_tape = list(input_tape.strip()) + [' '] * 10
        self.head = len(input_tape) - 1
        self.state = 'start'
        self.carry = 0
        self.tape = self.input_tape.copy()
        self.history = []

        if '#' not in self.input_tape:
            raise ValueError("Invalid input: Missing '#' separator.")
        self.sep_index = self.input_tape.index('#')

    def step(self):
        if self.state == 'halt':
            return []

        log_steps = []
        a_ptr = self.sep_index - 1
        b_ptr = self.sep_index + 1
        result_ptr = self.sep_index + 10

        # Start state
        log_steps.append((self.tape.copy(), self.head, 'start', self.carry, "Starting Turing Machine..."))

        for i in range(3, -1, -1):
            a_pos = a_ptr - (3 - i)
            b_pos = b_ptr + i
            res_pos = result_ptr - (3 - i)

            a = int(self.tape[a_pos]) if self.tape[a_pos] in '01' else 0
            b = int(self.tape[b_pos]) if self.tape[b_pos] in '01' else 0
            total = a + b + self.carry
            bit = total % 2
            new_carry = total // 2
            self.tape[res_pos] = str(bit)

            log = f"Read:[ a({a}) + b({b}) + old carry({self.carry}) ] = {total}\nWrite: {bit}, New carry: {new_carry}\nMove: ←"
            self.head = res_pos
            self.carry = new_carry
            state_name = 'carry' if self.carry else 'no-carry'
            log_steps.append((self.tape.copy(), self.head, state_name, self.carry, log))

        if self.carry == 1:
            res_pos = result_ptr - 4
            self.tape[res_pos] = '1'
            self.head = res_pos
            log = f"Read: Final carry(1) → Write: 1\nMove: ←"
            log_steps.append((self.tape.copy(), self.head, 'final-carry', 0, log))

        self.state = 'halt'
        log_steps.append((self.tape.copy(), self.head, 'halt', self.carry, "Machine HALTED."))

        return log_steps

# ---------------------- GUI Interface ----------------------
class TMSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Turing Machine Simulator - 4-bit Binary Addition")
        self.machine = None
        self.steps = []
        self.step_index = 0

        self.input_label = tk.Label(root, text="Enter two 4-bit binaries (e.g. 1101#1011):")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, font=("Courier", 14))
        self.input_entry.pack()

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)

        self.tape_frame = tk.Frame(root)
        self.tape_frame.pack(pady=5)

        self.arrow_frame = tk.Frame(root)
        self.arrow_frame.pack()

        self.state_label = tk.Label(root, text="", font=("Courier", 12, "bold"))
        self.state_label.pack()

        self.carry_label = tk.Label(root, text="Carry: 0", font=("Courier", 12))
        self.carry_label.pack()

        self.next_step_button = tk.Button(root, text="Next Step", command=self.next_step, state=tk.DISABLED)
        self.next_step_button.pack(pady=5)

        self.log_output = tk.Text(root, height=6, width=80, font=("Courier", 10))
        self.log_output.pack(pady=5)

    def start_simulation(self):
        input_value = self.input_entry.get()
        if not self.validate_input(input_value):
            messagebox.showerror("Invalid Input", "Please enter input as 4-bit binary numbers like 1101#1011.")
            return

        self.machine = TuringMachine(input_value)
        self.steps = self.machine.step()
        self.step_index = 0
        self.next_step_button.config(state=tk.NORMAL)
        self.show_step()

    def validate_input(self, tape):
        if tape.count('#') != 1:
            return False
        a, b = tape.split('#')
        return len(a) == 4 and len(b) == 4 and all(c in '01' for c in a + b)

    def show_step(self):
        if self.step_index >= len(self.steps):
            self.next_step_button.config(state=tk.DISABLED)
            return

        tape, head, state, carry, log = self.steps[self.step_index]
        self.state_label.config(text=f"{state.upper()}")
        self.carry_label.config(text=f"Carry: {carry}")

        # Clear tape and arrow frames
        for widget in self.tape_frame.winfo_children():
            widget.destroy()
        for widget in self.arrow_frame.winfo_children():
            widget.destroy()

        # Tape and arrow display
        for i, symbol in enumerate(tape):
            label = tk.Label(self.tape_frame, text=symbol, width=2, borderwidth=2, relief="solid",
                             bg="yellow" if i == head else "white")
            label.pack(side=tk.LEFT, padx=1)

        for i in range(len(tape)):
            arrow = tk.Label(self.arrow_frame, text="↑" if i == head else "  ", width=2)
            arrow.pack(side=tk.LEFT, padx=1)

        # Log
        self.log_output.delete(1.0, tk.END)
        self.log_output.insert(tk.END, log)

    def next_step(self):
        self.show_step()
        self.step_index += 1

# ---------------------- Multiprocessing and Threading Test ----------------------
def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())

def run_multiprocessing_test():
    size = 10000000
    for procs in [5, 10, 50]:
        jobs = []

        # Multiprocessing
        start_time = time.time()
        for i in range(procs):
            out_list = [i]
            process = multiprocessing.Process(target=do_something, args=(size, out_list))
            jobs.append(process)
        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
        end_time = time.time()
        mp_time = end_time - start_time
        print(f"\nMultiprocessing Test - {procs} processes completed:")
        for idx, job in enumerate(jobs):
            print(f"  Process {idx} (PID: {job.pid}) finished.")
        print(f"Total Multiprocessing Time: {mp_time:.2f} seconds")

        # Reset jobs list for threading
        jobs = []

        # Threading
        start_time = time.time()
        for k in range(procs):
            out_list = [k]
            thread = threading.Thread(target=do_something, args=(size, out_list))
            jobs.append(thread)
        for l in jobs:
            l.start()
        for l in jobs:
            l.join()
        end_time = time.time()
        thread_time = end_time - start_time
        print(f"\nThreading Test - {procs} threads completed:")
        for idx, job in enumerate(jobs):
            print(f"  Thread {idx} finished.")
        print(f"Total Threading Time: {thread_time:.2f} seconds")
        print(f"Summary: Multiprocessing was {'faster' if mp_time < thread_time else 'slower'} by {abs(mp_time - thread_time):.2f} seconds.")

# ---------------------- Run the GUI and Test ----------------------
if __name__ == "__main__":
    # Run the GUI
    root = tk.Tk()
    app = TMSimulatorGUI(root)
    root.mainloop()

    # Run the multiprocessing and threading test
    run_multiprocessing_test()