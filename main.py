# main.py
# System Footprinting & Privacy Dashboard | Cyber Range as a Service (CRaaS) Simulation
# Educational Use Only: Runs locally, gathers only non-sensitive metadata, simulates attack/defense safely.

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import platform, socket, os, time, threading, json, math
from datetime import datetime

class CRaaSFootprintSim:
    def __init__(self, root):
        self.root = root
        self.root.title("CRaaS | System Footprinting & Privacy Dashboard")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f5f7fa")

        # Simulation State
        self.session_id = f"CR-{int(time.time())}"
        self.attacking = False
        self.exposure = {"network": False, "os": False, "services": False, "env_data": False}
        self.privacy_score = 100
        self.logs = []
        self.defenses = {"firewall": False, "service_hardening": False, "privacy_mode": False}

        self.build_ui()
        self.log(f"[{self.session_id}] CRaaS session initialized.")

    def build_ui(self):
        # Header
        header = tk.Label(self.root, text="🛡️ System Footprinting & Privacy Dashboard | Cyber Range as a Service", 
                          font=("Segoe UI", 14, "bold"), bg="#2c3e50", fg="#ecf0f1", pady=8)
        header.pack(fill=tk.X)

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # LEFT: Attack Panel
        left = ttk.LabelFrame(main_frame, text="🔍 Attack Simulation (Footprinting)")
        left.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=True)

        self.btn_start = ttk.Button(left, text="▶ Start Footprint", command=self.start_attack)
        self.btn_start.pack(pady=5, fill=tk.X)
        self.btn_step = ttk.Button(left, text="⏭ Next Phase", command=self.next_phase, state=tk.DISABLED)
        self.btn_step.pack(pady=5, fill=tk.X)
        ttk.Button(left, text="⏹ Reset Session", command=self.reset_session).pack(pady=5, fill=tk.X)

        self.attack_log = scrolledtext.ScrolledText(left, height=12, font=("Consolas", 9))
        self.attack_log.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # CENTER: Privacy Dashboard
        center = ttk.LabelFrame(main_frame, text="📊 Privacy Dashboard")
        center.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=True)

        self.canvas = tk.Canvas(center, height=120, bg="#ffffff")
        self.canvas.pack(fill=tk.X, pady=10)
        self.score_bar = self.canvas.create_rectangle(10, 50, 10, 90, fill="#2ecc71", outline="")
        self.score_label = tk.Label(center, text="Privacy Score: 100/100", font=("Segoe UI", 12, "bold"))
        self.score_label.pack()

        self.metrics_frame = ttk.Frame(center)
        self.metrics_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        self.metric_labels = {}
        for key in self.exposure:
            lbl = tk.Label(self.metrics_frame, text=f"{key.replace('_',' ').title()}: ✅ Hidden", font=("Segoe UI", 10))
            lbl.pack(anchor=tk.W, pady=2)
            self.metric_labels[key] = lbl

        # RIGHT: Defense Panel
        right = ttk.LabelFrame(main_frame, text="🛡️ Defense Controls")
        right.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=True)

        self.def_btns = {}
        for key in self.defenses:
            btn = ttk.Button(right, text=f"Enable {key.replace('_',' ').title()}", 
                             command=lambda k=key: self.apply_defense(k))
            btn.pack(fill=tk.X, pady=5)
            self.def_btns[key] = btn

        ttk.Button(right, text="📥 Export Session Log", command=self.export_log).pack(fill=tk.X, pady=10)

        self.status_bar = tk.Label(self.root, text="Status: Idle | CRaaS Mode: Active", 
                                   relief=tk.SUNKEN, anchor=tk.W, bg="#34495e", fg="white", padx=5)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def update_dashboard(self):
        exposed_count = sum(1 for v in self.exposure.values() if v)
        mitigation_count = sum(1 for v in self.defenses.values() if v)
        self.privacy_score = max(0, 100 - (exposed_count * 30) + (mitigation_count * 15))
        self.privacy_score = min(100, self.privacy_score)

        self.canvas.coords(self.score_bar, 10, 50, 10 + (self.privacy_score * 2.8), 90)
        color = "#2ecc71" if self.privacy_score > 70 else "#f1c40f" if self.privacy_score > 40 else "#e74c3c"
        self.canvas.itemconfig(self.score_bar, fill=color)
        self.score_label.config(text=f"Privacy Score: {self.privacy_score}/100")

        for k, v in self.exposure.items():
            state = "⚠️ Exposed" if v else "✅ Hidden"
            self.metric_labels[k].config(text=f"{k.replace('_',' ').title()}: {state}", 
                                         fg="#e74c3c" if v else "#27ae60")

        self.root.update()

    def start_attack(self):
        if self.attacking: return
        self.attacking = True
        self.btn_start.config(state=tk.DISABLED)
        self.btn_step.config(state=tk.NORMAL)
        self.log("🚀 Footprint simulation started.")
        self.status_bar.config(text="Status: Attack Active | CRaaS Mode: Simulating")
        self.root.after(100, self.next_phase)

    def next_phase(self):
        phases = [
            ("network", "🌐 Scanning local network interfaces..."),
            ("os", "🖥️ Fingerprinting OS & kernel metadata..."),
            ("services", "🔌 Enumerating active local services..."),
            ("env_data", "📦 Collecting environment & user context...")
        ]
        for phase_key, msg in phases:
            if not self.exposure[phase_key]:
                self.exposure[phase_key] = True
                self.log(msg)
                self.log(f"   ↳ Result: {self.simulate_result(phase_key)}")
                break
        else:
            self.log("✅ Footprint complete. All phases executed.")
            self.attacking = False
            self.btn_start.config(state=tk.NORMAL)
            self.btn_step.config(state=tk.DISABLED)
            self.status_bar.config(text="Status: Attack Finished | CRaaS Mode: Idle")

        self.update_dashboard()
        if self.attacking:
            self.btn_step.config(state=tk.NORMAL)

    def simulate_result(self, phase):
        safe_data = {
            "network": f"{socket.gethostname()} | {socket.gethostbyname(socket.gethostname())}",
            "os": f"{platform.system()} {platform.release()} | Arch: {platform.machine()}",
            "services": "sshd, httpd, postgres (simulated)",
            "env_data": f"User: {os.getenv('USER', 'local')}, Shell: {os.getenv('SHELL', 'bash')}"
        }
        return safe_data.get(phase, "N/A")

    def apply_defense(self, key):
        if self.defenses[key]:
            self.log(f"⚠️ {key.replace('_',' ').title()} already active.")
            return
        self.defenses[key] = True
        self.log(f"🛡️ Applied: {key.replace('_',' ').title()}")
        self.def_btns[key].config(text=f"✅ {key.replace('_',' ').title()} Active", state=tk.DISABLED)
        self.update_dashboard()

    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {msg}")
        self.attack_log.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.attack_log.see(tk.END)

    def reset_session(self):
        self.exposure = {k: False for k in self.exposure}
        self.defenses = {k: False for k in self.defenses}
        self.privacy_score = 100
        self.attacking = False
        self.logs.clear()
        self.attack_log.delete(1.0, tk.END)
        for k in self.def_btns:
            self.def_btns[k].config(text=f"Enable {k.replace('_',' ').title()}", state=tk.NORMAL)
        self.btn_start.config(state=tk.NORMAL)
        self.btn_step.config(state=tk.DISABLED)
        self.update_dashboard()
        self.log("🔄 Session reset. Ready for new simulation.")
        self.status_bar.config(text="Status: Idle | CRaaS Mode: Active")

    def export_log(self):
        with open(f"{self.session_id}_cr_log.json", "w") as f:
            json.dump({"session": self.session_id, "logs": self.logs, "final_score": self.privacy_score}, f, indent=2)
        messagebox.showinfo("Export Complete", f"Session log saved to {self.session_id}_cr_log.json")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRaaSFootprintSim(root)
    root.mainloop()